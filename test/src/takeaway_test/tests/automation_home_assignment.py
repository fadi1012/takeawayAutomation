import pytest

from test.src.takeaway_test.test_infra.api.base_test_classes.base_automation_assignment import BaseAutomationAssignment


@pytest.mark.automation_assignment
class TestAutomationAssignment(BaseAutomationAssignment):
    def test_automation_assignment(self):
        pass
