import pandas as pd

from fuzzy_pharma.definitions import NOMENCLATURE


def get_data_frames(nomenclature_dir, header=None):
    nomenclature_files = nomenclature_dir.glob('*')

    df = pd.DataFrame()

    for nomenclature in nomenclature_files:
        n = pd.read_excel(nomenclature, header=header)
        df = pd.concat([df, n], ignore_index=True, axis=0)

    return df


def main():
    nomenclature_df = get_data_frames(NOMENCLATURE)


if __name__ == '__main__':
    main()
