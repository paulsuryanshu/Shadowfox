# -*- coding: utf-8 -*-
"""AutoCorrectKeyboard.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ypqZyXoUN-PK1L3eUNpMlIgKipBLeQ26
"""

class AutocorrectKeyboard:
    def __init__(self, vocabulary):
        self.vocabulary = vocabulary

    def edit_distance(self, word1, word2):

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]


        for i in range(len(word1) + 1):
            dp[i][0] = i
        for j in range(len(word2) + 1):
            dp[0][j] = j


        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        return dp[len(word1)][len(word2)]

    def autocorrect(self, word):
        original_case = word
        word = word.lower()
        if word in self.vocabulary:
            return original_case


        min_distance = float('inf')
        closest_word = original_case
        for vocab_word in self.vocabulary:
            distance = self.edit_distance(word, vocab_word)
            if distance < min_distance:
                min_distance = distance
                closest_word = vocab_word

        return closest_word

# Example usage
if __name__ == "__main__":
    vocabulary = {"apple", "banana", "orange", "pear", "peach"}
    autocorrector = AutocorrectKeyboard(vocabulary)

    input_text = "I like to eat appl and banaba."
    corrected_text = " ".join(autocorrector.autocorrect(word) for word in input_text.split())
    print("Original Text:", input_text)
    print("Corrected Text:", corrected_text)