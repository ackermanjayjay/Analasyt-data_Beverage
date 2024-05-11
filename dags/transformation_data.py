from read_data import read_data
import re

# def regex_it(text):
#     text  = re.sub(r"\s","",text)
#     text  = text.lower()
#     return text
    


def transformation_data():
    """transformation:
    'Beverage_category', 'Beverage', 'Beverage_prep', 'Calories',
    ' Total Fat (g)', 'Trans Fat (g) ', 'Saturated Fat (g)', ' Sodium (mg)',
    ' Total Carbohydrates (g) ', 'Cholesterol (mg)', ' Dietary Fibre (g)',
    ' Sugars (g)', ' Protein (g) ', 'Vitamin A (% DV) ', 'Vitamin C (% DV)',
    ' Calcium (% DV) ', 'Iron (% DV) ', 'Caffeine (mg)'
    to remove whitespace to "_" and  Capitalize to lowercase
    """
    data = read_data()
    data.columns = data.columns.str.replace(r"\s+","",regex=True).str.lower()
    return data
   


print(transformation_data())
