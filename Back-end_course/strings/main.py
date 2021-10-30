# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#part 1
scorer_goal0 = 'Ruud Gullit'
scorer_goal1 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer_goal0+ " " + str(goal_0) + ", " + scorer_goal1+ " " + str(goal_1)
report = f"{scorer_goal0} scored in the {goal_0}nd minute\n{scorer_goal1} scored in the {goal_1}th minute"

#part 2
player = "Ruud Gullit"
first_name = player[player.find("Ruud"):4]
last_name_len = len(player[player.find("Gullit"):])
name_short = f'{first_name[0]}. {player[player.find("Gullit"):]}'
chant = (f'{first_name}! ' * len(first_name))[:-1]
good_chant = chant[len(chant) - 1] != " "

