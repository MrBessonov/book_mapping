import folium
import pandas

data = pandas.read_csv("books.txt")
latitude = list(data["latitude"])
longitude = list(data["longitude"])
author = list(data["author"])
title = list(data["title"])
book_genre = list(data["genre"])
html = """<h4>Информация о книге:</h4>
Автор: %s
Название:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
"""


def color_of_markers(genre):
    if genre == "detective":
        return "purple"
    elif genre == "comedy":
        return "orange"
    elif genre == "classic":
        return "red"
    elif genre == "fantasy":
        return "lightblue"
    elif genre == "science fiction":
        return "green"
    elif genre == "adventure":
        return "white"
    elif genre == "horror":
        return "lightgray"
    else:
        return "black"


book_map = folium.Map(location=[51.5, -0.1], size=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="Book_map")
for lt, ln, t, g, a in zip(latitude, longitude, title, book_genre, author):
    iframe = folium.IFrame(html=html % (a, t, t), width=200, height=100)
    fg.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe),
                               icon=folium.Icon(color=color_of_markers(g))))

book_map.add_child(fg)

book_map.save("book_map.html")