def verify_text(text):
    if text == "":
        raise Exception("Input text required.")
    return text[0].isupper() and text[-1] in '.?")'