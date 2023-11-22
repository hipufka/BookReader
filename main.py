import src.model as mo

# Change text in quotes to name of file you want to read
BOOK = "frost_and_starlight_excerpt"

with open(BOOK + ".txt", "r") as text_file:
    data = text_file.read()

mo.text_to_speech(text=data, book_name=BOOK, lang='en')

#TODO: add mode to read text from html page
#TODO: add other text formats to process - epub, fb2, pdf
