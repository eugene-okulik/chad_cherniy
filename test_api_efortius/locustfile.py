from locust import task, HttpUser
import random


class LocustUser(HttpUser):
    one_id = random.randint(1, 10000)

    @task
    def get_all_posts(self):
        self.client.get("/object")


    @task
    def get_one_post(self):
        self.client.get(f"/object/{self.one_id}")
