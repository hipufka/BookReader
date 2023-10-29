import src.model as mo

#TODO: add mode to read from url to html page
#TODO: add other text formats to process - epub, fb2, pdf

# File with text to voice
book = "j_austin_quote_en"

with open(book + ".txt", "r") as text_file:
    data = text_file.read()

mo.text_to_speech(text=data, book_name=book, lang='en')
