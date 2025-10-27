# Name: Garvit
# Student ID: 241ADB140

def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    char_count = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()
    return (char_count, word_count, contains_python)

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    char_count, word_count, contains_python = analyze_sentence(sentence)
    print(f"Total characters: {char_count}")
    print(f"Total words: {word_count}")
    print(f"Contains 'Python': {contains_python}")
