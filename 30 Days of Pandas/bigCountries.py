import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    # Filter the DataFrame based on the conditions for being a big country
    big_countries_df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    
    # Select only the required columns
    result = big_countries_df[['name', 'population', 'area']]
    
    return result

# Example usage
data = {'name': ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola'],
        'continent': ['Asia', 'Europe', 'Africa', 'Europe', 'Africa'],
        'area': [652230, 28748, 2381741, 468, 1246700],
        'population': [25500100, 2831741, 37100000, 78115, 20609294],
        'gdp': [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]}

world_df = pd.DataFrame(data)

result_df = big_countries(world_df)
print(result_df)    