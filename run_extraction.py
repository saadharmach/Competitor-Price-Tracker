# run_extraction.py
from config import STORES
from src.extractor import fetch_all_products
from src.processor import flatten_products

all_records = []

for store in STORES:
    print(f"Fetching {store['store_name']}...")
    raw_products = fetch_all_products(store['domain'])
    flat_products = flatten_products(raw_products, store['store_name'])

    all_records.extend(flat_products)
    print(f"  - {len(flat_products)} records contributed")

print(f"Total records collected: {len(all_records)}")
import pandas as pd

df = pd.DataFrame(all_records)
print(df.info())
print(df.head())
missing_sku_products = df[(df["store"] == "Bells of Steel") & (df["sku"].isna())]
print(missing_sku_products["product_title"].value_counts())