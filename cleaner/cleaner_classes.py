import pandas as pd 
import numpy as np

def remove_not_approved(csv_class_period):
	# Read class csv
	print('--> Reading file: ' + csv_class_period + '.csv')
	class_period = pd.read_csv('../raw_data/classes/' + csv_class_period + '.csv', delimiter=";")	
	print('--> ' + csv_class_period + '.csv read!')
	class_period = class_period[class_period.descricao.str.contains('APROVADO') == True]
	print('--> Saving file: ' + csv_class_period + '.csv')
	pd.DataFrame(class_period).to_csv('../data/classes/' + csv_class_period + '.csv', encoding='utf-8', index=False)
	print('--> ' + csv_class_period + '.csv saved!')

def main():
	for i in range(2010, 2018):
		for j in range(1,3):
			if i == 2017 and j > 1:
				continue
			remove_not_approved( str(i)+str(j) )

main()