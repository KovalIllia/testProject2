import datetime
import os
import requests

class Logger():

    if not os.path.exists('logs'):
        os.makedirs('logs')

    file_name=f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"


    @classmethod
    def write_log_to_file(cls,data:str):
        with open(cls.file_name, 'a',encoding='utf-8') as logger_file:
            logger_file.write(data)

    @classmethod
    def add_request(cls,url:str, method: str,body:None):
        test_name=os.environ.get("PYTEST_CURRENT_TEST")#назва тесту який виконується

        data_to_add = f"\n-----\n"#дані які додаються з переносами і пробілами
        data_to_add += f"Test:  {test_name}\n"
        data_to_add += f"Time:  {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method:  {method}\n"
        data_to_add += f"Request URL:  {url}\n"
        data_to_add += "\n"
        if body is not None:
            data_to_add += f"Request body: {body}\n"

        data_to_add += "\n"
        cls.write_log_to_file(data_to_add)


    @classmethod
    def add_response(cls,response,body=None,endpoint_name:str=None):
        data_to_add=""
        if endpoint_name:
            data_to_add+=f"Endpoint: {endpoint_name}\n"
        data_to_add = f"Response status: {response.status_code}\n"
        data_to_add += f"Response body: {response.text}\n"

        if body is not None:
            data_to_add += f"Request body: {body}\n"

        data_to_add += "-----\n"

        print(data_to_add)
        cls.write_log_to_file(data_to_add)
        # cookie_as_dict=dict(result.cookies)#поміщ в файл
        # headers_as_dict=dict(result.headers)#поміщ в файл
        #
        # data_to_add = f"Response code: {result.status_code}\n"#які дані ще додаються в файл -- при оголошенні тільки "=", а не "+="
        # data_to_add += f"Response text: {result.text}\n"#які дані ще додаються в файл
        # data_to_add += f"Response headers: {headers_as_dict}\n"#які дані ще додаються в файл
        # data_to_add += f"Response cookies: {cookie_as_dict}\n"#які дані ще додаються в файл
        # data_to_add += f"\n-----\n"  # string для розділення
        #
        # cls.write_log_to_file(data_to_add)