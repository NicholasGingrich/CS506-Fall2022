import pandas as pd

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    mat = pd.read_csv()

    mat = pd.pivot_table(mat)

    return mat
