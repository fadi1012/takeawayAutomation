from test.src.takeaway_test.test_infra.api.base_test_classes.base_api_test import BaseApiTest
from test.src.takeaway_test.test_infra.api.case_classes.comment import Comment
from test.src.takeaway_test.test_infra.api.case_classes.post import Post


# this class contains shared method that comments tests can use
class BaseCommentsAutomationAssignmentTest(BaseApiTest):

    def get_all_comments(self):
        return self.api_client.get_all_comments()

    def create_new_comment(self, id, comment_data=None):
        new_comment_data = comment_data or Comment.generate_default_comment_details(id=id)
        self.api_client.create_new_comment(post_data=new_comment_data)
        return new_comment_data

    def get_comment_by_id(self, comment_id):
        return self.api_client.get_comment_by_id(comment_id)

    def update_comment(self, comment_id, comment_data):
        return self.api_client.update_comment(comment_id, comment_data)

    def delete_comment(self, comment_id):
        return self.api_client.delete_comment(comment_id)

    def validate_comment_details(self, comment1, comment2):
        assert comment1.id == comment2.id
        assert comment1.post_id == comment2.post_id
        assert comment1.name == comment2.name
        assert comment1.email == comment2.email
        assert comment1.body == comment2.body
        assert comment1._links == comment2._links
