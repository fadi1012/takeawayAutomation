import pytest
from test.src.takeaway_test.test_infra.api.base_test_classes.posts.base_posts_automation_assignment_test import BasePostsAutomationAssignmentTest
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


@pytest.mark.automation_assignment
class TestAutomationAssignmentPostsValidation(BasePostsAutomationAssignmentTest):
    def test_posts_automation_assignment(self):
        self.init_all_test_variables()
        posts_list = self.get_all_posts()
        assert len(posts_list) > 1
        # create new post
        new_post = self.create_new_post(id=len(posts_list) + 1)
        updated_posts_list = self.get_list_of_posts()
        # validate posts list is updated
        assert len(updated_posts_list) > len(posts_list)
        # get specific post by id
        fetched_post_by_id = self.get_post_by_id(new_post.id)
        # validate post details
        self.validate_post_details(fetched_post_by_id, new_post)
        # update random post name from posts list
        random_post = posts_list[get_rand_number_between_zero_to_max_number(len(posts_list) - 1, 0)]
        random_post.title = "new title"
        self.update_post(post_id=random_post.id, post_data=random_post)
        # get post by id and validate it's updated
        post = self.get_post_by_id(post_id=random_post.id)
        assert post.title == "new title"
        # delete post
        self.delete_post(post_id=post.id)
        updated_list = self.get_all_posts()
        # validate that number of posts is back to the original before the new addition
        assert len(updated_list) == len(posts_list)
