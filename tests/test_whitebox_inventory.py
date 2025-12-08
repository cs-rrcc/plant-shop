"""
Author: Kobe
Description: White-box test for internal inventory visibility logic.
Focus:
    - Ensure that the internal helper function get_all_plant_listings()
      only returns plants with quantity > 0.
    - This is a white-box test because it calls the helper directly and
      inspects its return values, with full knowledge of the implementation.
"""

import os
import sys
import unittest
from decimal import Decimal
from app import app, db
from app.models import User, UserRole, Plant
from app.routes import get_all_plant_listings

# Make sure Python can find src/app as the `app` package
CURRENT_DIR = os.path.dirname(__file__)
SRC_PATH = os.path.join(CURRENT_DIR, "..", "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)


class TestWhiteBoxInventory(unittest.TestCase):
    def setUp(self):
        """
        Create an isolated app context and a fresh database with a few plants.
        """
        self.app = app
        self.app.config["TESTING"] = True

        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

        # Create a horticulturist so plants can reference a valid seller_id
        self.seller = User(
            name="Test Seller",
            email="seller@example.com",
            password=b"test-password",
            role=UserRole.HORTICULTURIST,
        )
        db.session.add(self.seller)
        db.session.commit()

        # In-stock plant
        self.in_stock_plant_1 = Plant(
            name="In-Stock Plant 1",
            color="Green",
            variety="flower",
            climate="temperate",
            quantity=5,
            price=Decimal("10.00"),
            seller_id=self.seller.id,
        )

        # Out-of-stock plant
        self.out_of_stock_plant = Plant(
            name="Sold-Out Plant",
            color="Yellow",
            variety="flower",
            climate="temperate",
            quantity=0,
            price=Decimal("5.00"),
            seller_id=self.seller.id,
        )

        # Another in-stock plant
        self.in_stock_plant_2 = Plant(
            name="In-Stock Plant 2",
            color="Red",
            variety="succulent",
            climate="arid",
            quantity=3,
            price=Decimal("7.50"),
            seller_id=self.seller.id,
        )

        db.session.add_all(
            [
                self.in_stock_plant_1,
                self.out_of_stock_plant,
                self.in_stock_plant_2,
            ]
        )
        db.session.commit()

        # Cache IDs for precise comparisons later
        self.in_stock_ids = {
            self.in_stock_plant_1.id,
            self.in_stock_plant_2.id,
        }
        self.out_of_stock_id = self.out_of_stock_plant.id

    def tearDown(self):
        """
        Drop all tables and pop the app context so each test runs isolated.
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_all_plant_listings_excludes_zero_quantity(self):
        """
        Verify that get_all_plant_listings only returns plants that have
        quantity > 0 and excludes any plant with quantity == 0.
        """
        listings = get_all_plant_listings()

        # All returned plants must have quantity > 0
        self.assertTrue(
            all(plant.quantity > 0 for plant in listings),
            "Found a plant with zero or negative quantity in the listings.",
        )

        returned_ids = {plant.id for plant in listings}

        # The in-stock plants must be present
        self.assertTrue(
            self.in_stock_ids.issubset(returned_ids),
            "Expected in-stock plants are missing from the listings.",
        )

        # The sold-out plant must not be present
        self.assertNotIn(
            self.out_of_stock_id,
            returned_ids,
            "Sold-out plant should not be included in the listings.",
        )


if __name__ == "__main__":
    unittest.main()
