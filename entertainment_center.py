import media
import fresh_tomatoes

# for each movie create an instance of the class Movies in a variable that
# stores related movie information. Sources: imdb, wikipedia, youtube.com
the_matrix = media.Movie(
    "The Matrix",
    "Is reality real?",
    "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
    "https://youtu.be/vKQi3bBA1y8", "1999", "Keanu Reeves")

avatar = media.Movie(
    "Avatar",
    "A marine on an alien planet",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://youtu.be/d1_JBMrrYw8", "2009", "Sam Worthington")

inception = media.Movie(
    "Inception",
    "Nested Dreams",
    "https://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
    "https://youtu.be/8hP9D6kZseM", "2010", "Leonardo DiCaprio")

interstellar = media.Movie(
    "Interstellar",
    "Space Adventure",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://youtu.be/zSWdZVtXT7E", "2014", "Matthew McConaughey")

edge_of_tomorrow = media.Movie(
    "Edge of Tomorrow",
    "Live, Die, Repeat",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
    "https://youtu.be/yUmSVcttXnI", "2014", "Tom Cruise")

ex_machina = media.Movie(
    "Ex Machina",
    "Machine becomes (wo)man",
    "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
    "https://youtu.be/EoQuVnKhxaM", "2015", "Alicia Vikander")

transcendence = media.Movie(
    "Trascendence",
    "His soul becomes software",
    "https://upload.wikimedia.org/wikipedia/en/e/ef/Transcendence2014Poster.jpg",
    "https://youtu.be/VCTen3-B8GU", "2014", "Johnny Depp")

memento = media.Movie(
    "Memento",
    "Some memories are best forgotten",
    "https://upload.wikimedia.org/wikipedia/en/c/c7/Memento_poster.jpg",
    "https://youtu.be/0vS0E9bBSL0", "2000", "Guy Pearce")

seven_psychopaths = media.Movie(
    "Seven Psychopaths",
    "Find the nutter",
    "https://upload.wikimedia.org/wikipedia/en/e/e3/Seven_Psychopaths_Poster.jpg",
    "https://youtu.be/jsHR77oQKEY", "2012", "Colin Farrell")

# create an array for each instance above, each element will be iterated through
# and printed to HTML
movies = [the_matrix, avatar, inception, interstellar, edge_of_tomorrow,
          ex_machina, transcendence, memento, seven_psychopaths]

# open the fresh_tomatoes moodule calling the open_movies_page function that
# takes as an argument the movies array
fresh_tomatoes.open_movies_page(movies)
