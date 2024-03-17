# Computing ID: vgs3qt
# Name: Zhiyuan Chang

# [movie name, gross earning, year, rating out of 10, number of ratings]

def get_name(movie):
    """
    The get_name function should return the name in the provided list.
    :param movie: provided list.
    :return: name
    """
    name = movie[0]
    return name


def get_gross(movie):
    """
    The get_gross function should return the gross earnings in the provided list.
    :param movie: provided list
    :return: the gross earnings
    """
    gross = movie[1]
    return gross


def get_rating(movie):
    """
    The get_rating function should return the rating in the provided list.
    :param movie: provided list
    :return: rating
    """
    rating = movie[3]
    return rating


def get_num_ratings(movie):
    """
    The get_num_ratings function should return the number of ratings in the provided list.
    :param movie: provided list
    :return: the number of ratings
    """
    num = movie[4]
    return num


def better_movies(movie_name, movies_list):
    """
    The better_movies function should take the provided movie_name and search through the
    provided movies_list and return a list of all movies’ information that have a higher
    rating than that of movie_name. Assume that the movie_name given will always be in the provided list.
    :param movie_name: name of the movie you want to compare
    :param movies_list: list of all movies
    :return: all movies and their info if the rating is higher than the one you compared
    """
    better = []
    compare = 0
    for i in range(len(movies_list)):
        a = get_name(movies_list[i])
        if a == movie_name:
            compare = get_rating(movies_list[i])

    for index in range(len(movies_list)):
        b = get_rating(movies_list[index])
        if b > compare:
            better.append(movies_list[index])
    return better


def average(category, movies_list):
    """
    The average function will return the average for all movies based on the provided category. For
    example, if category is equal to “rating”, this function will return the average of all ratings in
    movie_list.
    :param category: the category you want to average
    :param movies_list: list of all movies
    :return: the average value of that category from all movies
    """
    result = 0
    final = 0
    if category == "rating":
        for i in range(len(movies_list)):
            result += get_rating(movies_list[i])
        final = result / int(len(movies_list))
    elif category == "gross":
        for i in range(len(movies_list)):
            result += get_gross(movies_list[i])
        final = result / int(len(movies_list))
    elif category == "number of ratings":
        for i in range(len(movies_list)):
            result += get_num_ratings(movies_list[i])
        final = result / int(len(movies_list))
    return final
