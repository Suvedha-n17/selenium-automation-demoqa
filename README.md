# Automation Framework (Python + Selenium + Behave)
Automation of DEMOQA site testing using Selenium and Page Object Model.

---

### 🛠️ Used technologies
- **Language:** Python 3.8+
- **Automation:** Selenium WebDriver
- **BDD:** Behave
- **Reporting:** Allure
- **Logging:** Python's built-in `logging` module

---

## 📁 Project Structure
```
/demoqa_automation
├── features/              # Main project directory
│   ├── steps/             # Step definitions for Behave
│   │   ├── base_steps.py  
│   │   ├── book_store_steps.py  
│   │   ├── checkbox_steps.py  
│   │   ├── dynamic_properties_steps.py  
│   │   ├── forms_steps.py  
│   ├── book_store.feature  
│   ├── checkbox.feature    
│   ├── dynamic_properties.feature  
│   ├── forms.feature       
│   ├── environment.py   # Consists of hooks for Behave
├── pages  # Page Object Model (POM) implementation
│   ├── base_page.py        # Common methods for all pages
│   ├── book_store_page.py  
│   ├── checkbox_page.py    
│   ├── dynamic_properties_page.py   
│   ├── forms_page.py    
├── utils   # Utility modules and helper functions
│   ├── logger.py           # Custom logging utility
├── logs   
│   ├── test.log  # Captures test execution logs
├── allure-results/  # Allure results folder
├── allure-report/   # Allure report folder
├── .gitignore           # Git ignore file
├── requirements.txt  # List of dependencies
├── README.md          
└── ├── result_demoqa.PNG # Execution report
```

## ⚙️ Getting Started
# Clone repository
git clone https://github.com/Suvedha-n17/selenium-automation-demoqa.git
# Install virtual environment
python -m venv venv
# Activate virtual environment
source venv/bin/activate  
# Install dependencies
pip install -r requirements.txt
```
```
### ⚙️ Execution Steps
### 📄To run all feature file- From the project root:
 behave 
 
### 📄To run specific feature file
 behave features/forms.feature"
 behave features/checkbox.feature"
 behave features/dynamic_properties.feature"
 behave features/book_store.feature"
```
```
### 📊 Viewing reports
Install [Allure](https://allurereport.org/docs/#_get_started) from the official website

Execute the following command to generate allure report.
### To run tests with Allure formatter
behave -f allure_behave.formatter:AllureFormatter -o allure-results

### Generate report
allure generate allure-results -o allure-report --clean

### Open report
allure open allure-report
```
```
### Allure execution report
View [Allure test results] (https://github.com/Suvedha-n17/selenium-automation-demoqa/blob/master/result_demoqa.png)

