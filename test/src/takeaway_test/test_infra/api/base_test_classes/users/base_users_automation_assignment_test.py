from test.src.takeaway_test.test_infra.api.base_test_classes.base_api_test import BaseApiTest
from test.src.takeaway_test.test_infra.api.case_classes.user import User


class BaseUserAutomationAssignmentTest(BaseApiTest):

    def get_list_of_users(self):
        return self.api_client.get_list_of_users()

    def create_new_user(self, id, user=None):
        new_user_data = user or User.generate_default_user_details(id=id)
        self.api_client.create_new_user(user_data=new_user_data)
        return new_user_data

    def get_user_by_first_name(self, first_name):
        return self.api_client.get_user_by_first_name(first_name)

    def get_user_by_id(self, user_id):
        return self.api_client.get_user_by_id(user_id)

    def update_user(self, user_id, user_data):
        return self.api_client.update_user(user_id, user_data)

    def delete_user(self, user_id):
        return self.api_client.delete_user(user_id)

    def validate_user_details(self, user1, user2):
        assert user1.id == user2.id
        assert user1.first_name == user2.first_name
        assert user1.last_name == user2.last_name
        assert user1.phone == user2.phone
        assert user1.address == user2.address
        assert user1.gender == user2.gender
        assert user1.dob == user2.dob
        assert user1.email == user2.email
        assert user1.website == user2.website
        assert user1.address == user2.address
        assert user1.status == user2.status
        assert user1._links == user2._links
