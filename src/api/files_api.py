import requests

from src.api.base_api import ApiClient


class FilesApi(ApiClient):
    # def upload_pet_image(self,pet_id: int,
    #                      file_path:str,
    #                      additional_metadata:str=None):
    #     url=self.build_url(f"/pet/{pet_id}/uploadImage")
    #     files= {"file": open(file_path, "rb")}
    #     data={}
    #     if additional_metadata:
    #         data["additional_metadata"]=additional_metadata
    #     self.logger.add_request(url,method="POST",body=data)
    #     with allure.step(f"POST /pet/{pet_id}/uploadImage"):
    #         response = requests.post(url, data=data, files=files)
    #     self.logger.add_response(response)
    #     return response

    def upload_pet_image(self, pet_id: int, file_path: str, additional_metadata: str = None):
        url = self.build_url(f"/pet/{pet_id}/uploadImage")
        files = {"file": open(file_path, "rb")}
        data = {"additionalMetadata": additional_metadata} if additional_metadata else {}
        response = requests.post(url, files=files, data=data)
        files["file"].close()
        return response
