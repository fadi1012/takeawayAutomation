import pytest

from test.src.takeaway_test.test_infra.api.base_test_classes.users.base_users_automation_assignment_test import BaseUserAutomationAssignmentTest
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


@pytest.mark.automation_assignment
class TestAutomationAssignmentUserValidation(BaseUserAutomationAssignmentTest):
    def test_user_automation_assignment(self):
        self.init_all_test_variables()
        # get list of all users
        users_list = self.get_list_of_users()
        assert len(users_list) > 1
        # create new user
        new_user = self.create_new_user(id=int(users_list[-1].id) + 1)
        updated_list = self.get_list_of_users()
        # validate user list is updated
        # TODO this validation is failing, i am getting a success in adding the user but when fetching again for the users it's not there
        assert len(updated_list) > len(users_list)
        # get specific user
        fetched_user = self.get_user_by_id(new_user.id)
        self.validate_user_details(fetched_user, new_user)
        # validate user details
        # update random user name from users list
        random_user = users_list(get_rand_number_between_zero_to_max_number(len(users_list) - 1, 0))
        random_user.first_name = "new_name"
        self.update_user(user_id=random_user.id, user_data=random_user)
        # get user by id and validate it's updated
        user = self.get_user_by_id(user_id=random_user.id)
        assert user.name == "new_name"
        # delete user
        self.delete_user(user_id=new_user.id)
        updated_list = self.get_list_of_users()
        # validate that number of users is back to the original before the new addition
        assert len(updated_list) == len(users_list)
