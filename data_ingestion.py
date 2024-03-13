import pandas as pd

def load_and_prep_promotions(csv_path):
    df_promotions = pd.read_csv(csv_path)

    # Cleaning the telephone column
    df_promotions['telephone'] = df_promotions['telephone'].replace("''", pd.NA)

    # Rename client_email to email for direct merging
    df_promotions.rename(columns={'client_email': 'email'}, inplace=True)
    return df_promotions


def load_and_prep_transfers(csv_path):
    df_transfers = pd.read_csv(csv_path)

    # Convert date to datetime format for easier handling
    df_transfers['date'] = pd.to_datetime(df_transfers['date'])
    return df_transfers

def load_and_prep_transactions(xml_path):
    df_transactions = pd.read_xml(xml_path, xpath='./transaction')
    df_transactions['transactionDate'] = pd.to_datetime(df_transactions['transactionDate'])

    # Rename transactionDate to date
    df_transactions.rename(columns={'transactionDate': 'date'}, inplace=True)

    # Split buyer_name at the period, then strip to remove leading/trailing spaces
    df_transactions[['firstName', 'lastName']] = df_transactions['buyer_name'].str.split('.', n=1, expand=True)
    df_transactions['firstName'] = df_transactions['firstName'].str.strip()
    df_transactions['lastName'] = df_transactions['lastName'].str.strip()

    # Drop the original buyer_name column
    df_transactions.drop(columns=['buyer_name'], inplace=True)

    # Reorder columns to have firstName and lastName between id and item
    cols = ['id', 'firstName', 'lastName'] + [col for col in df_transactions.columns if col not in ['id', 'firstName', 'lastName']]
    df_transactions = df_transactions[cols]
    return df_transactions

# Data paths
df_promotions = load_and_prep_promotions('data/promotions.csv')
df_transfers = load_and_prep_transfers('data/transfers.csv')
df_transactions = load_and_prep_transactions('data/transactions.xml')

#print(df_promotions.head())
#print(df_transfers.head())
#print(df_transactions.head())
