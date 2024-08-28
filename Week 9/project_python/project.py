import re
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from functools import lru_cache
from contractions import contractions
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPES


# Function to create a Spotify client instance using the provided token
def create_spotify_client(token):
    try:
        spotify = Spotify(auth=token)
        user_profile = spotify.current_user()
        print(f"Authenticated as {user_profile['display_name']}")
        return spotify
    except Exception as e:
        print(f"Failed to authenticate: {e}")
        return None


# Caching search results to optimize repeated queries
@lru_cache(maxsize=1000)
def cached_search(query, spotify):
    return spotify.search(q=query, type='track', limit=50)['tracks']['items']


# Function to convert the user's sentence to a standardized format
def standardize_sentence(sentence):
    # Remove punctuation except for apostrophes
    sentence = re.sub(r'[^\w\s\']', '', sentence)
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    # Replace contractions with their expanded forms
    for word, replacement in contractions.items():
        sentence = re.sub(r'\b' + word + r'\b', replacement, sentence)
    return sentence


# Function to create a Spotify playlist based on a given sentence
def create_playlist(sentence, spotify):
    if not sentence:
        return None

    sentence = standardize_sentence(sentence)
    phrases = generate_phrases(sentence.split())

    for phrase_combination in phrases:
        songs = []
        for phrase in phrase_combination:
            song = token_to_song(phrase, spotify)
            if song:
                songs.append(song)

        if songs and len(songs) == len(phrase_combination):
            try:
                playlist = spotify.user_playlist_create(
                    user=spotify.me()['id'],
                    name=sentence,
                    public=True,
                    collaborative=False,
                    description='Have fun with your playlist! Created by @mariahazmir on Github'
                )
                spotify.user_playlist_add_tracks(
                    user=spotify.me()['id'],
                    playlist_id=playlist['id'],
                    tracks=songs
                )
                return playlist['id']
            except Exception as e:
                print(f"Failed to create or add tracks to playlist: {e}")
                return None

    return None


# Function to find a song matching the given token
def token_to_song(token, spotify):
    if token in ['a', 'to', 'the']:
        return None

    if token.lower() == 'and':
        return '5cIZoKmBiFgjabaBG0D9fO'

    banned = []
    query = f"track:{token}"

    for offset in range(0, 1000, 7):
        if banned:
            banned_suffix = " NOT " + " NOT ".join(banned)
            final_query = f"{query}{banned_suffix}"
        else:
            final_query = query

        if len(final_query) > 1000:
            final_query = final_query[:1000]

        try:
            tracks = cached_search(final_query, spotify)
        except Exception as e:
            print(f"Error during search: {e}")
            return None

        if not tracks:
            return None

        for track in tracks:
            if track['name'].lower() == token.lower():
                return track['uri']
            else:
                words = track['name'].split(' ')
                for word in words:
                    if word.lower() != token.lower() and len(banned) < 10:
                        banned.append(word)
                offset = 0
    return None


# Function to generate all possible phrase combinations from a list of words


def generate_phrases(words):
    if isinstance(words, str):
        words = words.split()

    n = len(words)
    phrases = []

    def generate_combinations(start, current_combination):
        if start == n:
            if current_combination:
                phrases.append(current_combination[:])
            return

        for i in range(start, n):
            current_combination.append(' '.join(words[start:i+1]))
            generate_combinations(i + 1, current_combination)
            current_combination.pop()

        if start < n - 1:
            current_combination.append(words[start])
            generate_combinations(start + 1, current_combination)
            current_combination.pop()

    generate_combinations(0, [])
    return phrases


def main():
    # Spotify OAuth2 authentication
    sp_oauth = SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope=SCOPES)

    # Get the authorization URL and ask the user to visit it
    auth_url = sp_oauth.get_authorize_url()
    print(f"Please visit this URL to authorize the application: {auth_url}")

    # After the user authorizes, they will be redirected to the URL with a code
    response = input("Enter the URL you were redirected to: ")
    code = sp_oauth.parse_response_code(response)

    try:
        # Retrieve access token using the authorization code
        token_info = sp_oauth.get_access_token(code)
        access_token = token_info['access_token']
        print(f"Access Token: {access_token}")
    except Exception as e:
        print(f"Error obtaining access token: {e}")
        return

    # Create a Spotify client using the access token
    spotify = create_spotify_client(access_token)
    if not spotify:
        print("Spotify client could not be created. Please check the token and scopes.")
        return

    # Get the user's input sentence
    sentence = input("Enter a sentence to generate a playlist: ")

    # Generate the playlist and output the result
    playlist_id = create_playlist(sentence, spotify)
    if playlist_id:
        print(f"Playlist created! Listen here: https://open.spotify.com/playlist/{playlist_id}")
    else:
        print("Sorry, we couldn't generate a playlist. Please try a different sentence.")


if __name__ == "__main__":
    main()

