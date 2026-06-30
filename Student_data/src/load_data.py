import pandas as pd

def load_dataset(file_path):

    data = pd.read_csv(file_path)

    print("\nFirst 5 Records:")
    print(data.head())

    print("\nLast 5 Records:")
    print(data.tail())

    print("\nDataset Shape:")
    print(data.shape)

    print("\nColumn Names:")
    print(data.columns)

    print("\nData Types:")
    print(data.dtypes)

    return data