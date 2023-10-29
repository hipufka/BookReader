import src.model as mo

#if __name__ == '__main__':
#TODO: add mode to read from url to html page
#TODO: add other text formats to process - epub, fb2, pdf

# File with text to voice
book = "frost_and_starlight_excerpt"

text_file = open(book + ".txt", "r")
data = text_file.read()
text_file.close()

_ = mo.text_to_speech(text=data, book_name=book, lang='en')