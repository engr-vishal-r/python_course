import pandas as pd
from pathlib import Path
import numpy as np
from multiprocessing import Pool

input_path = Path(r"F:\python_tutorial\pandas\hire_summary.csv")
output_path = input_path.parent / f"{input_path.stem}_output_hire.csv"

chunksize = 1000

def process_chunk(chunk):
    chunk['level'] = np.where(
        chunk["days_between_hires"] >= 400,
        "Senior",
        "Junior"
    )
    return chunk

if __name__ == "__main__":

    with Pool(4) as p:   # start with 4, not 16
        for processed_chunk in p.imap(process_chunk, pd.read_csv(input_path, chunksize=chunksize)):

            print(processed_chunk)