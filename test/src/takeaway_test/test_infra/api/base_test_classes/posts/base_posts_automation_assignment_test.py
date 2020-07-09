from test.src.takeaway_test.test_infra.api.base_test_classes.base_api_test import BaseApiTest
from test.src.takeaway_test.test_infra.api.case_classes.post import Post

# this class contains shared method that posts tests can use
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

    def validate_post_details(self, post1, post2):
        assert post1.id == post2.id
        assert post1.user_id == post2.user_id
        assert post1.title == post2.title
        assert post1.body == post2.body
        assert post1._links == post2._links
