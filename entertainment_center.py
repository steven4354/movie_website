import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life","https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print (toy_story.storyline)

avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

#print (avatar.storyline)

#avatar.show_trailer()
guardians_of_the_galaxy_vol_2 = media.Movie("Guardians of the Galaxy Vol. 2", "Peter Quill finds his father", "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg", "https://www.youtube.com/watch?v=duGqrYw4usE")

iron_man = media.Movie("Iron Man", "Tony Stark, an industrialist and master engineer, builds a powered exoskeleton and becomes the technologically advanced superhero Iron Man", "https://upload.wikimedia.org/wikipedia/en/thumb/7/70/Ironmanposter.JPG/220px-Ironmanposter.JPG", "https://www.youtube.com/watch?v=8hYlB38asDY")

movies = [iron_man, guardians_of_the_galaxy_vol_2, toy_story, avatar]

fresh_tomatoes.open_movies_page(movies)

#media.Movie.___doc___
#media.Movie.___name___
#media.Movie.___module__
