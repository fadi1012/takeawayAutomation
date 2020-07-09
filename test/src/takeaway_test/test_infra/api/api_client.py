from test.src.takeaway_test.test_infra.api.case_classes.post import Post
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
    def __generate_post(self, params):
        return Post(id=params['id'],
                    user_id=params['user_id'],
                    title=params['title'], body=params['body'], _links=self.__generate_user_links(params['_links']))

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

    def delete_user(self, user_id):
        return self.__http_client.delete(url=config.USER_BY_ID.format(user_id),
                                         params=self.token)

    # _________________________________________ POSTS SECTION __________________________________________

    def get_all_posts(self):
        resp = self.__http_client.get(url=config.POSTS,
                                      params=self.token)
        return [self.__generate_post(item) for item in resp['result']]

    def create_new_post(self, post_data):
        return self.__http_client.post(url=config.POSTS, data=post_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def get_post_by_id(self, user_id):
        resp = self.__http_client.get(url=config.POST_BY_ID.format(user_id), params=self.token)
        return self.__generate_user(resp['result'])

        # _____________________________________________________________________________________________________________________________

    def update_post(self, post_id, post_data):
        return self.__http_client.post(url=config.POST_BY_ID.format(post_id), data=post_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def delete_post(self, post_id):
        return self.__http_client.delete(url=config.POST_BY_ID.format(post_id),
                                         params=self.token)
