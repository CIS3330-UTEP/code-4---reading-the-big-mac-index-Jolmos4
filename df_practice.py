import pandas as pd

filename = "big-mac-full-index.csv"

df = pd.read_csv(filename)


# print(df['dollar_price'])
# print(df['name'])


query = f"(iso_a3 == 'ARG')"
arg_df = df.query(query)

# print(arg_df)

# arg_df.to_csv('argenitna_report.csv')

print(arg_df['dollar_price'].median())
