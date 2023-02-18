import logging

import pandas as pd
from fuzzywuzzy import fuzz

from fuzzy_pharma.definitions import NOMENCLATURE, CLIENTS


def get_data_frames(nomenclature_dir, header=None):
    nomenclature_files = nomenclature_dir.glob('*')

    df = pd.DataFrame()

    for nomenclature in nomenclature_files:
        n = pd.read_excel(nomenclature, header=header)
        df = pd.concat([df, n], ignore_index=True, axis=0)

    return df


def get_client_data_frames(client_dir, usecols, header=0):
    client_files = client_dir.glob('*')

    df = pd.DataFrame()

    for client in client_files:
        c = pd.read_excel(client, header=header, usecols=usecols)
        df = pd.concat([df, c], ignore_index=True, axis=0)

    return df


def get_nomenclature_name(client_name, nomenclature_names):
    try:
        rating = 0
        sku = ''
        nomenclature_name = ''
        for dct in nomenclature_names:
            measure = fuzz.token_sort_ratio(
                dct['nomenclature_name'].lower().strip(),
                client_name.lower().strip()
            )
            if measure > rating and measure != rating:
                rating = measure
                sku = dct['sku']
                nomenclature_name = dct['nomenclature_name']
        return sku, nomenclature_name, client_name, rating
    except Exception as e:
        logging.exception(e)
        return None, None, None, 0


def main():
    nomenclature_df = get_data_frames(NOMENCLATURE)
    clients_df = get_client_data_frames(CLIENTS, ['наименование'])

    nomenclature_names = []

    for row in nomenclature_df.itertuples():
        nomenclature_names.append({
            'sku': row[1],
            'nomenclature_name': row[2],
        })

    out_tuples = []

    for row in clients_df.itertuples():
        out_tuple = get_nomenclature_name(row[1], nomenclature_names)
        out_tuples.append(out_tuple)


if __name__ == '__main__':
    main()
