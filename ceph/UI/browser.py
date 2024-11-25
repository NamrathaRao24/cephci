from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class Browser:
    def __init__(self, browser_type: str = "chrome"):
        """
        Initializes the Browser with the specified browser type.
        :param browser_type: The type of browser to use ('chrome', 'firefox', etc.). Defaults to 'chrome'.
        """
        self.driver = None
        if browser_type.lower() == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_type.lower() == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(
                f"Unsupported browser type: {browser_type}. Supported types are 'chrome' and 'firefox'."
            )

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

    def close(self):
        """
        Closes the browser and ends the session.
        """
        try:
            self.driver.quit()
        except WebDriverException as e:
            raise RuntimeError(f"Failed to close the browser: {e}")
