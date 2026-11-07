import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv(r"datasets\full_data\EEGDataDemographicOnly.csv")
train, test = train_test_split(data, test_size=0.2, stratify=data["main.disorder"], random_state=42)
train.to_csv(r"datasets\train\train_demographic.csv", index=False)
test.to_csv(r"datasets\test\test_demographic.csv", index=False)

data = pd.read_csv(r"datasets\full_data\EEG.machinelearing_data_BRMH.csv")
train, test = train_test_split(data, test_size=0.2, stratify=data["main.disorder"], random_state=42)
train.to_csv(r"datasets\train\train_full.csv", index=False)
test.to_csv(r"datasets\test\test_full.csv", index=False)