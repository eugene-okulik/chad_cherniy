import allure


class BaseEndpoint:
    response = None
    status_code = None
    json = None

    @allure.step("Check status code is {expected_status}")
    def check_status_code(self, expected_status):
        actual_status = self.response.status_code if self.response is not None else self.status_code
        assert actual_status == expected_status, (
            f"Expected status code {expected_status}, got {actual_status}"
        )
