# Selenium Automation DEMOQA
Automation of [DEMOQA](https://demoqa.com/) site testing using Selenium and Page Object Model

## Used technologies
<p  align="center">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/pycharm/pycharm-original.svg" title="PyCharm" alt="PyCharm">
  <img width="5%" src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" title="Python" alt="Python">
  <img width="5%" src="https://avatars0.githubusercontent.com/u/983927?v=3&s=400" title="Selenium" alt="Selenium">
  <img width="5%" src="https://biercoff.com/content/images/2017/08/allure-logo.png" title="Allure Report" alt="Allure Report">
  <img width="5%" src="https://i.postimg.cc/fbsyvkVW/requests.png" title="Requests" alt="Requests">
</p>

## Project Structure:
```
selenium-automation-demoqa/
├── features/              
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
│   ├── logger.py           
├── logs   # Captures and stores logs
│   ├── test.log  # Captures test execution logs
├── allure-results/  # Allure results folder
├── allure-report/   # Allure report folder
├── .gitignore           
├── requirements.txt  # List of dependencies
├── README.md          # Project documentation
└── ├── result_demoqa.PNG # Execution report
```

## Getting Started
```bash
# Clone repository
git clone https://github.com/Suvedha-n17/selenium-automation-demoqa.git

# Install virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```
## Running Tests
```
To run all feature file- From the project root:
behave

To run specific feature file

behave features/forms.feature"
behave features/checkbox.feature"
behave features/dynamic_properties.feature"
behave features/book_store.feature"

To run tests with Allure formatter
behave -f allure_behave.formatter:AllureFormatter -o allure-results

```
## Viewing reports
- Install [**Allure**](https://docs.qameta.io/allure/#_get_started) from the official website
- Generate Allure report
  
  ```bash
  allure serve
  ```
<p align="center">
  <img width="97%" src='https://github.com/Suvedha-n17/selenium-automation-demoqa/blob/master/result_demoqa.png' alt='allure'/>
</p>

- View [**Allure test results**](https://github.com/Suvedha-n17/selenium-automation-demoqa/blob/master/result_demoqa.png)

---
