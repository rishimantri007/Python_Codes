from collections import Counter

def count_file_stats(filename):
    with open(filename, "r") as f:
        text = f.read()

    # Count lines, words, characters
    lines = text.splitlines()
    words = text.split()
    chars = len(text)

    # Word frequency (case-insensitive, strip punctuation)
    cleaned_words = [w.strip(".,!?").lower() for w in words]
    word_freq = Counter(cleaned_words)

    return len(lines), len(words), chars, word_freq


# Example usage
lines, words, chars, word_freq = count_file_stats("/Users/rishi/Desktop/Workspace/Python_11_Day/Sample.txt")

print(f"Lines: {lines}, Words: {words}, Characters: {chars}")
print("Word Frequency:", word_freq)