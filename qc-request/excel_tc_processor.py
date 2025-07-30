import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
PROJECT_DIR = ROOT_DIR / "qc-request"

today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y%m%d")
plan_file_path = PROJECT_DIR / "data" / f"KOCOWA 4.0 Requested Test_No116_20250709.csv"
card_file_path = PROJECT_DIR / "data" / f"KOCOWA 4.0 Requested Test_No119_20250730.xlsx - Request119.csv"
combined_file_path = PROJECT_DIR / "processed-data" / f"combined_project_test_cases.csv"

# Define available devices
available_devices = [
    'Android Mobile', 'Apple Mobile', 'Android TV', 'Apple TV', 
    'Fire TV', 'Smart TV', 'Vizio TV', 'Roku', 'Web'
]

# Map out column rename rules
rename_rules = {
    "대분류": "main_category",
    "중분류": "sub_category",
    "소분류": "component",
    "Section": "scenario",
    "테스트 항목": "test_case"
}

df_project = pd.read_csv(combined_file_path)
df_new = pd.read_csv(card_file_path)[['Purpose', '대분류', '중분류', '소분류', '테스트 항목']].fillna("")
df_new.rename(columns=rename_rules, inplace=True)  # type: ignore
project_name = "Card Management"

df_new["project_name"] = project_name
df_new["Web"] = False
df_new["Apple Mobile"] = False
df_new["Android Mobile"] = False
df_new["Apple TV"] = False
df_new["Android TV"] = False
df_new["Fire TV"] = False
df_new["Roku"] = False
df_new["Smart TV"] = False
df_new["Vizio TV"] = False

# Strip whitespace from category columns
for col in ["main_category", "sub_category", "component"]:
    df_new[col] = df_new[col].astype(str).str.strip()  # type: ignore

# Generate "scope_of_dev" column
def generate_scope_of_dev(main: str, sub: str, comp: str) -> str: # type: ignore
    if comp == "":
        if sub == "":
            return "General Rules"
        else:
            return sub
    else:
        if sub != "":
            return sub

# Generate "scope_of_dev" column
df_new["scope_of_dev"] = df_new.apply(lambda row: generate_scope_of_dev(row["main_category"], row["sub_category"], row["component"]), axis=1)

# Generate device relevancy
def device_relevancy(purpose: str, df: pd.DataFrame, idx: int):
    # If the purpose contains 'WEB', set the 'Web' column to True for the given row
    if "web" in purpose.lower():
        df.at[idx, "Web"] = True
    if "mobile" in purpose.lower():
        df.at[idx, "Android Mobile"] = True
        df.at[idx, "Apple Mobile"] = True
    if "connected tv" in purpose.lower():
        df.at[idx, "Android TV"] = True
        df.at[idx, "Apple TV"] = True
        df.at[idx, "Fire TV"] = True
        df.at[idx, "Roku"] = True
    if "smarttv" in purpose.lower():
        df.at[idx, "Smart TV"] = True
        df.at[idx, "Vizio TV"] = True

# Set device relevancy
for idx, row in df_new.iterrows():
    device_relevancy(row["Purpose"], df_new, idx) # type: ignore

# Group by scope of dev and combine test cases with \n
df_new = df_new.groupby(['project_name', 'main_category', 'scope_of_dev']).agg({
    'test_case': lambda x: '\n'.join(x),
    'Fire TV': 'max',
    'Roku': 'max',
    'Android TV': 'max',
    'Apple TV': 'max',
    'Web': 'max',
    'Apple Mobile': 'max',
    'Android Mobile': 'max',
    'Smart TV': 'max',
    'Vizio TV': 'max'
}).reset_index()

col_orders = ['project_name', 'main_category', 'scope_of_dev', 'test_case', 'Fire TV', 'Roku', 'Android TV', 'Apple TV', 'Web', 'Apple Mobile', 'Android Mobile', 'Smart TV', 'Vizio TV']
df_new = df_new[col_orders]

df_new.to_csv(PROJECT_DIR / "processed-data" / f"{today}_{project_name}.csv", index=False) # type: ignore

# combine the new test cases with the old test cases
df_new = pd.concat([df_project, df_new]).sort_values(by=['project_name'], ascending=False) # type: ignore

df_new.to_csv(PROJECT_DIR / "processed-data" / f"combined_project_test_cases.csv", index=False) # type: ignore
