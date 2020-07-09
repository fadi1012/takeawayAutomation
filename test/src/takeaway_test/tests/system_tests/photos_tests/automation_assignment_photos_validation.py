import pytest

from test.src.takeaway_test.test_infra.api.base_test_classes.photos.base_photos_automation_assignment_test import BasePhotosAutomationAssignmentTest
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


@pytest.mark.automation_assignment
class TestAutomationAssignmentPostsValidation(BasePhotosAutomationAssignmentTest):
    def test_photos_automation_assignment(self):
        self.init_all_test_variables()
        photos_list = self.get_all_photos()
        assert len(photos_list) > 1
        # upload new photo + validate case class details ( this happens in api_client no need to do it twice)
        new_photo = self.upload_new_photo(id=len(photos_list) + 1)
        updated_photos_list = self.get_all_photos()
        # validate photos list is updated
        assert len(updated_photos_list) > len(photos_list)
        # get specific photo by id
        fetched_new_photo_by_id = self.get_photo_by_id(new_photo.id)
        # validate new_photo details
        self.validate_photo_details(fetched_new_photo_by_id, new_photo)
        # update random photo title from photos list
        random_photo = photos_list[get_rand_number_between_zero_to_max_number(len(photos_list) - 1, 0)]
        random_photo.title = "new photo title"
        self.update_photo(photo_id=random_photo.id, photo_data=random_photo)
        # get photo  by id and validate it's updated
        photo = self.get_photo_by_id(photo_id=random_photo.id)
        assert photo.title == "new photo title"
        # delete photo
        self.delete_photo(photo_id=photo.id)
        updated_photos_list = self.get_all_photos()
        # validate that number of photos is back to the original before the new addition
        assert len(updated_photos_list) == len(photos_list)
