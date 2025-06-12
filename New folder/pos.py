from store_backend import StoreBackend
from barcode import BarcodeProcessor
from cart import ShoppingCart


class POSSystem:
    def __init__(
        self,
        inventory_path: str,
        membership_path: str,
        coupon_path: str,
    ):

        # TODO: Implement this method
        self.store_backend = StoreBackend(inventory_path, membership_path, coupon_path)
        self.barcode_processor = BarcodeProcessor()
        self.shopping_cart = ShoppingCart()

    def process_barcodes(self, barcode_file_path: str) -> None:
        """For each line in the barcode file (length 95 strings), we will need to do the following:
        1. Validate the barcode
        2. If it doesn't work, flip the barcode and try again
        3.1 If it doesn't work, just skip the barcode
        3.2 If it does work, convert the barcode to 12 digits (and continue to step 4)
        4. Identify the type of the barcode (item, coupon, or membership)
        5. Process the barcode based on its type (update the shopping cart instance
        """

        # TODO: Implement this method
        with open(barcode_file_path, 'r') as f:
            barcodes = [line.strip() for line in f if line.strip()]
            for barcode in barcodes:
                try:
                    if not self.barcode_processor.validate_barcode(barcode):
                        raise ValueError
                except ValueError:
                    inverted_barcode = self.barcode_processor.inver_barcode(barcode)
                    try:
                        if not self.barcode_processor.validate_barcode(inverted_barcode):
                            continue
                        else:
                            barcode = inverted_barcode
                    except ValueError:
                        continue
                digit_barcode = self.barcode_processor.convert_to_12_digits(barcode)
                if not self.barcode_processor.modulo_check(digit_barcode):
                    continue
                else:
                    type_of_barcode = self._identify_barcode_type(digit_barcode)
                    if not type_of_barcode:
                        continue
                    if type_of_barcode == "product":
                        product = self.store_backend.get_product(digit_barcode)
                        if product.quantity > 0 and product:
                            self.shopping_cart.add_item(product)
                    elif type_of_barcode == "coupon":
                        coupon = self.store_backend.get_coupon(digit_barcode)
                        if coupon:
                            self.shopping_cart.add_coupon(coupon)
                    elif type_of_barcode == "membership":
                        membership = self.store_backend.get_member(digit_barcode)
                        if membership:
                            self.shopping_cart.add_membership(membership)

    def _identify_barcode_type(self, numeric_barcode: str) -> str:
        """Given a barcode (length 12 string), identify the type of the barcode.

        Args:
            numeric_barcode (str): The barcode to identify.

        Returns:
            str: The type of the barcode.

        Raises:
            ValueError: If the numeric_barcode is invalid.
        """

        # TODO: Implement this method
        first = numeric_barcode[0]
        if first == "0":
            return "product"
        elif first == "1":
            return "coupon"
        elif first == "2":
            return "membership"
        else:
            return None

    def checkout(self) -> float:
        """Given the current cart, calculate the total price of the cart, with the coupon applied and membership applicable. We also need to update the inventory and membership databases.

        Returns:
            float: The total price of the cart.
        """

        # TODO: Implement this method
        total_cost = self.shopping_cart.calculate_total()
        for product in self.shopping_cart.get_items():
            self.store_backend.decrease_product_quantity(product, 1)
        membership = self.shopping_cart.get_membership()
        if membership:
            points_add = float(total_cost * membership.get_points_multiplier())
            self.store_backend.add_member_points(membership, points_add)
        self.store_backend.save_inventory()
        self.store_backend.save_memberships()
        return total_cost

    def get_current_cart(self) -> ShoppingCart:
        # TODO: Implement this method
        return self.shopping_cart



def pos_doctests(self):
    """Function to run the doctests for the POSSystem class.

    Note that you should run this doctest at the root folder of the project
    (same level as main.py)

    It's recommended that you add additional doctests
    or test using by creating scripts like main.py

    >>> pos = POSSystem(
    ...     'db-data/inventory.csv',
    ...     'db-data/memberships.csv',
    ...     'db-data/coupons.csv'
    ... )
    >>> pos.process_barcodes('cart-data/scan_1_binary.txt')
    >>> cart = pos.get_current_cart()
    >>> items = cart.get_items()
    >>> len(items) == 2
    True
    >>> item_names = [item.get_name() for item in items]
    >>> 'Apple' in item_names and 'Cheddar Cheese' in item_names
    True
    >>> cart.get_membership().get_name() == 'John Smith'
    True
    >>> cart.get_membership().return_membership_type() == 'Gold'
    True
    >>> import math
    >>> math.isclose(pos.checkout(), 0.415, abs_tol=0.001)
    True
    >>> updated_memerships_exists = False
    >>> try:
    ...     f = open('db-data/updated_memberships.csv')
    ...     f.close()
    ...     updated_memerships_exists = True
    ... except FileNotFoundError:
    ...     updated_memerships_exists = False
    >>> updated_memerships_exists
    True
    >>> updated_inventory_exists = False
    >>> updated_inventory_exists = False
    >>> try:
    ...     f = open('db-data/updated_inventory.csv')
    ...     f.close()
    ...     updated_inventory_exists = True
    ... except FileNotFoundError:
    ...     updated_inventory_exists = False
    >>> updated_inventory_exists
    True
    >>> expected_types = ['coupon', 'membership', 'product', 'product']
    >>> calculated_types = []
    >>> with open('cart-data/scan_1.txt', 'r') as f:
    ...     for line in f:
    ...         numeric_barcode = line.strip()
    ...         barcode_type = pos._identify_barcode_type(numeric_barcode)
    ...         calculated_types.append(barcode_type)
    >>> expected_types == calculated_types
    True
    """
