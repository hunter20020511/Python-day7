def clean_text(text):
    return text.strip().lower()


def replace_words(text):
    replacements = {
        "bad": "good",
        "nice": "nachiket"
    }

    for word, replacement in replacements.items():
        text = text.replace(word, replacement)

    return text


def remove_punctuation(text):
    for ch in ",.!?():;'":
        text = text.replace(ch, "")
    return text


#Pipeline
def process_text(text):
    pipeline = [clean_text, replace_words, remove_punctuation]

    for func in pipeline:
        text = func(text)

    return text


#take input frm user
input_text = input("Type your text for cleaning: ")

#Process the input took from user
output = process_text(input_text)

print("Final Output:", output)