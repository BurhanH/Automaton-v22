from random import SystemRandom

from locust import HttpUser, task

# Target URL - http://api-flask-baur.herokuapp.com
API_ENDPOINT_PREFIX = '/api/v1/quotes'
HEADERS = {'Content-type': 'application/json'}


class QuickStart(HttpUser):

    def on_start(self):
        # Get authorization token, etc.
        pass

    def on_stop(self):
        # Close client session, etc.
        pass

    def get_quote(self, quote_id=None):
        target_endpoint = API_ENDPOINT_PREFIX
        if quote_id:
            target_endpoint = f'{API_ENDPOINT_PREFIX}/{quote_id}'

        with self.client.get(
            url=target_endpoint,
            headers=HEADERS,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Failed to get quote")
            if response.text == "{}":
                response.failure("Empty response")
            if response.elapsed.total_seconds() > 0.5:
                response.failure("Response took longer than 0.5 second")

    @task
    def random_quote(self):
        # Trying to get random quote from the end point
        self.get_quote()

    @task
    def first_quote(self):
        # Trying to get first quote from the end point
        self.get_quote(1)

    @task
    def any_quote(self):
        # Trying to get any quote (from 2 to 11) from the end point
        # Note! We exclude quote 1, this scenario covers in the previous task
        quiote_id = SystemRandom().randint(2, 11)
        self.get_quote(quiote_id)
