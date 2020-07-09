from test.src.takeaway_test.infra.utilities.http_client import HttpClient


class AgentApiClient:
    def __init__(self):
        self.__http_client = HttpClient()
        self.takeaway_token = ""
        self.token =  {"Authorization": "Token " + self.takeaway_token}

    # _____________________________________________________________________________________________________________________________

    def get_stores(self):
        resp = self.__http_client.get(url="",
                                      headers=self.token)
        return resp
    # _____________________________________________________________________________________________________________________________

