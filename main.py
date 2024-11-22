import sys

import pandas as pd
from functools import partial

from pandas import DataFrame

EXCEL_INPUT_PATH = "Input.xlsx"
EXCEL_OUTPUT_PATH = "Output.xlsx"

print_err = partial(print, file=sys.stderr)

def main():
    try:
        df: DataFrame = pd.read_excel(EXCEL_INPUT_PATH)
    except PermissionError:
        print_err("ERROR: The excel file is open. Please close the file and restart the program")
        exit(-1)









if __name__ == '__main__':
    main()