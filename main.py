from flask import Flask
import random

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    # choose a movie by invoking our new function
    movie = get_random_movie()
    tomorrow = get_random_movie()

    # build the response string
    content = "<h1>Movie of the Day</h1>"
    content += "<ul>"
    content += "<li>" + movie + "</li>"
    content += "</ul>"
    
    
    content += "<h1>Tommorrow's Movie</h1>"
    content += "<ul>"
    content += "<li>" + tomorrow + "</li>"
    content += "</ul>"
    return content

    # TODO: pick another random movie, and display it under
    

def get_random_movie():
    # TODO: make a list with at least 5 movie titles
    movies =["The Shawshank Redemption", "The Godfather", "The Godfather, Part II", "The Dark Knight", "12 Angry Men"]
    select = random.randint(0,4)
    return movies [select]
    # TODO: randomly choose one of the movies, and return it
    


app.run()
