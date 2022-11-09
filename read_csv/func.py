import pandas as pd


def read(path):
    try:
        if path[-4:] == 'xslx':
            excel = pd.read_excel(path)
        elif path[-3:] == 'csv':
            csv = pd.read_csv(path)
        else:
            return 'Incorrect type of data'

    except FileNotFoundError as fnf_ex:
        return 'File not found'

    except IndexError as i_ex:
        return 'Incorrect type of data'

    return f'{path} readed'

