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
        self.client.get(
            url=API_ENDPOINT_PREFIX,
            headers=HEADERS,
        )

    @task
    def first_quote(self):
        # Trying to get first quote from the end point
        self.client.get(
            url=f'{API_ENDPOINT_PREFIX}/1',
            headers=HEADERS,
        )

    @task
    def any_quote(self):
        # Trying to get any quote (from 2 to 11) from the end point
        # Note! We exclude quote 1, this scenario covers in the previous task
        self.client.get(
            url=f'{API_ENDPOINT_PREFIX}/{SystemRandom().randint(2, 11)}',
            headers=HEADERS,
        )
