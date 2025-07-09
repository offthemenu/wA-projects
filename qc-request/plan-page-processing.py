import pandas as pd
import numpy as np
from datetime import datetime, timedelta

today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0).strftime("%Y%m%d")
df_preProject = pd.read_csv("processed-data/processed_KOCOWA_4.0_tc_final.csv")

plan_page_object = [
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': "Subscribe", 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Hover', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribed', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Basic Monthly', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Premium Monthly', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Basic Annual', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Countdown', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Single Pass', 'Web': True},
    {'project_name': 'Plan Page Improvement', 'main_category': 'Subscribe', 'scope_of_dev': 'Smart TV > QR', 'Web': True},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Scroll'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Selected'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Basic Monthly'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Premium Monthly'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Basic Annual'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribed'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion (Pad)'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Countdown > Date (Pad)'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Counthdown > Time (Pad)'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Premiun (Mobile)'},
    {'project_name': 'Plan Page Improvement','Apple Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Basic > Countdown > Day (Mobile)'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Scroll'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Selected'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Basic Monthly'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Premium Monthly'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Upgrade > Basic Annual'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribed'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion (Pad)'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Countdown > Date (Pad)'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Counthdown > Time (Pad)'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Premiun (Mobile)'},
    {'project_name': 'Plan Page Improvement','Android Mobile': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Basic > Countdown > Day (Mobile)'},
    {'project_name': 'Plan Page Improvement','Android TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribe'},
    {'project_name': 'Plan Page Improvement','Android TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribed'},
    {'project_name': 'Plan Page Improvement','Android TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Restore Purchase > Focused'},
    {'project_name': 'Plan Page Improvement','Android TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion'},
    {'project_name': 'Plan Page Improvement','Android TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Subscribed'},
    {'project_name': 'Plan Page Improvement','Fire TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribe'},
    {'project_name': 'Plan Page Improvement','Fire TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribed'},
    {'project_name': 'Plan Page Improvement','Fire TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Restore Purchase > Focused'},
    {'project_name': 'Plan Page Improvement','Fire TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion'},
    {'project_name': 'Plan Page Improvement','Fire TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Subscribed'},
    {'project_name': 'Plan Page Improvement','Apple TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribe'},
    {'project_name': 'Plan Page Improvement','Apple TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribed'},
    {'project_name': 'Plan Page Improvement','Apple TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Restore Purchase > Focused'},
    {'project_name': 'Plan Page Improvement','Apple TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion'},
    {'project_name': 'Plan Page Improvement','Apple TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Subscribed'},
    {'project_name': 'Plan Page Improvement','Smart TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribe'},
    {'project_name': 'Plan Page Improvement','Smart TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Subscribed'},
    {'project_name': 'Plan Page Improvement','Smart TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion'},
    {'project_name': 'Plan Page Improvement','Smart TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'Promotion > Subscribed'},
    {'project_name': 'Plan Page Improvement','Smart TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'BR'},
    {'project_name': 'Plan Page Improvement','Smart TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'BR > Scroll 1'},
    {'project_name': 'Plan Page Improvement','Smart TV': True, 'main_category': 'Subscribe', 'scope_of_dev': 'BR > Scroll 2'},
    
]

df_planPage = pd.DataFrame(plan_page_object).fillna(False).reset_index(drop=True)
df_planPage['test_case']=None

# columns = ['project_name', 'main_category', 'scope_of_dev', 'test_case', 'Fire TV','Roku', 'Android TV', 'Apple TV', 'Web', 'Apple Mobile', 'Android Mobile', 'Smart TV', 'Vizio TV']
# df_planPage['Fire TV']=False
# df_planPage['Roku']=False
# df_planPage['Android TV']=False
# df_planPage['Apple TV']=False
# df_planPage['Smart TV']=False
# df_planPage['Vizio TV']=False

df_project = pd.concat([df_preProject, df_planPage], ignore_index=True)

df_project.to_csv("processed-data/combined_project_test_cases.csv", index=False)