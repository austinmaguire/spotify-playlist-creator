"""
Spotify Playlist Creator

This script automatically creates Spotify playlists from predefined track lists
stored in separate files within the 'playlists' directory.
"""

import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import importlib
import sys

# Load environment variables from .env file
load_dotenv()

# Set up Spotify API authentication
SCOPE = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))

def read_created_playlists():
    """Read the list of already created playlists from a file."""
    created = set()
    try:
        if os.path.exists('created_playlists.txt'):
            with open('created_playlists.txt', 'r') as f:
                for line in f:
                    name = line.strip()
                    created.add(name)
                    created.add(name.replace(' ', '_').lower())  # Add lowercase version with underscores
    except IOError:
        print("Error reading created_playlists.txt")
    return created

def write_created_playlist(playlist_name):
    """
    Write a newly created playlist name to the file.
    
    Args:
        playlist_name (str): The name of the playlist to be recorded.
    """
    with open('created_playlists.txt', 'a') as f:
        f.write(playlist_name + '\n')
        f.write(playlist_name.replace('_', ' ').title() + '\n')

def create_playlist(name, description, tracks):
    """
    Create a new Spotify playlist and add tracks to it.

    Args:
        name (str): The name of the playlist.
        description (str): A description for the playlist.
        tracks (list): A list of track names to add to the playlist.
    """
    # Create a new playlist
    playlist = sp.user_playlist_create(sp.me()['id'], name, public=False, description=description)
    
    # Search for each track and prepare to add it to the playlist
    track_ids = []
    not_found = []

    for track in tracks:
        result = sp.search(q=track, type='track', limit=1)
        if result['tracks']['items']:
            track_ids.append(result['tracks']['items'][0]['id'])
        else:
            not_found.append(track)

    # Add all found tracks to the playlist in one request
    if track_ids:
        sp.playlist_add_items(playlist['id'], track_ids)

    # Print summary of playlist creation
    print(f"Playlist '{name}' created successfully with {len(track_ids)} tracks.")
    if not_found:
        print("The following tracks were not found:")
        for track in not_found:
            print(f"- {track}")
    
    # Record the newly created playlist
    write_created_playlist(name)

def get_new_playlists():
    """
    Identify and import new playlists from the 'playlists' directory.

    Returns:
        list: A list of tuples containing (playlist_name, tracks) for new playlists.
    """
    created_playlists = read_created_playlists()
    new_playlists = []

    # Add the 'playlists' directory to the Python path
    playlists_dir = os.path.join(os.path.dirname(__file__), 'playlists')
    sys.path.append(playlists_dir)

    # Iterate through playlist files in the directory
    for filename in os.listdir(playlists_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            playlist_name = filename[:-3]  # Remove '.py' extension
            formatted_name = playlist_name.replace('_', ' ').title()
            if playlist_name.lower() not in created_playlists and formatted_name not in created_playlists:
                module = importlib.import_module(playlist_name)
                playlist_variable = getattr(module, playlist_name.upper())
                new_playlists.append((playlist_name, playlist_variable))

    return new_playlists

def main():
    """Main function to orchestrate the playlist creation process."""
    new_playlists = get_new_playlists()

    if not new_playlists:
        print("Script executed, no new playlists found.")
        return

    for playlist_name, tracks in new_playlists:
        print(f"Creating playlist: {playlist_name}")
        create_playlist(
            playlist_name.replace('_', ' ').title(),
            f"A curated playlist of {playlist_name.replace('_', ' ')} tracks",
            tracks
        )

if __name__ == "__main__":
    main()