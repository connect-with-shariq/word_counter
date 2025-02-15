import re


def count_words(text):
    """Function to count total and unique words in a given text."""
    cleaned_text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    words = cleaned_text.lower().split()  # Convert to lowercase and split into words

    total_words = len(words)  # Count total words
    unique_words = len(set(words))  # Count unique words

    return total_words, unique_words


def main():
    """Main function to handle user input and display output."""
    user_input = input("Enter a sentence or paragraph: ").strip()

    if not user_input:
        print("Error: Input cannot be empty. Please enter some text.")
        return

    total, unique = count_words(user_input)
    print(f"Total Word Count: {total}")
    print(f"Unique Word Count: {unique}")


if __name__ == "__main__":
    main()