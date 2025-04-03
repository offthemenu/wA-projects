# 🧪 QC Request Form Generator

A lightweight internal web application built with Streamlit that standardizes QA request forms across development teams.

This tool was created during the SMS and Billing Gateway system migration project to eliminate inconsistencies in how developers submitted QC requests, and to ensure clear, testable scopes were communicated to third-party QA vendors.

---

## 🚀 Features

- **Auto-filled Request Metadata**  
  Captures request date and allows easy input of requester, environment, task name, and more.

- **Region & Type Selector**  
  Easily filter the target region(s), QC type, urgency, and platform.

- **Scope of Development**  
  Choose relevant development categories (중분류) via checkboxes to generate scoped QA request items.

- **Automated Test Scope Generation**  
  Generates a list of all applicable 테스트 항목 based on selected categories.

- **HTML Table Output**  
  Generates a copy-paste friendly HTML table format ready for Jira tickets.

---

## 🛠️ How to Run the App

1. **Clone this repo:**

    ```bash
    git clone https://your-company-internal.git/qc-request-form-generator.git
    cd qc-request-form-generator
    ```

2. **Install dependencies (in a virtualenv if possible):**

    ```bash
    pip install -r requirements.txt
    ```

3. **Place the processed dataset**  
    Ensure `20250331_processed_billing_test_cases.csv` is in the same directory as the script.

4. **Run the app:**

    ```bash
    streamlit run qc_request_app.py
    ```

---

## 📋 How to Use

1. **Basic Info**
    - Fill in requester name
    - Select platform (`Android mobile`, `iOS`, or `Web`)
    - Specify version and task name
    - Choose the test environment (Staging or Production)

2. **Region & QC Type**
    - Select target region(s)
    - Choose QC type (New, Bug Fix, Routine, etc.)
    - Define test round number and urgency
    - Optionally link a design/reference document (Zeplin, Notion, etc.)

3. **Scope of Development**
    - Select relevant `중분류` items from your target region(s)
    - Test scope will be automatically generated based on these categories

4. **Generate**
    - Click **Generate QC Form**
    - An HTML table will be created, ready to paste into Jira
    - You’ll see success confirmation at the bottom

---

## 📁 Dataset Format

The app relies on a pre-processed test case CSV with the following schema:

| Column             | Description                                     |
|--------------------|-------------------------------------------------|
| Region/Category    | Region or shared feature bucket (`All Regions`) |
| 중분류              | High-level category of the feature               |
| 소분류              | Subcategory or specific component                |
| 테스트 항목         | Description of the test case                    |

This dataset is grouped internally to match test scope with selected development categories.

---

## 🔧 Troubleshooting

- **App Won’t Start?**  
  Make sure your CSV file is present and your Python environment includes `pandas` and `streamlit`.

- **No Items Showing Under Region?**  
  Confirm that `중분류` entries exist under that region in the dataset.

- **Duplicates in Tests?**  
  The app automatically deduplicates `테스트 항목`. If you notice any, ensure your dataset has normalized entries.

---

## 🧠 Design Notes

- **Why Streamlit?**  
  Fast to build, deploy, and easy to use for non-technical users

- **Why HTML Output?**  
  Jira and Confluence render HTML tables cleanly — ensuring seamless handoffs to QA teams

- **Why This Tool Exists**  
  During high-volume development sprints, inconsistently formatted QA requests created blockers. This tool enforces standardization while maintaining flexibility.

---

## 👋 Hand-off Notes

This app was built by **Yeonwoo (Ian) Chang** in March 2025.  
For long-term maintainability:

- Keep the dataset (`20250331_processed_billing_test_cases.csv`) updated as new test cases are added
- Consider connecting the app to a backend database if used across teams
- If you wish to extend features (e.g., copy-to-clipboard, Jira API integration), refer to the Streamlit [docs](https://docs.streamlit.io)

---

## 📄 License

Internal use only. Not for public distribution.
