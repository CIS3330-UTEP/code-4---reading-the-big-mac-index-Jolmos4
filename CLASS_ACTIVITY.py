# import pandas as pd

# df = pd.read_csv('big-mac-full-index.csv')

# query = f"(iso_a3 ='NZ' or iso_a3 == 'DNK')"

# df_result = df.query(query)

# mean_dollar_price = df_result['dollar_price'].mean()

# mean_dollar_price_two_decimals = round(mean_dollar_price,2)

# print(mean_dollar_price)
# print(mean_dollar_price_two_decimals)

import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

new_query = f"(date >'2000-01-01' and date <= '2000-12-31')"

year = '2000'
country_code = 'ARG'
new_query = f"(date >'{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}')"
# #new_query = f"(date >'{year}-01-01' and date <= '{int(year)+1}-12-31' and iso_a3 == '{country_code}')" (TO ADD MORE YEARS)


df_by_date = df.query(new_query)

print(df_by_date)
# print(df)



# The row that has the minimum value of bigmac

# index_of_min_value = df['dollar_price'].idxmin()

# print(index_of_min_value)

# print(df.loc[index_of_min_value])

# print(df['dollar_price'].min())