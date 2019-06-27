import omdb
from omdbapi.movie_search import GetMovie


args =input("Enter movie name")

movie = GetMovie(title= args, api_key='46237dd4')
movie.get_all_data()