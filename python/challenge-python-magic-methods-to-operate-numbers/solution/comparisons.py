class MathExpression:
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other: 'MathExpression') -> bool:
        """Determines if two instances of the class are equal.

        Args:
            other (MathExpression): The other MathExpression object to compare with.

        Returns:
            bool: True if the two MathExpression objects are equal, False otherwise.
        """
        return self.value == other.value

    def __ne__(self, other: 'MathExpression') -> bool:
        """Determines if two instances of the class are not equal.

        Args:
            other (MathExpression): The other MathExpression object to compare with.

        Returns:
            bool: True if the two MathExpression objects are not equal, False otherwise.
        """
        return self.value != other.value

    def __lt__(self, other: 'MathExpression') -> bool:
        """Determines if one instance of the class is less than another.

        Args:
            other (MathExpression): The other MathExpression object to compare with.

        Returns:
            bool: True if the current MathExpression object is less than the other MathExpression object, False otherwise.
        """
        return self.value < other.value

    def __le__(self, other: 'MathExpression') -> bool:
        """Determines if one instance of the class is less than or equal to another.

        Args:
            other (MathExpression): The other MathExpression object to compare with.

        Returns:
            bool: True if the current MathExpression object is less than or equal to the other MathExpression object, False otherwise.
        """
        return self.value <= other.value

    def __gt__(self, other: 'MathExpression') -> bool:
        """Determines if one instance of the class is greater than another.

        Args:
            other (MathExpression): The other MathExpression object to compare with.

        Returns:
            bool: True if the current MathExpression object is greater than the other MathExpression object, False otherwise.
        """
        return self.value > other.value

    def __ge__(self, other: 'MathExpression') -> bool:
        """Determines if one instance of the class is greater than or equal to another.

        Args:
            other (MathExpression): The other MathExpression object to compare with.

        Returns:
            bool: True if the current MathExpression object is greater than or equal to the other MathExpression object, False otherwise.
        """
        return self.value >= other.value