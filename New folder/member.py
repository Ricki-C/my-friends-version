class Member:
    """A member of the store."""

    points_multiplier = 1  # 1 point per dollar
    discount_rate = 0  # no discount

    def __init__(self, numeric_barcode: str, name: str, points: float):
        # TODO: Implement this method
        self.barcode = numeric_barcode
        self.name = name
        self.points = float(points)

    def add_points(self, points: float):
        """Add the specified number of points to the member.

        Args:
            points (int): The number of points to add.
        """
        # TODO: Implement this method
        self.points += points

    def get_name(self) -> str:
        """Get the name of the member.

        Returns:
            str: The name of the member.
        """
        # TODO: Implement this method
        return self.name

    def get_points(self) -> int:
        """Get the number of points the member has.

        Returns:
            int: The number of points the member has.
        """
        # TODO: Implement this method
        return self.points

    def get_barcode(self) -> str:
        """Get the barcode of the member.

        Returns:
            str: The barcode of the member.
        """
        # TODO: Implement this method
        return self.barcode

    def get_points_multiplier(self) -> int:
        """Get the points multiplier for the member.

        Returns:
            int: The points multiplier for the member.
        """
        # TODO: Implement this method
        return self.points_multiplier

    def get_discount_rate(self) -> float:
        """Get the discount rate for the member.

        Returns:
            float: The discount rate for the member.
        """
        # TODO: Implement this method
        return self.discount_rate

    def return_membership_type(self) -> str:
        """Return the membership type of the member.

        Returns:
            str: The membership type of the member.
        """
        # TODO: Implement this method
        pass


class SilverMember(Member):
    """A standard member of the store."""
    points_multiplier = 1.1 
    discount_rate = 0.01

    def return_membership_type(self) -> str:
        """Return the membership type of the member.

        Returns:
            str: The membership type of the member.
        """
        # TODO: Implement this method
        return "Silver"


class GoldMember(Member):
    """A gold member of the store."""
    points_multiplier = 1.5
    discount_rate = 0.05

    def return_membership_type(self) -> str:
        """Return the membership type of the member.

        Returns:
            str: The membership type of the member.
        """
        # TODO: Implement this method
        return "Gold"


class PlatinumMember(Member):
    """A platinum member of the store."""
    points_multiplier = 2.0
    discount_rate = 0.10  

    def return_membership_type(self) -> str:
        """Return the membership type of the member.

        Returns:
            str: The membership type of the member.
        """
        # TODO: Implement this method
        return "Platinum"


def member_doctests():
    """Function to run the doctests for the Member class.
    >>> numeric_barcode = '012345678912'
    >>> name = 'David'
    >>> points = 10

    >>> test_member = PlatinumMember(numeric_barcode, name, points)
    >>> test_member.get_barcode() == numeric_barcode
    True
    >>> test_member.get_name() == name
    True
    >>> test_member.get_points() == points
    True
    >>> test_member.get_points_multiplier() == 2
    True
    >>> test_member.get_discount_rate() == 0.1
    True
    >>> test_member.add_points(5)
    >>> test_member.get_points()
    15

    >>> test_silver = SilverMember(numeric_barcode, name, points)
    >>> test_silver.return_membership_type() == 'Silver'
    True
    >>> test_silver.get_points_multiplier() == 1.1
    True
    >>> test_silver.get_discount_rate() == 0.01
    True

    >>> test_gold = GoldMember(numeric_barcode, name, points)
    >>> test_gold.return_membership_type() == 'Gold'
    True
    >>> test_gold.get_points_multiplier() == 1.5
    True
    >>> test_gold.get_discount_rate() == 0.05
    True

    >>> test_plat = PlatinumMember(numeric_barcode, name, points)
    >>> test_plat.return_membership_type() == 'Platinum'
    True
    >>> test_plat.get_points_multiplier() == 2
    True
    >>> test_plat.get_discount_rate() == 0.1
    True
    """