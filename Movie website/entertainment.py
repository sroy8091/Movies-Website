import media
import fresh_tomatoes

batman_begins = media.Movie("Batman Begins",
                            "Revenge of a rich boy",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Batman_Begins_Poster.jpg/220px-Batman_Begins_Poster.jpg",
                            "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

dark_knight = media.Movie("The Dark Knight",
                          "Batman has a new foe, the Joker, who is an accomplished criminal hell-bent on decimating Gotham City. Together with Gordon and Harvey Dent, Batman struggles to thwart the Joker before it is too late.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")

rises = media.Movie("The Dark Knight Rises",
                    "Bane, an imposing terrorist, attacks Gotham City and disrupts its eight-year-long period of peace. This forces Bruce Wayne to come out of hiding and don the cape and cowl of Batman again.",
                    "https://upload.wikimedia.org/wikipedia/en/thumb/8/83/Dark_knight_rises_poster.jpg/220px-Dark_knight_rises_poster.jpg",
                    "https://www.youtube.com/watch?v=g8evyE9TuYk")

movies = [batman_begins, dark_knight, rises]

fresh_tomatoes.open_movies_page(movies)
