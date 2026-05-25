"""Data loading utilities for player data analysis."""

import pandas as pd
import os
from pathlib import Path


def load_player_data(filepath):
    """
    Load player data from CSV file.
    
    Parameters:
    -----------
    filepath : str
        Path to the CSV file
        
    Returns:
    --------
    pd.DataFrame
        Player data dataframe
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Data file not found: {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"Loaded {len(df)} player records from {filepath}")
    return df


def load_all_data(data_dir='data'):
    """
    Load all CSV files from data directory.
    
    Parameters:
    -----------
    data_dir : str
        Directory containing CSV files
        
    Returns:
    --------
    pd.DataFrame
        Combined player data from all CSV files
    """
    data_files = list(Path(data_dir).glob('*.csv'))
    
    if not data_files:
        print(f"No CSV files found in {data_dir}")
        return None
    
    dfs = []
    for file in data_files:
        try:
            df = load_player_data(str(file))
            dfs.append(df)
        except Exception as e:
            print(f"Error loading {file}: {e}")
    
    if dfs:
        combined_df = pd.concat(dfs, ignore_index=True)
        return combined_df
    return None


def clean_data(df):
    """
    Clean and validate player data.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Raw player data
        
    Returns:
    --------
    pd.DataFrame
        Cleaned player data
    """
    df = df.copy()
    
    # Remove duplicates
    df = df.drop_duplicates(subset=['player_id'], keep='last')
    
    # Fill missing values
    numeric_cols = df.select_dtypes(include=['number']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    
    # Convert date columns
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass
    
    print(f"Data cleaned: {len(df)} records")
    return df
