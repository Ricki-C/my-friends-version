from datetime import datetime


class Coupon:
    def __init__(
        self,
        numeric_barcode: str,
        expiration_date: datetime,
        min_purchase: float,
        description: str,
    ):
        # TODO: Implement this method
        self.numeric_barcode = numeric_barcode
        self.expiration_date = expiration_date
        self.min_purchase = min_purchase
        self.description = description

    def _is_expired(self) -> bool:
        """Check if the coupon is expired by comparing to current datetime.now()

        Returns:
            bool: True if the coupon is expired, False otherwise.
        """
        # TODO: Implement this method
        return datetime.now() > self.expiration_date

    def discount_amount(self, subtotal: float) -> float:
        """Calculate the discount amount for the coupon.
        This is a placeholder for the actual discount amount. You will need to implement the actual discount amount in the subclasses.

        Args:
            subtotal (float): The subtotal of the cart.
        """

        pass


class PercentDiscountCoupon(Coupon):

    def __init__(
        self,
        numeric_barcode: str,
        expiration_date: datetime,
        min_purchase: float,
        description: str,
        percent_value: float,
    ):
        # TODO: Implement this method
        super().__init__(numeric_barcode, expiration_date, min_purchase,\
 description)
        self.percent_value = percent_value

    def discount_amount(self, subtotal: float) -> float:
        """Calculates the percentage discount to subtract from the subtotal based on the coupon
        Args:
            subtotal (float): The subtotal of the cart
        Returns:
            float: The discount amount
        """

        # TODO: Implement this method
        if super()._is_expired() or subtotal < self.min_purchase:
            return 0
        return min(subtotal * (self.percent_value / 100), subtotal)

class FixedDiscountCoupon(Coupon):

    def __init__(
        self,
        numeric_barcode: str,
        expiration_date: datetime,
        min_purchase: float,
        description: str,
        fixed_value: float,
    ):
        super().__init__(
            numeric_barcode, expiration_date, min_purchase, description
        )
        self.fixed_value = fixed_value  # should be float,

    def discount_amount(self, subtotal: float) -> float:
        """Calculates the fixed amount to subtract from the subtotal based on the coupon

        Args:
            subtotal (float): The subtotal of the cart
        Returns:
            float: The discount amount
        """

        # TODO: Implement this method
        if super()._is_expired() or subtotal < self.min_purchase:
            return 0
        return min(self.fixed_value, subtotal)

def coupon_doctests():
    """Function to run the doctests for the Coupon class.
    >>> barcode = '012345678925'
    >>> expiration_date_not_expired = datetime(2025, 12, 31, 11, 59, 59)
    >>> expiration_date_expired = datetime(2024, 12, 31, 11, 59, 59)
    >>> min_purchase = 20.0
    >>> description = 'This is our tester!'
    >>> percent_value = 15.5
    >>> fixed_value = 30.0
    >>> test_coupon1 = PercentDiscountCoupon(barcode, \
                                expiration_date_expired, \
                                min_purchase, \
                                description, \
                                percent_value)
    >>> test_coupon1._is_expired()
    True
    >>> test_coupon2 = PercentDiscountCoupon(barcode, \
                                expiration_date_not_expired, \
                                min_purchase, \
                                description, \
                                percent_value)
    >>> test_coupon2._is_expired()
    False
    >>> test_percent = PercentDiscountCoupon(barcode, \
                                                expiration_date_not_expired, \
                                                min_purchase, \
                                                description, \
                                                percent_value)
    >>> test_percent.discount_amount(200.0)
    31.0
    >>> test_percent.discount_amount(15.0)
    0
    >>> test_fixed = FixedDiscountCoupon(barcode, \
                                            expiration_date_not_expired, \
                                            min_purchase, \
                                            description, \
                                            fixed_value)
    >>> test_fixed.discount_amount(200.0)
    30.0
    >>> test_fixed.discount_amount(20.0)
    20.0
    >>> test_fixed.discount_amount(10.0)
    0
    """
