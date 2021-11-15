# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time, cow_status,
  cow_location, season, slurry, grass_status):

  farm_actions_list = ["take cows to cowshed", "milk cows", "fertilize pasture", "mow grass"]

  action_to_perform = ["", "wait", ""]

  if (cow_status == True or grass_status == True or slurry == True) == True and cow_location == "pasture":
    cow_location = "cowshed"
    action_to_perform[0] = farm_actions_list[0]
    action_to_perform[2] = "take cows back to pasture"
    
  if cow_location == "pasture" and weather == "rainy" and time == "night":
    action_to_perform[1] = farm_actions_list[0]
  elif cow_location == "cowshed" and cow_status == True:
    action_to_perform[1] = farm_actions_list[1]
  elif slurry == True and (cow_location == "cowshed" and (weather != "sunny" and weather != "windy")) == True:
    action_to_perform[1] = farm_actions_list[2]
  elif cow_location == "pasture" and (grass_status == True and season == "spring" and weather == "sunny") == True:
    action_to_perform[1] == farm_actions_list[3]

  
  return "\n".join(action_to_perform) if action_to_perform[0] != "" and action_to_perform[2] != "" else action_to_perform[1]

print(farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))