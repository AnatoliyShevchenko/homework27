from flask import Flask
import urllib.request
import json
import requests
from requests.models import Response


app = Flask(__name__)

url = "https://www.freetogame.com/api/games?platform=pc"
r: Response = requests.get(url)
data = r.json()
_list_of_games = []
for element in data:
    _list_of_games.append(element.get("title"))


_my_favorite_games = ["Witcher 3", "Forza Horizon 4", "Darksiders", "Devil May Cry", "Doom", "Divinity: Original Sin 2", "Halo", "Need For Speed: Underground", 
"Need For Speed: Most Wanted", "Need For Speed: Hot Pursuit", "Tomb Rider"]
_my_favorite_films = ["The Lord Of The Rings", "Harry Potter", "Star Wars", "Count of Monte Cristo"]

@app.route('/')
def index():
    return f'<h3>This is the page about my homework</h3>\
        <a href="http://localhost:8085/about">Ссылка на страницу обо мне</a><br>\
            <a href="http://localhost:8085/games">Ссылка на страницу c моими любимыми видеоиграми</a><br>\
            <a href="http://localhost:8085/films">Ссылка на страницу с моими любимыми фильмами</a><br>\
            <a href="http://localhost:8085/all-games">Ссылка на страницу с играми по JSON</a>'
    
@app.route('/about')
def about():
    return f"<p>Hello, my name is Anatoliy. You can call me a Brick. I am thirty years old. I like playing guitar (i own sevenstring guitar), and throw knives, and shoot a bow. \
        Also i like videogames and write a code on a Python, it's my first language and it's amazing.</p>"

@app.route('/games')
def games():
    table = '<center><table border=1><tr><th>Мои любимые видеоигры</th></tr></center>'
    for game in _my_favorite_games:
        table += f'<tr><th>{game}<th></tr>'
    return table

@app.route('/films')
def films():
    table = '<center><table border=1><tr><th>Мои любимые фильмы</th></tr></center>'
    for film in _my_favorite_films:
        table += f'<tr><th>{film}<th></tr>'
    return table

@app.route('/all-games')
def all_games():
    table = '<center><table border=1><tr><th>Все игры по JSON</th></tr></center>'
    for game in _list_of_games:
        table += f'<tr><th>{game}<th></tr>'
    return table
    

if __name__ == "__main__":
    app.run(port=8085, debug=True)