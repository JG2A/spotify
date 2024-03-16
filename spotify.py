import requests
import json

CLIENT_ID = "8972d6fff6634b039fadd96d3b5bb42d"
CLIENT_SECRET = "ed708dbf70ae4af585e206040125a1e6"

AUTH_URL = "https://accounts.spotify.com/api/token"

# POST
auth_response = requests.post(
    AUTH_URL,
    {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    },
)

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data["access_token"]

headers = {"Authorization": "Bearer {token}".format(token=access_token)}

# base URL of all Spotify API endpoints
BASE_URL = "https://api.spotify.com/v1/"
print("The purpose of this program is to compare two tracks and determine which one has a higher dancibility\n")
track_name1 = input("Enter the name of a track: ")
print()
artist_name = input("Enter the name of an artist: ")
print()
search_artist = BASE_URL + "search?q=" + artist_name + "&type=artist"
search_track2 = BASE_URL + "search?q=" + track_name1
search_track3 = search_track2 + "%20artist:" + artist_name + "&type=track"
t1 = requests.get(search_track3, headers=headers)
t1 = t1.json()
track_id = t1["tracks"]["items"][0]["id"]
r1 = requests.get(BASE_URL + "audio-features/" + track_id, headers=headers)
r1 = r1.json()
track1Danceability = r1["danceability"]

track_name = input("Enter a track name: ")
print()
artist_name = input("Enter the artist name: ")
print()
search_track1 = BASE_URL + "search?q=" + track_name
search_track = search_track1 + "%20artist:" + artist_name + "&type=track"
t = requests.get(search_track, headers=headers)
t = t.json()
track_id = t["tracks"]["items"][0]["id"]
r = requests.get(BASE_URL + "audio-features/" + track_id, headers=headers)
r = r.json()
track2Danceability = r["danceability"]
print()
if track1Danceability > track2Danceability:
    print(track_name1 + " has a higher danceability than " + track_name)

else: 
    print(track_name + " has a higher danceability than " + track_name1)

print()
print()
