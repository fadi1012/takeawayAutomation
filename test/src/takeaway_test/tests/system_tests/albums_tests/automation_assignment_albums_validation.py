import pytest

from test.src.takeaway_test.test_infra.api.base_test_classes.albums.base_albums_automation_assignment_test import BaseAlbumsAutomationAssignmentTest
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


@pytest.mark.automation_assignment
class TestAutomationAssignmentAlbumsValidation(BaseAlbumsAutomationAssignmentTest):
    def test_albums_automation_assignment(self):
        self.init_all_test_variables()
        albums_list = self.get_all_albums()
        assert len(albums_list) > 1
        # add new album
        new_album = self.create_new_album(id=len(albums_list) + 1)
        updated_albums_list = self.get_all_albums()
        # validate albums list is updated
        assert len(updated_albums_list) > len(albums_list)
        # get specific album by id
        fetched_album_by_id = self.get_album_by_id(new_album.id)
        # validate album details
        self.validate_album_details(fetched_album_by_id, new_album)
        # update random album title from albums list
        random_album = get_rand_number_between_zero_to_max_number(len(albums_list) - 1, 0)
        random_album.title = "new album title"
        self.update_album(album_id=random_album.title, album_data=random_album)
        # get album by id and validate it's updated
        album = self.get_album_by_id(album_id=random_album.id)
        assert album.title == "new album title"
        # delete album
        self.delete_album(album_id=album.id)
        updated_albums_list = self.get_all_albums()
        # validate that number of album is back to the original before the new addition
        assert len(updated_albums_list) == len(albums_list)
