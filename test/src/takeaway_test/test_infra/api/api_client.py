from test.src.takeaway_test.test_infra.api.case_classes.user import User, UserLink
from test.src.takeaway_test.test_infra.conf import config
from test.src.takeaway_test.test_infra.utilities.http_client import HttpClient


class ApiClient:
    def __init__(self):
        self.__http_client = HttpClient()
        self.takeaway_token = "iiO3ZDQpM81BIqSgW79UA2c-iCa_V0otGWZU"
        self.token = {"access-token": self.takeaway_token}

    # +++++++++++++++++++++++++++++++++ private generation methods +++++++++++++++++++++++++++++#

    def __generate_user_links(self, params):
        return UserLink(self_link=params['self']['href'], edit=params['edit']['href'], avatar=params['avatar']['href'])

    def __generate_user(self, params):
        return User(id=params['id'],
                    first_name=params['first_name'],
                    last_name=params['last_name'], gender=params['gender'],
                    dob=params['dob'], email=params['email'], phone=params['phone'], website=params['website'],
                    address=params['address'], status=params['status'], _links=self.__generate_user_links(params['_links']))

    # _____________________________________________________________________________________________________________________________

    def get_list_of_users(self):
        resp = self.__http_client.get(url=config.USERS,
                                      params=self.token)
        return [self.__generate_user(item) for item in resp['result']]

    # _____________________________________________________________________________________________________________________________

    def create_new_user(self, user_data):
        return self.__http_client.post(url=config.USERS, data=user_data.to_dict(),
                                       params=self.token)

    # _____________________________________________________________________________________________________________________________

    def get_user_by_first_name(self, first_name):
        resp = self.__http_client.get(url=config.USER_BY_FIRST_NAME.format(first_name), params=self.token)
        return self.__generate_user(resp['result'])

    # _____________________________________________________________________________________________________________________________

    def get_user_by_id(self, user_id):
        resp = self.__http_client.get(url=config.USER_BY_ID.format(user_id), params=self.token)
        return self.__generate_user(resp['result'])

    # _____________________________________________________________________________________________________________________________

    def update_user(self, user_id, user_data):
        return self.__http_client.post(url=config.USER_BY_ID.format(user_id), data=user_data.to_dict(),
                                       params=self.token)
