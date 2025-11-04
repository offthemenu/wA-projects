# QC Request Form Generator - Handover Document

## Overview
This application is a Streamlit-based tool that generates standardized QC (Quality Control) request forms for Jira tickets. It reads test case data from a CSV file and allows users to select projects, components, and test scopes to automatically generate formatted QC request forms.

---

## Quick Start

### Accessing the Application
**Production URL**: https://qc-generator.streamlit.app/

The application is deployed on Streamlit Cloud and accessible via the link above.

### Running Locally (Optional)
```bash
streamlit run qc-request/qc_form_generator.py
```

The application will launch in your default web browser at `http://localhost:8501`

### Deploying to Streamlit Cloud
The app is currently deployed from a personal GitHub repository. To update the deployment:
1. Push your changes to the connected GitHub repository
2. Streamlit Cloud will automatically redeploy the app
3. Refer to Streamlit's official documentation for detailed deployment instructions

---

## Key Components

### 1. Main Application File
- **File**: `qc_form_generator.py`
- **Purpose**: Streamlit UI for generating QC request forms
- **Data Source**: Reads from `processed-data/combined_project_test_cases.csv`

### 2. Data Processing Script
- **File**: `excel_tc_processor.py`
- **Purpose**: Converts new test case files into the correct format and merges them into the combined CSV

---

## Adding New Test Cases (CRITICAL)

### Input File Requirements

Your input Excel/CSV file **MUST** contain these exact columns:

| Column Name | Korean Name | Required | Description |
|-------------|-------------|----------|-------------|
| Purpose | Purpose | Yes | Target platforms (e.g., "WEB", "MOBILE", "CONNECTED TV", "SMARTTV") |
| 대분류 | 대분류 | Yes | Main category |
| 중분류 | 중분류 | No | Sub-category (can be empty) |
| 소분류 | 소분류 | No | Component (can be empty) |
| 테스트 항목 | 테스트 항목 | Yes | Test case description |

**Additional columns** (like Section, 사전조건, 테스트 스텝, 기대결과) can exist but will be ignored.

### Purpose Column Values
The `Purpose` column determines which devices the test applies to:
- **"WEB"** → Sets Web = True
- **"MOBILE"** → Sets Android Mobile & Apple Mobile = True
- **"CONNECTED TV"** → Sets Android TV, Apple TV, Fire TV, Roku = True
- **"SMARTTV"** → Sets Smart TV & Vizio TV = True

Values are case-insensitive and can contain multiple keywords.

---

## Step-by-Step: Adding New Project Data

### Step 1: Prepare Your Input File
1. Place your Excel/CSV file in the `data/` folder
2. Ensure it has the required columns listed above
3. Example filename: `KOCOWA 4.0 Requested Test_No114_20251024_Get_Started.csv`

### Step 2: Update the Processing Script
Open `excel_tc_processor.py` and modify these lines:

```python
# Line 59: Update the input file path
project_file_path = PROJECT_DIR / "data" / f"YOUR_NEW_FILE.csv"

# Line 70: Update the project name
project_name = "Your Project Name"
```

### Step 3: Run the Processing Script
```bash
python qc-request/excel_tc_processor.py
```

This will:
1. Process your input file
2. Create a dated output file in `processed-data/` (e.g., `20251028_Your Project Name.csv`)
3. Automatically merge it into `combined_project_test_cases.csv`

### Step 4: Verify the Output
Check that `processed-data/combined_project_test_cases.csv` now contains your new project data with:
- Correct project name
- Proper device mappings (True/False values)
- Test cases grouped by scope
- All required columns present

### Step 5: Test in the Application
1. Run the Streamlit app
2. Select your new project from the dropdown
3. Verify components and test cases appear correctly

---

## Output Format (combined_project_test_cases.csv)

The processed file has these columns:
```
project_name, main_category, scope_of_dev, test_case, Fire TV, Roku,
Android TV, Apple TV, Web, Apple Mobile, Android Mobile, Smart TV, Vizio TV
```

- **project_name**: The project identifier
- **main_category**: Top-level categorization
- **scope_of_dev**: Generated from 중분류 or 소분류 (sub-category takes priority)
- **test_case**: Multiple test cases combined with newline (`\n`) separators
- **Device columns**: Boolean (True/False) indicating platform applicability

---

## Troubleshooting

### Issue: New project doesn't appear in dropdown
- **Solution**: Check that `project_name` was set correctly in the processing script
- Verify the data was actually appended to `combined_project_test_cases.csv`

### Issue: No components showing for a device
- **Solution**: Check the `Purpose` column in your input file
- Ensure device keywords are spelled correctly (case-insensitive)
- Verify the device columns have `True` values in the processed CSV

### Issue: Test cases not displaying
- **Solution**: Ensure the `테스트 항목` column is not empty in your input file
- Check for any encoding issues if using special characters

### Issue: Processing script fails
- **Solution**: Verify all required columns exist in your input file
- Check for typos in column names (Korean characters must match exactly)
- Ensure the file path is correct

---

## Supported Devices
The application supports these 9 device types:
- Android Mobile
- Apple Mobile
- Android TV
- Apple TV
- Fire TV
- Roku
- Web
- Smart TV
- Vizio TV

---

## Maintenance Notes

### File Structure
```
qc-request/
├── qc_form_generator.py          # Main Streamlit app
├── excel_tc_processor.py         # Data processing script
├── data/                          # Raw input files
└── processed-data/                # Processed CSV files
    └── combined_project_test_cases.csv  # Master data file
```

### Regular Tasks
1. **Adding new test cases**: Follow the 5-step process above
2. **Updating existing projects**: Re-run the processor with updated input files
3. **Backing up data**: Periodically backup `combined_project_test_cases.csv`

### Important Notes
- The processing script **appends** new data to the combined file (doesn't overwrite)
- Test cases with the same `project_name`, `main_category`, and `scope_of_dev` are grouped together
- Device relevancy is based on `Purpose` column keywords (see table above)

---

## Contact & Support
For questions or issues with this application, contact the PM team or refer to the code comments in `excel_tc_processor.py` and `qc_form_generator.py`.
