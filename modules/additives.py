# Function to clean and split the additives_en column
import pandas as pd 

def clean_additives(additives):
    if pd.isna(additives):
        return 'No additives'
    # Split by commas and remove leading/trailing whitespace
    return list(set([additive.strip() for additive in str(additives).split(',')]))