# Imports
from flask import Flask, render_template, request, url_for
import requests

# Setup the app
app = Flask(__name__)

# Global Variables
title = ""
description = ""
info_link = ""
link_message = ""
book_thumbnail = ""
page_count = ""

# Creating the home page


@app.route("/")
def home():
    return render_template('home.html')

# Creating the main page


@app.route("/main_page", methods=['GET', 'POST'])
def main():
    global title, description, info_link, link_message, book_thumbnail, page_count

    webpage = request.form
    try:
        book_name = str(webpage['bookInp'])
    except:
        book_name = 'Hamlet'
    print(book_name)
    URL = f"https://www.googleapis.com/books/v1/volumes?q={book_name}&download=epub&key=AIzaSyB6-WgaJUKC4uRH-ZIsMtQGmTe8dpi73sU"

    response = requests.get(URL)

    jsonated_response = response.json()

    # print(jsonated_response)

    try:
        title = jsonated_response['items'][0]['volumeInfo']['title']
    except:
        title = "No title found"

    try:
        description = jsonated_response['items'][0]['volumeInfo']['description']
    except:
        description = "No Description Found for this book"

    try:
        book_thumbnail = jsonated_response['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    except:
        book_thumbnail = "Book thumbnail not found"
    try:
        page_count = jsonated_response['items'][0]['volumeInfo']['pageCount']
    except:
        page_count = "Page Count not found"

    try:
        info_link = jsonated_response['items'][0]['volumeInfo']['infoLink']
        link_message = "To Check this book out click on this link"

    except:
        info_link = ""
        link_message = ""

    return render_template("index.html", book_title=title, book_description=description, book_link=info_link, msg=link_message, thumbnail=book_thumbnail, pages=page_count)


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
