from test.src.takeaway_test.test_infra.api.case_classes.user import UserLink
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


class Photo:
    def __init__(self, id, url, title, album_id, _links, thumbnail):
        self.id = id
        self.album_id = album_id
        self.title = title
        self.url = url
        self.thumbnail = thumbnail
        self._links = _links

    def to_dict(self):
        _links_dict = self._links.to_dict()
        return {'id': self.id,
                'url': self.url, 'title': self.title, 'album_id': self.album_id, "_links": _links_dict, "thumbnail": self.thumbnail}

    @staticmethod
    def generate_default_photo_details(id, links=None, album_id=None):
        album_id = "12313" or album_id
        links = links or UserLink(self_link="https://gorest.co.in/public-api/photos/1964", edit="https://gorest.co.in/public-api/photos/1964",
                                  avatar="https://gorest.co.in/public-api/photos/1964")
        return Photo(id=id, album_id=album_id, url="w", title="post-title", thumbnail="post body etc...", _links=links)
