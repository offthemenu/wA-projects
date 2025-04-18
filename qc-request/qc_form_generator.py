import streamlit as st
import pandas as pd
from datetime import date
from collections import defaultdict

# Run with: streamlit run qc-request/qc_form_generator.py

# Load test case dataset
df = pd.read_csv("qc-request/data/processed/processed_KOCOWA_4.0_tc_connectedTV.csv")

# Define available devices
available_devices = ['Android Mobile', 'Apple Mobile', 'Android TV', 'Apple TV', 'Fire TV', 'Roku', 'Web', 'Smart TV', 'Vizio TV']
available_regions = ["All Regions", "NA", "LATAM", "EU", "OCD", "BRL"]

# --- UI Components ---
st.title("QC Request Form Generator")

# 0. Project Selection
st.subheader("Project")
project_options = sorted(df.project_name.dropna().unique())
selected_project = st.selectbox("Select Project", project_options)

# 0.1 Filter by selected project
df_project = df[df.project_name == selected_project]

# 1. Basic Info
st.subheader("Basic Information")
request_date = date.today()
st.markdown(f"**Request Date:** {request_date}")
requester = st.text_input("Requester")
target_qc = st.selectbox("Target Device for QC", ["Select a device..."] + available_devices)
region = st.selectbox("Target Region", available_regions)
version = st.text_input("Version", placeholder="ex) v4.0.0_0")
task_name = st.selectbox("Task Name", sorted(df_project['project_name'].unique().tolist() + ["Other"]))
if task_name == "Other":
    task_name = st.text_input("Enter a new task name")
test_env = st.selectbox("Test Environment", ["Staging", "Production", "Live"])

# 2. Type Info
st.subheader("Type & Metadata")
qc_type = st.selectbox("Type for QC", ["New", "Bug Fix", "Routine", "Other"])
qc_round = st.selectbox("Round", list(range(1, 11)))
urgency = st.selectbox("Urgency Level", ["Normal", "Urgent"])
reference_doc = st.text_input("Reference Document (URL)", placeholder="Link to the relevant Zeplin Dashboard")

# 3. Scope of Development & Tests
st.subheader("Scope of Development")

col1, col2 = st.columns([1,1])

with col1:
    selected_scope_tree = []
    selected_tests = []

    if target_qc != "Select a device...":
        # Filter based on selected device
        df_filtered = df_project[df_project[target_qc] == True].copy()

        for main_cat in sorted(df_filtered['main_category'].unique()):
            with st.expander(main_cat):
                cat_df = df_filtered[df_filtered['main_category'] == main_cat]
                select_all = st.checkbox(
                    f"✅ Select all components",
                    key=f"{main_cat}_select"
                )

                for _, row in cat_df.iterrows():
                    comp = row['component']
                    test_cases = [tc.strip() for tc in row['test_case'].splitlines() if tc.strip()]
                    comp_key = f"{main_cat}_{comp}"

                    if select_all or st.checkbox(f"↳ {comp}", key=comp_key):
                        selected_scope_tree.append(f"{main_cat} > {comp}")
                        selected_tests.append((comp, test_cases))  # preserve grouping

grouped_tests = defaultdict(set)
for comp, test_list in selected_tests:
    grouped_tests[comp].update(test_list)

included_formatted = ""
for comp in sorted(grouped_tests):
    included_formatted += f"<b>{comp}</b><br>\n"
    for tc in sorted(grouped_tests[comp]):
        included_formatted += f"- {tc}<br>\n"

# 4. Format Scope of Development
development_scope_formatted = '<br>'.join(selected_scope_tree)

# --- Generate Output ---
with col2:
    st.markdown("### 📋 QC Request Form Preview")
    if target_qc == "Select a device...":
        st.warning("Please select a valid device to preview the request.")
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
        st.success("✅ This is your preview. Click below to finalize.")

if st.button("✅ Generate Final QC Form for Jira"):
    st.toast("You can now copy the preview above into your Jira ticket ✨")