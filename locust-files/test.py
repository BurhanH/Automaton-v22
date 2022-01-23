from random import SystemRandom

from locust import HttpUser, task

# Target URL - api-flask-baur.herokuapp.com/
API_ENDPOINT_PREFIX = 'api/v1/quotes'
HEADERS = {'Content-type': 'application/json'}


class QuickStart(HttpUser):

    def on_start(self):
        # Get authorization token, etc.
        pass

    def on_stop(self):
        # Close client session, etc.
        pass

    @task
    def random_quote(self):
        # Trying to get random quote from the end point
        with self.client.get(
            url=API_ENDPOINT_PREFIX,
            headers=HEADERS,
            catch_response=True
        ) as response:
            if response.status_code != 200:
                response.failure("Failed to get random quote")
            if response.text == '{}':
                response.failure("Empty response")
            if response.elapsed.total_seconds() > 0.5:
                response.failure("Response took longer than 0.5 second")

    @task
    def first_quote(self):
        # Trying to get first quote from the end point
        with self.client.get(
            url=f'{API_ENDPOINT_PREFIX}/1',
            headers=HEADERS,
        ) as response:
            if response.status_code != 200:
                response.failure("Failed to get first quote")
            if response.text == '{}':
                response.failure("Empty response")
            if response.elapsed.total_seconds() > 0.5:
                response.failure("Response took longer than 0.5 second")

    @task
    def any_quote(self):
        # Trying to get any quote (from 2 to 11) from the end point
        # Note! We exclude quote 1, this scenario covers in the previous task
        quiote_id = SystemRandom().randint(2, 11)
        with self.client.get(
            url=f'{API_ENDPOINT_PREFIX}/{quiote_id}',
            headers=HEADERS,
        ) as response:
            if response.status_code != 200:
                response.failure(f'Failed to get {quiote_id} quote')
            if response.text == '{}':
                response.failure("Empty response")
            if response.elapsed.total_seconds() > 0.5:
                response.failure("Response took longer than 0.5 second")
