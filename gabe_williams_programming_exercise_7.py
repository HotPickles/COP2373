import re

def get_paragraph():
    #prompts the user to enter paragraph
    print("Enter your paragraph:")
    return input()

def process_sentences(text):
    #shows sentences starting with numbers abd capital letters, requires punctuation and a space to define a sentence
    pat = r'[A-Z0-9].*?[.!?](?= [A-Z0-9]|$)'

    # re.multiline lets the pat detect sentences that end on the end of a line
    # re.dotall lets the sentence criteria to be detected between lines
    sentences = re.findall(pat, text, flags=re.DOTALL | re.MULTILINE)

    #show the user the sentences
    print('Sentences Detected:')
    for sentence in sentences:
        print(sentence.strip())

    #show the user the number of sentences
    print(f"Total number of sentences detected: {len(sentences)}")

def main():
    paragraph = get_paragraph()
    if paragraph:
        process_sentences(paragraph)
    else:
        print("No text entered")

if __name__ == "__main__":
    main()