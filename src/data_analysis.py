import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)

df = pd.read_csv('../data/survey_results_public.csv')
schema_df = pd.read_csv('../data/survey_results_schema.csv')


