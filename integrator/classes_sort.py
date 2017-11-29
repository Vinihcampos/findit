import pandas as pd 
import numpy as np

# Read loans csv
classes = pd.read_csv('../data/classes/classes_curricular_component.csv')

# Sorting data by date
classes = classes.sort_values(by=['data_inicio'])

pd.DataFrame(classes).to_csv('../data/classes/classes_curricular_component.csv', encoding='utf-8', index=False)