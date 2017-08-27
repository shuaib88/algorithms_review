def does_movielist_have_flight_length_movies(movie_lengths, flight_length):
    # limitation is if there are two movies with the same length,

    movie_dict = {}

    for movie in movie_lengths:
        movie_dict[movie] = {}

    for movie in movie_lengths:
        needed_length = flight_length - movie
        if needed_length in movie_dict:
            return True

    return False

def does_movielist_have_flight_length_movies(movie_lengths, flight_length):
    # limitation is if there are two movies with the same length,

    movie_dict = {}

    for movie in movie_lengths:
        needed_length = flight_length - movie
        if needed_length in movie_dict:
            return True

        movie_dict[movie] = {}
        
    return False


#test values
movie_lengths = [15, 30, 100, 85]
movie_lengths.reverse()
flight_length = 100

#execute
print does_movielist_have_flight_length_movies(movie_lengths, flight_length)
