import random

from faker import Faker

fake = Faker()


class PetFactory:
    @staticmethod
    def default_pet(name=fake.first_name(), status="available") -> dict:
        return {
            "id": random.randint(1, 1000),
            "category": {
                "id": random.randint(1, 1000),
                "name": fake.word()
            },
            "name": fake.first_name(),
            "photoUrls": [fake.image_url()],
            "tags": [
                {
                    "id": random.randint(1, 1000),
                    "name": fake.word()
                }
            ],
            "status": status
        }


class UpdatePetFactory:
    @staticmethod
    def update_pet_with_name_and_status(name: str = None, status: str = None) -> dict:
       return {"name":name or "Topik",status:status or "available"}