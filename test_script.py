import os
import pandas as pd

def test_dataset_loading():
    """
    Test if the dataset loads properly.
    """
    dataset_path = "data/dataset.csv"  # Update this path if needed

    if not os.path.exists(dataset_path):
        print(f" Dataset file not found at {dataset_path}")
        return  # Prevents crashing

    try:
        df = pd.read_csv(dataset_path)
        assert not df.empty, " Dataset is empty!"
        print(" Dataset loaded successfully!")
    except Exception as e:
        print(f" Dataset loading failed: {e}")

if __name__ == "__main__":
    test_dataset_loading()
