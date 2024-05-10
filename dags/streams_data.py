import pandas as pd
from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
import logging
from dags.read_data import read_data
default_args = {"owner": "mad", "retry": 5, "retry_delay": timedelta(minutes=5)}

def get_data():
    data = read_data()
    return data.to_json()


with DAG(
    default_args=default_args,
    dag_id="ETL-analyst-data-Starbucks",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
) as dag:
    task1 = PythonOperator(task_id="read_data", python_callable=get_data)