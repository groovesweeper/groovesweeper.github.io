import lyricsgenius

if __name__ == "__main__":
    #print("Welcome To GrooveSweeper!")
    '''
    Dict holds exactly
    CLIENT_ID:<ID from genius API>
    CLIENT_SECRET:<secret from Genius API>
    CLIENT_TOKEN:<token from Genius API>
    '''
	
	client_details = {}
	with open("client_details.txt") as f:
		for line in f:
			(key, val) = line.split(":")
			client_details[key] = val

	for key in client_details:
		print(key, ":", client_details[key])