import pandas as pd
from datetime import datetime,timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator
import logging
from transformation_data import transformation_data
default_args = {"owner": "mad", "retry": 5, "retry_delay": timedelta(minutes=5)}

def get_data():
    data = transformation_data()
    return data.to_json()

def insert_data():
    import psycopg2
    import time
    from sqlalchemy import create_engine

    res = transformation_data()
    # # Example: 'postgresql://username:password@localhost:5432/your_database'
    # code from https://medium.com/@askintamanli/fastest-methods-to-bulk-insert-a-pandas-dataframe-into-postgresql-2aa2ab6d2b24
    engine = create_engine("postgresql://airflow:airflow@host.docker.internal/data-starbucks")

    start_time = time.time()  # get start time before insert
    # Create a connection to your PostgreSQL database
    conn = psycopg2.connect(
        database="data-starbucks",
        user="airflow",
        password="airflow",
        host="host.docker.internal",
        port="5432",
    )
    cur = conn.cursor()
    try:
        res.to_sql(name="menu_starbucks", con=engine, if_exists="replace")
        conn.commit()
        end_time = time.time()  # get end time after insert
        total_time = end_time - start_time  # calculate the time
        logging.info(
            f"Insert affected : {cur.rowcount} and Insert time: {total_time} seconds"
        )

    except Exception as e:
        logging.error(f"could not insert data due to {e}")



with DAG(
    default_args=default_args,
    dag_id="ETL-analyst-data-Starbucks_to-database_v01",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@once",
) as dag:
    task1 = PythonOperator(task_id="read_data", python_callable=get_data)
    task2 = PythonOperator(task_id="insert_data_to_table", python_callable=insert_data)
    
    task1 >> task2