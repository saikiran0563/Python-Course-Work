movie_id = int(input("Enter Movie ID: "))
movie_title = input("Enter Movie Title: ")
imdb_rating = float(input("Enter IMDB Rating: "))
genres = input("Enter Genres (comma-separated): ").split(",")

duration = int(input("Enter Duration (in minutes): "))
release_year = int(input("Enter Release Year: "))
box_office = float(input("Enter Box Office Collection (in crores): "))

popularity_score = float(input("Enter Popularity Score: "))

actors = set(input("Enter Lead Actors (comma-separated): ").split(","))

director_name = input("Enter Director Name: ")
director_contact = input("Enter Director Contact Number: ")
director_country = input("Enter Director Country: ")

director_details = {
    "name": director_name,
    "contact": director_contact,
    "country": director_country
}

print("\n" + "="*50)
print("NETFLIX MOVIE INFORMATION SUMMARY")
print("="*50)

print("\n1. Using Comma Separation (sep=',')")
print("Movie ID, Title, Rating:", movie_id, movie_title, imdb_rating, sep=",")

print("\n2. Using Percentage Formatting (% operator)")
print("Popularity Score: %.2f%%" % popularity_score)

print("\n3. Using f-strings")
print(f"Movie Title: {movie_title}")
print(f"IMDB Rating: {imdb_rating}")
print(f"Duration: {duration} minutes, Release Year: {release_year}")
print(f"Box Office: ₹{box_office} crores")

print("\n4. Using .format() Method")
print("Director Details: Name - {}, Contact - {}, Country - {}".format(
    director_details["name"],
    director_details["contact"],
    director_details["country"]
))
