import pandas as pd
import yaml

def load_promotions(csv_path):
    return pd.read_csv(csv_path)

def load_transfers(csv_path):
    return pd.read_csv(csv_path)

def load_transactions(xml_path):
    return pd.read_xml(xml_path, xpath='./transaction')

# Data paths
df_promotions = load_promotions('data/promotions.csv')
df_transfers = load_transfers('data/transfers.csv')
df_transactions = load_transactions('data/transactions.xml')

# print(df_promotions.head())
# print(df_transfers.head())
# print(df_transactions.head())
