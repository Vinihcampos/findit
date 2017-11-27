import pandas as pd 
import numpy as np

def remove_not_graduation(csv_curricular_component):
	# Read class csv
	print('--> Reading file: ' + csv_curricular_component + '.csv')
	curricular_component = pd.read_csv('../raw_data/curricular-component/' + csv_curricular_component + '.csv', delimiter=";")	
	print('--> ' + csv_curricular_component + '.csv read!')
	curricular_component = curricular_component[curricular_component.nivel.str.contains('G') == True]
	print('--> Saving file: ' + csv_curricular_component + '.csv')
	pd.DataFrame(curricular_component).to_csv('../data/curricular-component/' + csv_curricular_component + '.csv', encoding='utf-8', index=False)
	print('--> ' + csv_curricular_component + '.csv saved!')

remove_not_graduation('curricular_component')