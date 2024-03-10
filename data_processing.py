import pandas as pd
import yaml

def load_json(json_path):
    """
    Loads and normalizes JSON data to a pandas DataFrame.
    
    This function reads the JSON file, normalizes nested JSON structures (if any),
    and renames columns to create a consistent schema with the YAML data.
    """
    df = pd.read_json(json_path)
    df = pd.json_normalize(df['people'])
    df.rename(columns={
        'surname': 'lastName', 'telephone': 'phone',
        'location.city': 'city', 'location.country': 'country'
    }, inplace=True)

    # Standardize the 'id' format using a lambda function to remove leading zeros
    df['id'] = df['id'].apply(lambda x: int(x.lstrip('0')))
    return df

def load_yaml(yaml_path):
    """
    Loads and normalizes YAML data to a pandas DataFrame.
    
    This function reads the YAML file, converts it to a DataFrame, and processes
    it to match the schema of the JSON data. It includes splitting 'city' into separate
    city and country columns and converting boolean device indicators into a list.
    """
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)['people']
    df = pd.DataFrame(data)

    # Extracts city and country from a single string
    df['devices'] = df.apply(lambda x: [device for device in ['iPhone', 'Android', 'Desktop'] if x.get(device, False)], axis=1)
    df[['city', 'country']] = df['city'].str.split(', ', expand=True)
    df.drop(columns=['iPhone', 'Android', 'Desktop', 'name'], inplace=True, errors='ignore')
    return df

def merge_dataframes(df1, df2):
    """Merges two DataFrames into one, maintaining a consistent schema.
    
    The merge ignores the original indexes to ensure a continuous index in the merged DataFrame.
    """
    return pd.concat([df1, df2], ignore_index=True)

# Example usage to demonstrate how to load, normalize, and merge the data
json_path = 'data/people.json'
yaml_path = 'data/people.yml'

# Load and normalize data from JSON and YAML files
df_json = load_json(json_path)
df_yaml = load_yaml(yaml_path)

# Merge the normalized DataFrames
df_merged = merge_dataframes(df_json, df_yaml)

# Display the first few rows of the merged DataFrame
print(df_merged.head())
