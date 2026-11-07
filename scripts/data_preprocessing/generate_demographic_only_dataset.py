import pandas as pd
'''
The full dataset is slow to work with 
'''


data = pd.read_csv('datasets\EEG.machinelearing_data_BRMH.csv')
COLS_TO_KEEP = 8
demographic_only = data.iloc[:, :COLS_TO_KEEP]
demographic_only.to_csv(r'EEGDataDemographicOnly.csv', index = False)

