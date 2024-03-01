from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 2)  # Random wait time between requests (1-2 seconds)

    @task
    def test_hello_world(self):
        self.client.get("/")  # Simulates a GET request to the homepage route