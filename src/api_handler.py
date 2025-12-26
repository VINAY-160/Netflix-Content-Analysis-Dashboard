import requests

API_KEY = "ee33ca9"   

def get_movie_rating(title):
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("Response") == "True":
            return {
                "imdb_rating": data.get("imdbRating"),
                "imdb_votes": data.get("imdbVotes"),
                "runtime": data.get("Runtime")
            }
        else:
            return None

    except Exception as e:
        print("Error:", e)
        return None


if __name__ == "__main__":
    movie_name = input("Enter the Movie Name: ")
    print(get_movie_rating(movie_name))
