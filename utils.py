"""Fancy utils."""


def reverse_string(term: str) -> str:
    """Reverse string util.

    TODO: doctest
    """
    if not term:
        return "please..."

    reverse = ""
    for char in term:
        reverse = char + reverse
    return reverse
