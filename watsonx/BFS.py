from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


def findWords(board, words):
    # Initialize result list
    result = []

    # Iterate through the words
    for word in words:
        # Initialize current word as an empty string
        current_word = ""

        # Iterate through the characters in the board
        for row in board:
            # For each character in the row, check if it matches the next character in the current word
            if row[0] == row[1]:
                # If it does, add the character to the current word
                current_word += row[0]
            else:
                # If it doesn't, start a new word
                current_word += row[0]

        # Check if the current word is valid
        if len(current_word) == len(set(current_word)):
            # If it is, add it to the result list
            result.append(current_word)

    return result
