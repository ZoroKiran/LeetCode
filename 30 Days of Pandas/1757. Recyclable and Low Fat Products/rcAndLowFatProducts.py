import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    rc_low_fat_products_df = products[(products['low_fats'] == 'Y') | (products['recyclable'] == 'Y')];
    result = rc_low_fat_products_df[['product_id']];
    return result;