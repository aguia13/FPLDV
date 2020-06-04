import requests, io




def main():
	response = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
	data = response.json()




if __name__ == '__main__':
	main()