# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(film_names):
  films = film_names
  films.sort()
  return films

def won_golden_globe(film_name):
  adjusted_name = film_name.lower()
  winner_movies = ["Jaws", "Star Wars: Episode IV – A New Hope", "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]
  i = 0
  while i < len(winner_movies):
    winner_movies[i] = winner_movies[i].lower()
    i += 1
  has_won = True if adjusted_name in winner_movies else False
  return has_won

def remove_toto_albums(list_to_tidy):
  tidy_list = list_to_tidy
  known_toto_albums = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in between", "35th Anniversary – Live in Poland", "2015: Toto XIV", "Old Is New", "40 Tours Around the Sun", "With a Little Help from My Friends"]
  i = len(tidy_list) - 1
  while i >= 0:
    if tidy_list[i] in known_toto_albums:
      del tidy_list[i]
    i -= 1
  return tidy_list


