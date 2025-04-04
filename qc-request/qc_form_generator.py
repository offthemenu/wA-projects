import streamlit as st
import pandas as pd
from datetime import date

# Run with: streamlit run qc-request/qc_form_generator.py

# Load test case dataset
df = pd.read_csv("qc-request/data/20250404_processed_test_cases.csv")

# Define available devices
available_devices = [
    'Android Mobile', 'Apple Mobile', 'Android TV', 'Apple TV',
    'Connected TV', 'Fire TV', 'Roku', 'Web'
]

available_regions = ["All Regions", "NA", "LATAM", "EU", "OCD", "BRL"]

# --- UI Components ---
st.title("🧪 QC Request Form Generator (Device-Based)")

# 1. Basic Info
st.subheader("📌 Basic Information")
request_date = date.today()
st.markdown(f"**Request Date:** {request_date}")
requester = st.text_input("Requester")
target_qc = st.selectbox("Target Device for QC", ["Select a device..."] + available_devices)
region = st.selectbox("Target Region", available_regions)
version = st.text_input("Version", placeholder="ex) v3.4.0_2")
task_name = st.selectbox("Task Name", ["New SMS Billing Gateway System"] + ["Other"])
if task_name == "Other":
    task_name = st.text_input("Enter new task name")
test_env = st.selectbox("Test Environment", ["Staging", "Production"])

# 2. Type Info
st.subheader("🧩 Type & Metadata")
qc_type = st.selectbox("Type for QC", ["New", "Bug Fix", "Routine", "Other"])
qc_round = st.selectbox("Round", list(range(1, 11)))
urgency = st.selectbox("Urgency Level", ["Normal", "Urgent"])
reference_doc = st.text_input("Reference Document (URL)")

# 3. Scope of Development & Tests
st.subheader("📦 Scope of Development")

selected_scope_tree = []
selected_tests = []

if target_qc != "Select a device...":
    df_filtered = df[df[target_qc] == True]

    for category in sorted(df_filtered['대분류'].unique()):
        cat_group = df_filtered[df_filtered['대분류'] == category]
        subcategories = sorted(cat_group['소분류'].unique())

        with st.expander(f"{category}"):
            # Select all checkbox
            select_all_key = f"select_all_{category}"
            select_all = st.checkbox("Select all", key=select_all_key)

            if len(subcategories) == 1 and subcategories[0] == category:
                if st.checkbox(f"{category} (All)", key=f"{category}_solo") or select_all:
                    selected_scope_tree.append(category)
                    selected_tests.extend(cat_group['테스트 항목'].tolist())
            else:
                for sub in subcategories:
                    sub_items = cat_group[cat_group['소분류'] == sub]['테스트 항목'].tolist()
                    if select_all or st.checkbox(f"↳ {sub}", key=f"{category}_{sub}"):
                        selected_scope_tree.append(f"{category} > {sub}")
                        selected_tests.extend(sub_items)

# Deduplicate selected 항목s directly
unique_selected = sorted(set(selected_tests))
included_formatted = '<br>'.join(unique_selected)
development_scope_formatted = '<br>'.join(selected_scope_tree)

# --- Generate Output ---
st.subheader("📋 Generated QC Request Form")
if st.button("Generate QC Form"):
    if target_qc == "Select a device...":
        st.error("Please select a valid target device before generating the form.")
    else:
        html_output = f"""
        <table>
            <tr><th>Field</th><th>Value</th></tr>
            <tr><td>Request Date</td><td>{request_date}</td></tr>
            <tr><td>Requester</td><td>{requester}</td></tr>
            <tr><td>Target Device</td><td>{target_qc}</td></tr>
            <tr><td>Region</td><td>{region}</td></tr>
            <tr><td>Version</td><td>{version}</td></tr>
            <tr><td>Task Name</td><td>{task_name}</td></tr>
            <tr><td>Test Environment</td><td>{test_env}</td></tr>
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
