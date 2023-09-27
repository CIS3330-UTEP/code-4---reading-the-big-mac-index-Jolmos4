import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)
print(df.columns)

def get_big_mac_price_by_year(year, country_code):
    country_code = country_code.upper()
    df_by_date = df[df['date'].str.startswith(str(year)) & (df['iso_a3']== country_code)]
    # new_query = f"(date > '{year}-04-01' & iso_a3 == '{country_code}')"
    mean_dollar_price = round(df_by_date['dollar_price'].mean(), 2)
    return mean_dollar_price

def get_big_mac_price_by_country(country_code):
    country_code = country_code.upper()
    df_by_country = df[df['iso_a3']== country_code]
    return round(df_by_country['dollar_price'].mean(), 2)

def get_the_cheapest_big_mac_price_by_year(year):
    new_query = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"
    df_by_year = df.query(new_query)
    index_of_min_value = df['dollar_price'].idxmin()

    print(index_of_min_value)

    print(df.loc[index_of_min_value])

    print(df['dollar_price'].min())

    print(df_by_year)

    return(index_of_min_value)

def get_the_most_expensive_big_mac_price_by_year(year):
    new_query = f"(date >= '{year}-01-01' & date <= '{year}-12-31')"
    df_by_year = df.query(new_query)
    index_of_max_value = df['dollar_price'].idxmax()

    print(index_of_max_value)

    print(df.loc[index_of_max_value])

    print(df['dollar_price'].max())
    
    print(df_by_year)

    return(index_of_max_value)

if __name__ == "__main__":
    year = '2000'
    country_code = 'arg'  

    mean_price_by_year = get_big_mac_price_by_year(year, country_code)
    print(f"Mean Dollar Price for {country_code.upper()} in {year}: ${mean_price_by_year}")

    mean_price_country = get_big_mac_price_by_country(country_code)
    print(f"Overall Mean Dollar Price for {country_code.upper()}: ${mean_price_country}")

    Cheapest_result = get_the_cheapest_big_mac_price_by_year(year)
    print(f"Most Cheapest Price in Big Mac in {year}: {Cheapest_result}")

    expensive_result = get_the_most_expensive_big_mac_price_by_year(year)
    print(f"Most Expensive Price in Big Mac in {year}: {expensive_result}")