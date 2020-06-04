import requests, io

response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
data = response.json()
#print(data)

'''
for i in data:
	print(i)

events
game_settings
phases
teams
total_players
elements
element_stats
element_types
---------------------------
prints out the following items in events

data["events"]
	id
	name
	deadline_time
	average_entry_score
	finished
	data_checked
	highest_scoring_entry
	deadline_time_epoch
	deadline_time_game_offset
	highest_score
	is_previous
	is_current
	is_next
	chip_plays:[{chip_name:x(bboost,3xc,),num_played:y}]
	most_selected
	most_transferred_in
	top_element
	top_element_info:{id,pts}
	transfers_made
	most_captained
	most_vice_captained

'''
with open(i_sonnet) as my_sonnet:
	for i in data
for i in data["events"]:
	print(i)
	exit()





