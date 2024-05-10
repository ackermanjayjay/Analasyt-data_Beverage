from read_data import read_data


def transformation_data():
    columns_data =  read_data()
    return columns_data.columns

print(transformation_data())