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

## Project structure

├── **api**/ # clients to call the API

├── **scripts**/ # helper scripts to run

├── **tests**/ # main tests

│ ├── **factories**/ # test data factories
│ ├── **utils**/ # utilities and helpers

│ ├── **test_pet_api.py**

│ ├── **test_store_api.py**

│ └── **test_petStoreApiTests.py**


├── **conftest.py** # global pytest fixtures

├── **requirements.txt** # Python dependencies

├── **pytest.ini** # pytest configuration

├── **Dockerfile** # build environment in Docker



## Technologies used
- Python 3.9
- Pytest
- Faker (data generation)
- Allure (reporting)
- Docker



## Install and Run 
**Local**
git clone https://github.com/username/testProject2.git # Clone the repository
cd testProject2

**Create a virtual environment and install dependencies**
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

**Run tests with Allure report generation**
pytest --alluredir=allure_report




## Docker

**Build the image**
docker build -t pytest_runner .

**Run tests with result mapping**
docker run --rm -v $(pwd)/test_result:/app/test_result pytest_runner


## Reports

The execution results are stored in the following directories:

**allure_report**/ — when running locally

**test_result**/ — when running in Docker

You can open the report with the command:

**allure serve allure_report**

