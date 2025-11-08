sentence = "The quick brown fox jumps over the lazy dog"
vowel_count = 0
for letter in sentence:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowel_count += 1
print("Vowel Count:", vowel_count)