import pandas as pd 
import numpy as np

# Read loans csv
loans = pd.read_csv('../raw_data/library/loans.csv', delimiter=";")

# Removing null discentes
loans = loans[pd.notnull(loans['discente'])]

# Removing all loans befere 2010
for i in range(2003,2010):
	loans = loans[loans.data_emprestimo.str.contains(str(i)) == False]

# Sorting data by date
loans = loans.sort_values(by=['data_emprestimo'])

pd.DataFrame(loans).to_csv('../data/library/loans.csv', encoding='utf-8', index=False)