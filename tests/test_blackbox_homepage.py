"""
Black-box Selenium test for the Unbeleafable Plant Shop home page.

User Story:
    As a visitor, I want to see a clear welcome message and navigation
    options on the home page so I know what the site is and how to log
    in or sign up.

Preconditions:
    - Flask app is running at http://localhost:5000
    - This test only inspects public UI on the home page.

Run with:
    python3 -m unittest tests.test_blackbox_homepage
"""

import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

BASE_URL = "http://127.0.0.1:5000"



class TestBlackBoxHomePage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Start a single headless browser for all tests."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")  # remove this to watch the browser
        options.add_argument("--window-size=1920,1080")

        cls.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )
        cls.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get(BASE_URL)

    def test_homepage_welcome_and_nav_blackbox(self):
        """
        Black-box test for the public home page.

        GIVEN an anonymous visitor
        WHEN they open the site's root URL
        THEN they see the site title, welcome message, and login/sign-up options.
        """
        driver = self.driver

        # Wait for the main header to be present
        header_h1 = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertEqual("Unbeleafable Plant Shop", header_h1.text)

        # Check the document <title>
        self.assertIn("Unbeleafable Plant Shop", driver.title)

        # Check the main welcome message from index.html
        h2 = driver.find_element(By.TAG_NAME, "h2")
        self.assertIn("Welcome to your one-stop plant shop!", h2.text)

        # Verify the explanatory subheading is present on the page
        page_source = driver.page_source
        self.assertIn(
            "Whether you need to buy or sell plants, we",
            page_source,
            msg="Expected the welcome description text on the home page.",
        )

        # Check navigation links for an anonymous user
        nav = driver.find_element(By.TAG_NAME, "nav")
        nav_text = nav.text

        # From base.html when not authenticated:
        #   Home, Login, Sign Up
        self.assertIn("Home", nav_text)
        self.assertIn("Login", nav_text)
        self.assertIn("Sign Up", nav_text)


if __name__ == "__main__":
    unittest.main()
