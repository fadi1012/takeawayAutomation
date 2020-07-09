from test.src.takeaway_test.test_infra.api.case_classes.user import UserLink


class Album:
    def __init__(self, id, user_id, title, _links):
        self.id = id
        self.user_id = user_id
        self.title = title
        self._links = _links

    def to_dict(self):
        _links_dict = self._links.to_dict()
        return {'id': self.id,
                'user_id': self.user_id, 'title': self.title, "_links": _links_dict}

    @staticmethod
    def generate_default_album_details(id, links=None, user_id=None):
        user_id = "12313" or user_id
        links = links or UserLink(self_link="https://gorest.co.in/public-api/albums/1964", edit="https://gorest.co.in/public-api/albums/1964")
        return Album(id=id, user_id=user_id, title="album title", _links=links)
