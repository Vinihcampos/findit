import pandas as pd 
import numpy as np

print('--> Reading file: curricular_component.csv')
curricular_component = pd.read_csv('../raw_data/curricular-component/curricular_component.csv', delimiter=";")	
print('--> curricular_component.csv read!')

classes_cc = pd.DataFrame(columns=['id_turma','id_componente_curricular','codigo','nome'])

def add(csv_class_period):
	# Read class csv
	print('--> Reading file: ' + csv_class_period + '.csv')
	class_period = pd.read_csv('../raw_data/classes/' + csv_class_period + '.csv', delimiter=";", error_bad_lines=False)	
	print('--> ' + csv_class_period + '.csv read!')

	index = 0

	for _, row in class_period.iterrows():
		for i, r in (curricular_component.loc[curricular_component['id_componente'] == row['id_componente_curricular']]).iterrows():
			classes_cc.loc[index] = [row['id_turma'], r['id_componente'], r['codigo'], r['nome']]
			index += 1

def saveClassesCC():
	print('--> Saving file: classes_curricular_component.csv')
	classes_cc.to_csv('../data/classes/classes_curricular_component.csv', encoding='utf-8', index=False)
	print('--> classes_curricular_component.csv saved!')

def main():
	for i in range(2010, 2018):
		for j in range(1,3):
			if i == 2017 and j > 1:
				continue
			add( str(i)+str(j) )
	saveClassesCC()

main()
