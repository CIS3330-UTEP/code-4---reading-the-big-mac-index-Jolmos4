import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    country_code = country_code.upper()
    new_query = f"(date > '{year}-04-01' & iso_a3 == '{country_code}')"
    df_by_date = df.query(new_query)
    mean_dollar_price = round(df_by_date['dollar_price'].mean(), 2)
    return mean_dollar_price

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    query = f"(iso_a3 == '{country_code}')"
    df_by_country = df.query(query)
    return round(df_by_country['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    new_query = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"
    df_by_year = df.query(new_query)
    cheapest_price = df_by_year['dollar_price'].min()
    cheapest_row = df_by_year[df_by_year['dollar_price'] == cheapest_price].iloc[0]
    cheapest_country_name = cheapest_row['country_name']
    cheapest_country_code = cheapest_row['iso_a3']
    return f"{cheapest_country_name}({cheapest_country_code}): ${cheapest_price}"

def get_the_most_expensive_big_mac_price_by_year(year):
    new_query = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"
    df_by_year = df.query(new_query)
    expensive_price = df_by_year['dollar_price'].max()
    expensive_row = df_by_year[df_by_year['dollar_price'] == expensive_price].iloc[0]
    expensive_country_name = expensive_row['country_name']
    expensive_country_code = expensive_row['iso_a3']
    return f"{expensive_country_name}({expensive_country_code}): ${expensive_price}"

if __name__ == "__main__":
    year = '2000'
    country_code = 'arg'  # Testing with lowercase as per instructions

    mean_price_by_year = get_big_mac_price_by_year(year, country_code)
    print(f"Mean Dollar Price for {country_code.upper()} in {year}: ${mean_price_by_year}")

    mean_price_country = get_big_mac_price_by_country(country_code)
    print(f"Overall Mean Dollar Price for {country_code.upper()}: ${mean_price_country}")

    cheapest_result = get_the_cheapest_big_mac_price_by_year(year)
    print(f"Cheapest Big Mac in {year}: {cheapest_result}")

    expensive_result = get_the_most_expensive_big_mac_price_by_year(year)
    print(f"Most Expensive Big Mac in {year}: {expensive_result}")