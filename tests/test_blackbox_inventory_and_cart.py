"""
Author: Kobe
Description: Black-box tests for customer dashboard and cart behavior.
Focus:
    - From the user's perspective, verify that only in-stock plants
      are visible on the customer dashboard.
    - Verify that an in-stock plant can be added to the cart and that
      the cart page reflects the correct item and total.

These tests interact with the application through HTTP routes and
rendered HTML, without calling the internal helper functions directly.
"""

import os
import sys
import unittest
from decimal import Decimal
from app import app, db
from app.models import User, UserRole, Plant

# Make sure Python can find src/app as the `app` package
CURRENT_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.join(CURRENT_DIR, "..", "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)


class TestBlackBoxInventoryAndCart(unittest.TestCase):
    def setUp(self):
        """
        Create an isolated app context, a fresh database, and a test client.
        """
        self.app = app
        self.app.config["TESTING"] = True

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        # Create a horticulturist (seller)
        self.seller = User(
            name="Seller",
            email="seller@example.com",
            password=b"test-seller",
            role=UserRole.HORTICULTURIST,
        )

        # Create a customer
        self.customer = User(
            name="Customer",
            email="customer@example.com",
            password=b"test-customer",
            role=UserRole.CUSTOMER,
        )

        db.session.add_all([self.seller, self.customer])
        db.session.commit()

        # Create one in-stock and one out-of-stock plant
        self.in_stock_plant = Plant(
            name="In-Stock Plant",
            color="Green",
            variety="flower",
            climate="temperate",
            quantity=5,
            price=Decimal("20.00"),
            seller_id=self.seller.id,
        )

        self.out_of_stock_plant = Plant(
            name="Sold-Out Plant",
            color="Brown",
            variety="succulent",
            climate="arid",
            quantity=0,
            price=Decimal("15.00"),
            seller_id=self.seller.id,
        )

        db.session.add_all([self.in_stock_plant, self.out_of_stock_plant])
        db.session.commit()

        self.client = self.app.test_client()

    def tearDown(self):
        """
        Drop all tables and pop the app context after each test.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def _login_as_customer(self):
        """
        Simulate a logged-in customer by setting the Flask-Login session key.

        This avoids testing authentication itself; login is only used as a
        precondition to reach customer-only pages.
        """
        with self.client.session_transaction() as session:
            session["_user_id"] = str(self.customer.id)
            session["_fresh"] = True

    def test_customer_dashboard_shows_only_in_stock_plants(self):
        """
        Black-box: The customer dashboard should list only plants with
        quantity > 0. Out-of-stock plants should not appear.
        """
        self._login_as_customer()

        response = self.client.get("/buyplants")
        self.assertEqual(
            response.status_code,
            200,
            "Customer dashboard did not load successfully.",
        )

        html = response.get_data(as_text=True)

        # In-stock plant should be visible
        self.assertIn(
            "In-Stock Plant",
            html,
            "In-stock plant name not found on customer dashboard.",
        )

        # Out-of-stock plant should not be visible
        self.assertNotIn(
            "Sold-Out Plant",
            html,
            "Sold-out plant is incorrectly visible on customer dashboard.",
        )

    def test_add_in_stock_plant_to_cart_and_view_cart(self):
        """
        Black-box: A customer should be able to add an in-stock plant
        to their cart, and the cart page should display the item and
        the correct total.
        """
        self._login_as_customer()

        # Add 2 units of the in-stock plant via the add-to-cart route
        response = self.client.post(
            "/mycart/add",
            data={
                "plant_id": self.in_stock_plant.id,
                "quantity": 2,
            },
            follow_redirects=True,
        )

        # The route redirects back to the customer dashboard on success
        self.assertEqual(
            response.status_code,
            200,
            "Adding to cart did not complete successfully.",
        )

        html_after_add = response.get_data(as_text=True)
        self.assertIn(
            "In-Stock Plant",
            html_after_add,
            "Expected plant name not visible after adding to cart.",
        )

        # Now view the cart page
        cart_response = self.client.get("/mycart")
        self.assertEqual(
            cart_response.status_code,
            200,
            "Cart page did not load successfully.",
        )

        cart_html = cart_response.get_data(as_text=True)

        # The cart should display the plant name
        self.assertIn(
            "In-Stock Plant",
            cart_html,
            "Plant not listed in cart page.",
        )

        # Quantity 2 should be visible somewhere in the table
        self.assertIn(
            "2",
            cart_html,
            "Expected quantity not shown for the cart item.",
        )

        # Total should be 2 * 20.00 = 40.00, rendered as "Total: $40.00"
        self.assertIn(
            "Total: $40.00",
            cart_html,
            "Cart total does not match expected value.",
        )


if __name__ == "__main__":
    unittest.main()
