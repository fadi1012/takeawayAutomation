from test.src.takeaway_test.test_infra.api.base_test_classes.base_api_test import BaseApiTest
from test.src.takeaway_test.test_infra.api.case_classes.album import Album


# this class contains shared methods that albums tests can use
class BaseAlbumsAutomationAssignmentTest(BaseApiTest):

    def get_all_albums(self):
        return self.api_client.get_all_albums()

    def create_new_album(self, id, album_data=None):
        new_album_data = album_data or Album.generate_default_album_details(id=id)
        self.api_client.create_new_album(album_data=new_album_data)
        return new_album_data

    def get_album_by_id(self, album_id):
        return self.api_client.get_album_by_id(album_id)

    def update_album(self, album_id, album_data):
        return self.api_client.update_album(album_id, album_data)

    def delete_album(self, album_id):
        return self.api_client.delete_album(album_id)

    def validate_album_details(self, album1, album2):
        assert album1.id == album2.id
        assert album1.user_id == album2.user_id
        assert album1.title == album2.title
        assert album1._links == album2._links