from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Dashboard:
    def __init__(self, driver):
        """
        Initializes the Dashboard with a WebDriver instance.
        :param driver: WebDriver instance for browser interaction.
        """
        if not driver or not hasattr(driver, "get"):
            raise ValueError("A valid WebDriver instance must be provided.")
        self.driver = driver

    def open(self, url: str):
        """
        Navigates to the specified URL.
        :param url: The URL to open in the browser.
        """
        if not isinstance(url, str):
            raise ValueError("A valid URL must be provided.")
        try:
            self.driver.get(url)
        except WebDriverException as e:
            raise RuntimeError(f"Failed to open URL '{url}': {e}")

    def is_element_visible(self, element_id: str, timeout: int = 10) -> bool:
        """
        Checks if an element is visible on the page within the given timeout.
        :param element_id: The ID of the element to check.
        :param timeout: Maximum time to wait for the element to be visible (default: 10 seconds).
        :return: True if the element is visible, False otherwise.
        """
        if not isinstance(element_id, str):
            raise ValueError("A valid element ID must be provided.")
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.ID, element_id))
            )
            return element.is_displayed()
        except TimeoutException:
            return False

    def click(self, element_id: str, timeout: int = 10):
        """
        Clicks a button or element identified by its ID.
        :param element_id: The ID of the element to click.
        :param timeout: Maximum time to wait for the element to be clickable (default: 10 seconds).
        """
        if not isinstance(element_id, str):
            raise ValueError("A valid element ID must be provided.")
        try:
            button = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.ID, element_id))
            )
            button.click()
        except TimeoutException:
            raise RuntimeError(
                f"Timed out waiting for the button with ID '{element_id}' to be clickable."
            )
        except WebDriverException as e:
            raise RuntimeError(
                f"Failed to click the button with ID '{element_id}': {e}"
            )
