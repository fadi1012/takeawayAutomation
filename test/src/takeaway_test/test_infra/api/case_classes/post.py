from test.src.takeaway_test.test_infra.api.case_classes.user import UserLink
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


class Post:
    def __init__(self, id, user_id, title, body, _links):
        self.id = id
        self.user_id = user_id
        self.title = title
        self.body = body
        self._links = _links

    def to_dict(self):
        _links_dict = self._links.to_dict()
        return {'id': self.id,
                'user_id': self.user_id, 'title': self.title, 'body': self.body, "_links": _links_dict}

    @staticmethod
    def generate_default_post_details(id, links=None):
        links = links or UserLink(self_link="https://gorest.co.in/public-api/users/1964", edit="https://gorest.co.in/public-api/users/1964",
                                  avatar="https://gorest.co.in/public-api/users/1964")
        return Post(id=id, user_id=str(get_rand_number_between_zero_to_max_number(100, 1)), title="post-title", body="post body etc...", _links=links)
