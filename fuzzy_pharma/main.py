import pandas as pd

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


def main():
    nomenclature_df = get_data_frames(NOMENCLATURE)
    clients_df = get_client_data_frames(CLIENTS, ['наименование'])


if __name__ == '__main__':
    main()
