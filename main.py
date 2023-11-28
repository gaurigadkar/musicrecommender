import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


client_id = '09767a9dab344ba4bc9407dacbe0847f'
client_secret = '5e579d8d5f1e49fe94332dbd145ef2ac'

# Create a Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def recommend_music(seed_track_id, limit=10):
    recommended_tracks = []


    track_info = sp.track(seed_track_id)
    track_name = track_info['name']
    artist_name = track_info['artists'][0]['name']

    st.subheader(f"Recommendations based on the track: '{track_name}' by {artist_name}")


    recommendations = sp.recommendations(seed_tracks=[seed_track_id], limit=limit)['tracks']

    # Display the recommended tracks
    for idx, track in enumerate(recommendations, 1):
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        st.write(f"{idx}. '{track_name}' by {artist_name}")
        recommended_tracks.append(track['uri'])

    return recommended_tracks


def main():
    st.title("Spotify Music Recommender")
    st.write("Enter a Spotify track ID to get recommendations")

    # Input for seed track ID
    seed_track_id = st.text_input("Seed Track ID")

    # Button to generate recommendations
    if st.button("Generate Recommendations"):
        if seed_track_id:
            recommended_tracks = recommend_music(seed_track_id)
        else:
            st.warning("Please enter a valid Spotify track ID.")

if __name__== '__main__':
    main()