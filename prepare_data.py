"""Cleans the Kaggle Superstore CSV with pandas and writes data.js for the dashboard."""
import json
import sys
import pandas as pd

RAW = "data/superstore.csv"
OUT = "data.js"

# Column names in the Kaggle file  ->  names the dashboard uses
COLUMNS = {
    "Order ID": "order_id",
    "Order Date": "order_date",
    "Region": "region",
    "Category": "category",
    "Quantity": "quantity",
    "Sales": "revenue",
}

# 1. load the file (some Kaggle CSVs are not UTF-8, so we retry with latin-1)
try:
    df = pd.read_csv(RAW)
except UnicodeDecodeError:
    df = pd.read_csv(RAW, encoding="latin-1")
except FileNotFoundError:
    sys.exit(f"Could not find {RAW}. Put the Kaggle CSV in the data folder and name it superstore.csv")
print(f"Loaded {len(df)} rows")

# 2. make sure the columns we need exist
missing = [c for c in COLUMNS if c not in df.columns]
if missing:
    print("These columns were not found:", missing)
    print("Columns in your file:", list(df.columns))
    sys.exit("Edit the COLUMNS dictionary at the top of this file to match your column names.")
df = df[list(COLUMNS)].rename(columns=COLUMNS)

# 3. remove exact duplicate rows
before = len(df)
df = df.drop_duplicates()
print(f"Removed {before - len(df)} duplicate rows")

# 4. fix text, dates and numbers
df["region"] = df["region"].astype(str).str.strip().str.title()
df["category"] = df["category"].astype(str).str.strip().str.title()
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

# 5. drop rows we cannot use
before = len(df)
df = df.dropna(subset=["order_date", "revenue", "quantity"])
print(f"Dropped {before - len(df)} rows with missing values")

# 6. new columns used by the dashboard
df["revenue"] = df["revenue"].round(2)
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.strftime("%Y-%m")

out = df[["order_id", "month", "year", "region", "category", "quantity", "revenue"]]
print(f"Years found: {out['year'].min()} to {out['year'].max()}")
with open(OUT, "w", encoding="utf-8") as f:
    f.write("const DATA = " + json.dumps(out.to_dict(orient="records")) + ";\n")
print(f"Wrote {len(out)} clean rows to {OUT}")
