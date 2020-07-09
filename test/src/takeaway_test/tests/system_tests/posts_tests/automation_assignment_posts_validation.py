import pytest

from test.src.takeaway_test.test_infra.api.base_test_classes.posts.base_posts_automation_assignment_test import BasePostsAutomationAssignmentTest
from test.src.takeaway_test.test_infra.api.base_test_classes.users.base_users_automation_assignment_test import BaseUserAutomationAssignmentTest
from test.src.takeaway_test.test_infra.helper.helper import get_rand_number_between_zero_to_max_number


@pytest.mark.automation_assignment
class TestAutomationAssignmentPostsValidation(BasePostsAutomationAssignmentTest):
    def test_posts_automation_assignment(self):
        self.init_all_test_variables()
        self.get_all_posts()
