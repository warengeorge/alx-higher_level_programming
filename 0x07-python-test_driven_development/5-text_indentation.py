#!/usr/bin/python3
"""
    5-text_indentation Module
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after each of this characters
        '.', '?', ':'
        Args:
            text: inital string to work on
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    letters = []
    text_split = []
    new_list = []

    for ch in text:
        letters.append(ch)
        if ch in ['.', '?', ':']:
            text_split.append(''.join(letters))
            letters.clear()

    if letters:
        text_split.append("".join(letters))
    letters.clear()

    for ch in text_split:
        new_list.append(ch.strip(' '))
    text_split.clear()

    for ch in new_list[-1]:
        if ch in ['.', '?', ':']:
            print("\n\n".join(new_list))
            print()
            return

    print("\n\n".join(new_list), end='')
