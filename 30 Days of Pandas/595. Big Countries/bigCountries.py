import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame based on the conditions for being a big country
    big_countries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Select only the required columns
    result = big_countries_df[['name', 'population', 'area']]
    
    return result