import pandas as pd
import os
import glob

xlsx_files = glob.glob('*.{}'.format('xlsx'))

df_concat = pd.concat([pd.read_excel(f) for f in xlsx_files ], ignore_index=True)

df_concat.to_excel(r'result.xlsx', index=False)