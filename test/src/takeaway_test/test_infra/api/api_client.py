from test.src.takeaway_test.test_infra.api.case_classes.album import Album
from test.src.takeaway_test.test_infra.api.case_classes.comment import Comment
from test.src.takeaway_test.test_infra.api.case_classes.photo import Photo
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
        return UserLink(self_link=params['self']['href'], edit=params['edit']['href'], avatar=params['avatar']['href'] if 'avatar' in params else None)

    def __generate_user(self, params):
        return User(id=int(params['id']),
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
    def __generate_photo(self, params):
        return Photo(id=params['id'],
                     album_id=params['album_id'],
                     title=params['title'], thumbnail=params['thumbnail'], url=params['url'], _links=self.__generate_user_links(params['_links']))

    # _____________________________________________________________________________________________________________________________

    def __generate_comment(self, params):
        return Comment(id=params['id'],
                       post_id=params['post_id'],
                       body=params['body'], name=params['name'], email=params['email'], _links=self.__generate_user_links(params['_links']))

    # _____________________________________________________________________________________________________________________________
    def __generate_album(self, params):
        return Album(id=params['id'],
                     user_id=params['post_id'],
                     title=params['body'], _links=self.__generate_user_links(params['_links']))

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

    # _________________________________________ POSTS API CALLS SECTION __________________________________________

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
        return self.__generate_post(resp['result'])

        # _____________________________________________________________________________________________________________________________

    def update_post(self, post_id, post_data):
        return self.__http_client.post(url=config.POST_BY_ID.format(post_id), data=post_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def delete_post(self, post_id):
        return self.__http_client.delete(url=config.POST_BY_ID.format(post_id),
                                         params=self.token)

    # _________________________________________ PHOTOS API CALLS SECTION __________________________________________

    def get_all_photos(self):
        resp = self.__http_client.get(url=config.PHOTOS,
                                      params=self.token)
        return [self.__generate_photo(item) for item in resp['result']]

    def upload_photo(self, photo_data):
        return self.__http_client.post(url=config.PHOTOS, data=photo_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def get_photo_by_id(self, photo_id):
        resp = self.__http_client.get(url=config.PHOTO_BY_ID.format(photo_id), params=self.token)
        return self.__generate_photo(resp['result'])

        # _____________________________________________________________________________________________________________________________

    def update_photo(self, photo_id, photo_data):
        return self.__http_client.post(url=config.PHOTO_BY_ID.format(photo_id), data=photo_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def delete_photo(self, photo_id):
        return self.__http_client.delete(url=config.PHOTO_BY_ID.format(photo_id),
                                         params=self.token)

        # _________________________________________ COMMENTS API CALLS SECTION __________________________________________

    def get_all_comments(self):
        resp = self.__http_client.get(url=config.COMMENTS,
                                      params=self.token)
        return [self.__generate_comment(item) for item in resp['result']]
        # _____________________________________________________________________________________________________________________________

    def create_new_comment(self, comment_data):
        return self.__http_client.post(url=config.COMMENTS, data=comment_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def get_comment_by_id(self, comment_id):
        resp = self.__http_client.get(url=config.COMMENT_BY_ID.format(comment_id), params=self.token)
        return self.__generate_comment(resp['result'])

        # _____________________________________________________________________________________________________________________________

    def update_comment(self, comment_id, comment_data):
        return self.__http_client.post(url=config.COMMENT_BY_ID.format(comment_id), data=comment_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def delete_comment(self, comment_id):
        return self.__http_client.delete(url=config.COMMENT_BY_ID.format(comment_id),
                                         params=self.token)

        # _________________________________________ ALBUMS API CALLS SECTION __________________________________________

    def get_all_albums(self):
        resp = self.__http_client.get(url=config.ALBUMS,
                                      params=self.token)
        return [self.__generate_album(item) for item in resp['result']]

    def create_new_album(self, album_data):
        return self.__http_client.post(url=config.ALBUMS, data=album_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def get_album_by_id(self, album_id):
        resp = self.__http_client.get(url=config.ALBUM_BY_ID.format(album_id), params=self.token)
        return self.__generate_album(resp['result'])

        # _____________________________________________________________________________________________________________________________

    def update_album(self, album_id, album_data):
        return self.__http_client.post(url=config.ALBUM_BY_ID.format(album_id), data=album_data.to_dict(),
                                       params=self.token)
        # _____________________________________________________________________________________________________________________________

    def delete_album(self, album_id):
        return self.__http_client.delete(url=config.ALBUM_BY_ID.format(album_id),
                                         params=self.token)
