import streamlit as st
import pandas as pd
from datetime import date

# Run streamlit run qc-request/qc_form_generator.py 

# Load test case dataset
df = pd.read_csv("qc-request/data/20250331_processed_billing_test_cases.csv")

# Preprocess dataset
all_regions = ['US', 'Argentina', 'United Kingdom', 'Australia', 'Brazil', 'Spain']
non_region_categories = df[~df['Region/Category'].isin(all_regions)]['Region/Category'].unique().tolist()

# Group data for checkbox hierarchy
grouped = df.groupby(['Region/Category', '중분류', '소분류'])['테스트 항목'].unique().reset_index()

# --- UI Components ---
st.title("🧪 QC Request Form Generator (Deployed Version)")

# 1. Basic Info
st.subheader("📌 Basic Information")
request_date = date.today()
st.markdown(f"**Request Date:** {request_date}")
requester = st.text_input("Requester")
target_qc = st.selectbox("Target for QC", ["Web", "Android Mobile", "Android TV", "iOS", "tvOS", "Roku", "Fire TV", "Smart TV", "Vizio"])
version = st.text_input("Version", placeholder="ex) v3.4.0_2")
task_name = st.selectbox("Task Name", ["New SMS Billing Gateway System"] + ["Other"])
if task_name == "Other":
    task_name = st.text_input("Enter new task name")
test_env = st.selectbox("Test Environment", ["Staging", "Production"])

# 2. Region + Type Info
st.subheader("🌍 Region & QC Type")
region_options = all_regions
selected_regions = st.multiselect("Region(s)", region_options, placeholder="Skip for Non-Regional Scopes")
if "All Regions" in selected_regions:
    selected_regions = all_regions  # override with all regions
qc_type = st.selectbox("Type for QC", ["New", "Bug Fix", "Routine", "Other"])
qc_round = st.selectbox("Round", list(range(1, 11)))
urgency = st.selectbox("Urgency Level", ["Normal", "Urgent"])
reference_doc = st.text_input("Reference Document (URL)")

# 3. Scope of Development & Tests
st.subheader("🧩 Scope of Development")
selected_scope = []
selected_scope_tree = []

for region in selected_regions + non_region_categories:
    region_group = grouped[grouped['Region/Category'] == region]
    st.markdown(f"**{region}**")
    for mid_cat in region_group['중분류'].unique():
        if st.checkbox(f"{mid_cat}", key=f"{region}_{mid_cat}_solo"):
            selected_scope_tree.append(f"{mid_cat} ({region})")
            matched_rows = region_group[region_group['중분류'] == mid_cat]
            for 항목_list in matched_rows['테스트 항목']:
                selected_scope.extend(항목_list)

# Deduplicate selected 항목s directly
unique_selected = sorted(set(selected_scope))
included_formatted = '<br>'.join(unique_selected)
development_scope_formatted = '<br>'.join(selected_scope_tree)

# --- Generate Output ---
st.subheader("📋 Generated QC Request Form")
if st.button("Generate QC Form"):
    html_output = f"""
    <table>
        <tr><th>Field</th><th>Value</th></tr>
        <tr><td>Request Date</td><td>{request_date}</td></tr>
        <tr><td>Requester</td><td>{requester}</td></tr>
        <tr><td>Target for QC</td><td>{target_qc}</td></tr>
        <tr><td>Version</td><td>{version}</td></tr>
        <tr><td>Task Name</td><td>{task_name}</td></tr>
        <tr><td>Test Environment</td><td>{test_env}</td></tr>
        <tr><td>Region</td><td>{', '.join(selected_regions)}</td></tr>
        <tr><td>Type for QC</td><td>{qc_type} Round {qc_round}</td></tr>
        <tr><td>Urgency Level</td><td>{urgency}</td></tr>
        <tr><td>Reference Document</td><td>{reference_doc}</td></tr>
        <tr><td>Scope of Development</td><td>{development_scope_formatted}</td></tr>
        <tr><td>Included in Tests</td><td>{included_formatted}</td></tr>
        <tr><td>Excluded from Tests</td><td>**해당사항 기입해주시기를 바랍니다.**</td></tr>
    </table>
    """
    st.markdown(html_output, unsafe_allow_html=True)
    st.success("✅ QC Request Form Generated! Copy it to your Jira ticket.")