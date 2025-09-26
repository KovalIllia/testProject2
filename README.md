## Project Description
This repository contains a set of **automated API tests** to test the operation of the online store service.
The tests are implemented in **Python 3.9** using **pytest**, and also have integration with **Allure** for building detailed reports.
**Docker** is used for ease of launch and environment isolation.

## Goal and objectives
The goal is to verify the stability and correctness of the REST API.
Main tasks:
- testing CRUD operations for `pet`, `store`, `files` resources;
- checking positive and negative scenarios;
- generating structured reports for analyzing results;
- the ability to run tests locally and in CI/CD.

This project **does not include**:
- UI testing;
- load testing.



## Technologies used
- Python 3.9
- Pytest
- Faker (data generation)
- Allure (reporting)
- Docker



## Install and Run 
**Local**
`git clone https://github.com/username/testProject2.git `# Clone the repository
**cd testProject2**


Create a virtual environment and install dependencies
``python3 -m venv .venv``
``source .venv/bin/activate``
``pip install -r requirements.txt``

Run tests with Allure report generation
``pytest --alluredir=allure_report``




## Docker

Build the image
``docker build -t pytest_runner .``

Run tests with result mapping
``docker run -v $(pwd)/output/test_result:/output/test_result pytest_runner``


## Reports

The execution results are stored in the following directories:

``allure_report``/ — when running locally

`test_result`/ — when running in Docker

`allure serve allure_report`/ — You can open the report with the command:

`./output/scripts/run_tests.sh`/- run a script to generate allure report


## GitHub Actions
https://github.com/KovalIllia/testProject2/blob/master/.github/workflows/pytest.yml