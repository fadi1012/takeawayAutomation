from test.src.takeaway_test.test_infra.api.base_test_classes.base_api_test import BaseApiTest
from test.src.takeaway_test.test_infra.api.case_classes.photo import Photo
from test.src.takeaway_test.test_infra.api.case_classes.post import Post

# this class contains shared method that photo tests can use
class BasePhotosAutomationAssignmentTest(BaseApiTest):

    def get_all_photos(self):
        return self.api_client.get_all_photos()

    def upload_new_photo(self, id, photo_data=None):
        new_photo_data = photo_data or Photo.generate_default_photo_details(id=id)
        self.api_client.upload_new_photo(photo_data=new_photo_data)
        return new_photo_data

    def get_photo_by_id(self, photo_id):
        return self.api_client.get_photo_by_id(photo_id)

    def delete_photo(self, photo_id):
        return self.api_client.delete_photo(photo_id)

    def update_photo(self, photo_id, photo_data):
        return self.api_client.update_photo(photo_id, photo_data)

    def validate_photo_details(self, photo1, photo2):
        # TODO need to be updated
        assert photo1.id == photo2.id
        assert photo1.album_id == photo2.album_id
        assert photo1.title == photo2.title
        assert photo1.url == photo2.url
        assert photo1.thumbnail == photo2.thumbnail
        assert photo1._links == photo2._links
