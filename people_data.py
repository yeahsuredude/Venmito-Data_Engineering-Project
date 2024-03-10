import pandas as pd
import yaml

def load_json(json_path):
    df = pd.read_json(json_path)
    df = pd.json_normalize(df['people'])

    # Renaming columns to match yaml file
    df.rename(columns={
        'surname': 'lastName', 'telephone': 'phone',
        'location.city': 'city', 'location.country': 'country'
    }, inplace=True)

    # Standardize the 'id' format using a lambda function to remove leading zeros
    df['id'] = df['id'].apply(lambda x: int(x.lstrip('0')))
    return df

def load_yaml(yaml_path):
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)['people']
    df = pd.DataFrame(data)

    # Split 'name' into 'firstName' and 'lastName'
    df[['firstName', 'lastName']] = df['name'].str.split(' ', expand=True, n=1)
    df.drop(['name'], axis=1, inplace=True)

    # Extracts devices from boolean values and city and country from a single string
    df['devices'] = df.apply(lambda x: [device for device in ['iPhone', 'Android', 'Desktop'] if x.get(device, False)], axis=1)
    df[['city', 'country']] = df['city'].str.split(', ', expand=True)

    # Drop unneeded last columns from df
    df.drop(columns=['iPhone', 'Android', 'Desktop', 'name'], inplace=True, errors='ignore')
    return df

def merge_dataframes(df1, df2):

    # Combine the dataframes
    combined_df = pd.concat([df1, df2], ignore_index=True)

    # Remove duplicates based on 'id' while keeping the first occurrence
    combined_df.drop_duplicates(subset='id', keep='first', inplace=True)

    # Sort by 'id' for easier readability and analysis
    combined_df.sort_values(by='id', inplace=True)

    # Reset index after sorting
    combined_df.reset_index(drop=True, inplace=True)

    return combined_df

# Data paths
json_path = 'data/people.json'
yaml_path = 'data/people.yml'

# Load and normalize data from JSON and YAML files
df_json = load_json(json_path)
df_yaml = load_yaml(yaml_path)

# Merge the normalized DataFrames
df_merged = merge_dataframes(df_json, df_yaml)

# Testing merged DataFrame
# print(df_merged.info())
