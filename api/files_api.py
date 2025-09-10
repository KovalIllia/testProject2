import allure
import requests

from api.base_api import ApiClient


class FilesApi(ApiClient):
    def upload_pet_image(self,pet_id: int,
                         file_path:str,
                         additional_metadata:str=None):
        url=self.build_url(f"/pet/{pet_id}/uploadImage")
        files= {"file": open(file_path, "rb")}
        data={}
        if additional_metadata:
            data["additional_metadata"]=additional_metadata
        self.logger.add_request(url,method="POST",body=data)
        with allure.step(f"POST /pet/{pet_id}/uploadImage"):
            response = requests.post(url, data=data, files=files)
        self.logger.add_response(response)
        return response