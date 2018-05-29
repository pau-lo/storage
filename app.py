# Movie App


"""
- Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie and 'q' to quit:

This app will do the following:

- Add movies
- See movies
- find movies
- Stop running the program when entered q

"""


movies = []


def menu():
    user_input = input(
        "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")
    while user_input != "q":
        if user_input == "a":
            add_movie()
        elif user_input == "l":
            show_movies()
        elif user_input == "f":
            find_by = input("What property of the movie is that? ")
            looking_for = input("What are you looking for? ")
            movie = find_movie(looking_for, lambda x: x[find_by])
            print(movie or "No movies found.")
        else:
            print("Unknown command-please try again.")
            continue
    user_input = input(
        "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie, and 'q' to quit: ")


def add_movie():
    name = input("Enter the movie name: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    actor = input("Enter the main actor: ")
    writers = input("Enter the movie writers: ")

    movies.append(
        {
            "name": name,
            "director": director,
            "year": year,
            "actor": actor,
            "writers": writers,
        }
    )


def show_movies():
    for movie in movies:
        show_movie_details(movie)


def show_movie_details(movie):
    print(f"Name: {movie['name']}")
    print(f"Director: {movie['director']}")
    print(f"Release year: {movie['year']}")
    print(f"Main Actor: {movie['actor']}")
    print(f"Main Writer: {movie['writers']}")


def find_movie(expected, finder):
    found = []
    for movie in movies:
        if finder(movie) == expected:
            found.append(movie)
    return found


menu()
