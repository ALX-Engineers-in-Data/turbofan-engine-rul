import pandas as pd
import os

def load_cmapss_subset(dataset_name, subset="train"):
    """
    Load CMAPSS dataset subset.
    dataset_name: e.g., 'FD001'
    subset: 'train' or 'test'
    """
    # Construct path assuming data is in data/raw/
    base_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
    file_name = f"{dataset_name}_{subset}.txt"
    file_path = os.path.join(base_path, file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} not found. Make sure CMAPSS data is downloaded.")

    # Load the data
    df = pd.read_csv(file_path, sep="\s+", header=None)
    return df
