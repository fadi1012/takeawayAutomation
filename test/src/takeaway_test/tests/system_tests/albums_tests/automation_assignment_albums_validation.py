import pytest

from test.src.takeaway_test.test_infra.api.base_test_classes.comments.base_comments_automation_assignment_test import BaseCommentsAutomationAssignmentTest
from test.src.takeaway_test.test_infra.api.base_test_classes.posts.base_posts_automation_assignment_test import BasePostsAutomationAssignmentTest
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


@pytest.mark.automation_assignment
class TestAutomationAssignmentCommentsValidation(BaseCommentsAutomationAssignmentTest):
    def test_comments_automation_assignment(self):
        self.init_all_test_variables()
        comments_list = self.get_all_comments()
        assert len(comments_list) > 1
        # add new comment
        new_comment = self.create_new_comment(id=len(comments_list) + 1)
        updated_comments_list = self.get_all_comments()
        # validate comments list is updated
        assert len(updated_comments_list) > len(comments_list)
        # get specific comment by id
        fetched_comment_by_id = self.get_comment_by_id(new_comment.id)
        # validate comment details
        self.validate_comment_details(fetched_comment_by_id, new_comment)
        # update random comment name from users list
        random_comment = get_rand_number_between_zero_to_max_number(len(comments_list) - 1, 0)
        random_comment.name = "new comment name"
        self.update_comment(comment_id=random_comment.id, comment_data=random_comment)
        # get comment by id and validate it's updated
        comment = self.get_comment_by_id(comment_id=random_comment.id)
        assert comment.name == "new comment name"
        # delete comment
        self.delete_comment(comment_id=comment.id)
        updated_comments_list = self.get_all_comments()
        # validate that number of comments is back to the original before the new addition
        assert len(updated_comments_list) == len(comments_list)
