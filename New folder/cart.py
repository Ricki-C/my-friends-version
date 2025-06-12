from product import Product
from member import Member, SilverMember, GoldMember, PlatinumMember
from coupon import Coupon, FixedDiscountCoupon, PercentDiscountCoupon


class ShoppingCart:
    def __init__(self):
        # TODO: Implement this method
        self.products = []
        self.membership = None
        self.coupons = {}
        

    def add_item(self, item: Product):
        """Add the specified item to the cart.

        Args:
            item (Product): The item to add to the cart.
        """
        # TODO: Implement this method
        self.products.append(item)
        return

    def add_membership(self, membership: Member):
        """Add a membership to the cart.

        Args:
            membership (Member): The membership to add to the cart.
        """
        # TODO: Implement this method
        self.membership = membership
        return

    def add_coupon(self, coupon: Coupon):
        """Add a coupon to the cart.

        Args:
            coupon (Coupon): The coupon to add to the cart.
        """
        # TODO: Implement this method
        if coupon.numeric_barcode in self.coupons:
            return
        self.coupons[coupon.numeric_barcode] = coupon

    def get_items(self) -> list[Product]:
        """Get the items in the cart.

        Returns:
            list[Product]: The items in the cart.
        """
        # TODO: Implement this method
        return self.products

    def get_membership(self) -> Member:
        """Get the membership in the cart.

        Returns:
            Member: The membership in the cart.
        """
        # TODO: Implement this method
        return self.membership

    def get_coupons(self) -> list[Coupon]:
        """Get the coupons in the cart.

        Returns:
            list[Coupon]: The coupons in the cart.
        """
        # TODO: Implement this method
        return list(self.coupons.values())

    def calculate_subtotal(self) -> float:
        """Calculate the price of all items in the cart.

        Returns:
            float: The subtotal of the cart.
        """
        # TODO: Implement this method
        return sum([float(item.get_price()) for item in self.products])

    def calculate_total(self) -> float:
        """Calculate the total price of the cart, with coupon applied and membership applicable

        Returns:
            float: The total price of the cart.
        """
        # TODO: Implement this method
        subtotal = self.calculate_subtotal()
        total_coupon_discount = sum([coupon.discount_amount(subtotal) for coupon in self.coupons.values()])
        if self.membership:
            membership_discount = subtotal * self.membership.get_discount_rate()
        else:
            membership_discount = 0
        sum_discount = total_coupon_discount + membership_discount
        total = max(subtotal - sum_discount, 0.0)
        return total
        

    def __str__(self):
        """Return a string representation of the shopping cart. This is for debugging purposes

        Returns:
            str: A formatted string showing the cart's contents, membership, coupons, and totals.
        """
        # OPTIONAL
        

def shopping_cart_doctests():
    """Function to run the doctests for the ShoppingCart class.

    Note that you should run this doctest at the root folder of the project
    (same level as main.py)

    # It's recommended that you add additional doctests

    >>> cart = ShoppingCart()
    >>> cart.add_item(Product('random_barcode', 'Milk', 2, 150))
    >>> cart.add_item(Product('random_barcode2', 'Bread', 3, 80))
    >>> cart.calculate_subtotal() == 5 == cart.calculate_total()
    True
    >>> sm = PlatinumMember('random_barcode3', 'John', 0)
    >>> cart.add_membership(sm)
    >>> cart.calculate_total() == 4.5
    True
    >>> from datetime import datetime
    >>> fc = FixedDiscountCoupon('b4', datetime(2030, 1, 1), 1, 'desc', 1)
    >>> cart.add_coupon(fc)
    >>> cart.calculate_total() == 3.5
    True
    >>> cart.add_coupon(fc)
    >>> len(cart.get_coupons()) == 1
    True
    >>> len(cart.get_items()) == 2
    True
    """
