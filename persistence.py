import os
from people_data import df_merged
from data_ingestion import df_promotions, df_transfers, df_transactions

def save_df_to_csv():
    directory = 'data_output'
    if not os.path.exists(directory):
        os.makedirs(directory)

    df_merged.to_csv(f'{directory}/df_merged.csv', index=False)
    df_promotions.to_csv(f'{directory}/df_promotions.csv', index=False)
    df_transfers.to_csv(f'{directory}/df_transfers.csv', index=False)
    df_transactions.to_csv(f'{directory}/df_transactions.csv', index=False)

if __name__ == "__main__":
    save_df_to_csv()
