# Spotify Playlist Creator

This project demonstrates how to automatically create Spotify playlists from predefined track lists using the Spotify API and Python.

## Overview

The Spotify Playlist Creator is a Python script that reads track lists from separate files and creates corresponding private playlists in your Spotify account. It's designed as an educational example to show how to interact with the Spotify API for playlist management.

For an enhanced experience, you can use AI assistants like Claude.ai by Anthropic to generate your pre-defined track lists. Simply provide a list of artists you enjoy, along with a theme and desired BPM progression (increase or decrease throughout the playlist). For example, you might request "Create a playlist with tracks from Bonobo, Tycho, and Four Tet, with a chill electronic theme and gradually increasing BPM." This approach allows for creative and personalized playlist generation before using the script to create the playlist on Spotify.

## Features

- Automatically creates private Spotify playlists
- Reads track lists from separate Python files
- Handles track searching and playlist population
- Keeps track of created playlists to avoid duplication

## Example Playlist

An example playlist file (`example_playlist.py`) is provided to demonstrate the format:

EXAMPLE_PLAYLIST = [
    "Aphex Twin - Xtal",
    "Aphex Twin - Ageispolis",
    "Bonobo - Kerala",
    "Bonobo - Cirrus",
    "Tycho - Awake",
    "Tycho - Division",
    "Anyma - Running",
    "Anyma - Consciousness"
]

To create your own playlists, follow this format in separate Python files within a `playlists/` directory.

## Project Structure

- `create_spotify_playlist.py`: Main script for creating playlists
- `example_playlist.py`: Example playlist file
- `requirements.txt`: List of Python dependencies
- `.env`: File for storing Spotify API credentials (not included in repo)
- `created_playlists.txt`: Keeps track of created playlists (not included in repo, create locally)

## Setup

1. Clone the repository: 

2. Install dependencies:
`pip install -r requirements.txt`

3. Set up a Spotify Developer account and create an app to get your API credentials:

- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
- Create a new app
- Note your Client ID and Client Secret


4. Create a .env file in the project root and add your Spotify API credentials: 

*Do Not Share Your CLIENT_ID or CLIENT_SECRET*

- `SPOTIFY_CLIENT_ID`=your_client_id
- `SPOTIFY_CLIENT_SECRET`=your_client_secret
- `SPOTIFY_REDIRECT_URL`=http://localhost:8888/callback

5. Create a `playlists/` directory and add your playlist files following the format in `example_playlist.py`.


6. Create an empty file named `created_playlists.txt` in the project root:
This file will keep track of playlists that have already been created to avoid duplication. It's ignored by Git to prevent committing user-specific data.

7. Run the script: `python create_spotify_playlist.py`


