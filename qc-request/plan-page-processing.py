import pandas as pd
import numpy as np
from datetime import datetime, timedelta

today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y%m%d")
df_preProject = pd.read_csv("processed-data/processed_KOCOWA_4.0_tc_final.csv")

df_plan_page = pd.DataFrame(columns=pd.Index([
    'project_name', 'main_category', 'scope_of_dev', 'test_case', 
    'Fire TV','Roku', 'Android TV', 'Apple TV', 
    'Web', 'Apple Mobile','Android Mobile', 
    'Smart TV', 'Vizio TV']))

plan_page_object_web = {
    0: {
        'main_category': 'Subscribe', 
        'scope_of_dev': None,
    },
    1: {
        'main_category': 'Subscribe', 
        'scope_of_dev': "Hover",
    },
    2: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Subscribed',
    },
    3: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Upgrade > Basic Monthly',
    },
    4: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Upgrade > Premium Monthly',
    },
    5: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Upgrade > Basic Annual',
    },
    6: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Promotion',
    },
    7: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Promotion > Countdown',
    },
    8: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Single Pass',
    },
    9: {
        'main_category': 'Subscribe', 
        'scope_of_dev': 'Smart TV > QR',
    },
}