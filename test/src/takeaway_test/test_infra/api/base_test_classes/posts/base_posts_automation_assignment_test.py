from test.src.takeaway_test.test_infra.api.base_test_classes.base_api_test import BaseApiTest
from test.src.takeaway_test.test_infra.api.case_classes.post import Post


class BasePostsAutomationAssignmentTest(BaseApiTest):

    def get_all_posts(self):
        return self.api_client.get_all_posts()

    def create_new_post(self, id, post_data=None):
        new_post_data = post_data or Post.generate_default_post_details(id=id)
        self.api_client.create_new_post(post_data=new_post_data)
        return new_post_data

    def get_post_by_id(self, post_id):
        return self.api_client.get_post_by_id(post_id)

    def update_post(self, post_id, post_data):
        return self.api_client.update_post(post_id, post_data)

    def delete_post(self, post_id):
        return self.api_client.delete_post(post_id)

    def validate_post_details(self, user1, user2):
        assert user1.id == user2.id
        assert user1.user_id == user2.user_id
        assert user1.title == user2.title
        assert user1.body == user2.body
        assert user1._links == user2._links
