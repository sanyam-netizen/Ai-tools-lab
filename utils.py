def is_palindrome(s):
    """Check whether a string is a palindrome.

    Ignores case, spaces and punctuation.

    Args:
        s (str): The text to check.

    Returns:
        bool: True if the text reads the same forwards and backwards.
    """
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def count_words(text):
    """Count the number of words in a piece of text.

    Words are separated by whitespace.

    Args:
        text (str): The text to count words in.

    Returns:
        int: The number of words.
    """
    return len(text.split())


def celsius_to_fahrenheit(c):
    """Convert a temperature from Celsius to Fahrenheit.

    Args:
        c (float): Temperature in degrees Celsius.

    Returns:
        float: Temperature in degrees Fahrenheit.
    """
    return c * 9 / 5 + 32


if __name__ == "__main__":
    print(is_palindrome("Madam"))
    print(count_words("AI tools lab exercise"))
    print(celsius_to_fahrenheit(100))
