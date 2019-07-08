import omdb
from omdbapi.movie_search import GetMovie
args =input("Enter movie name")
movie = GetMovie(title= args, api_key='46237dd4')
data = movie.get_all_data()
print(data)
print("Rotten Tomatoes rating :: ",data["Ratings"][1]["Value"])