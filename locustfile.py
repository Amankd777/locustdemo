from locust import HttpUser, task, between, constant

class WebsiteUser(HttpUser):
    wait_time = constant(3)  # Wait for 3 seconds between requests

    @task
    def test_hello_world(self):
        try:
            response = self.client.get("/")
            if response.status_code != 200:
                self.environment.runner.stop()  # Stop the test if the request fails
        except Exception as e:
            print(f"Error: {e}")
            self.environment.runner.stop()  # Stop the test if an exception occurs
