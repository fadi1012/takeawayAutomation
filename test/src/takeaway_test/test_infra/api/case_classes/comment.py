from test.src.takeaway_test.test_infra.api.case_classes.user import UserLink


class Comment:
    def __init__(self, id, post_id, name, email, _links, body):
        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body
        self._links = _links

    def to_dict(self):
        _links_dict = self._links.to_dict()
        return {'id': self.id,
                'post_id': self.post_id, 'name': self.name, 'email': self.email, "_links": _links_dict, "body": self.body}

    @staticmethod
    def generate_default_comment_details(id, links=None, post_id=None):
        post_id = "12313" or post_id
        links = links or UserLink(self_link="https://gorest.co.in/public-api/comment/1964", edit="https://gorest.co.in/public-api/comment/1964",
                                  avatar="https://gorest.co.in/public-api/comment/1964")
        return Comment(id=id, post_id=post_id, email="post-title", body="post body etc...", _links=links, name="default name")
