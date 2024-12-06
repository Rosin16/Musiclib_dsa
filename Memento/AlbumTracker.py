from Track import Track
from json_utilz import load, save
from sort import MusicLib

class AlbumTracker:
    def __init__(self):
        self.data = load() 
        self.sort_util = MusicLib()

    def get_albums(self):
        if "Albums" not in self.data:
            self.data["Albums"] = {}  
        return self.data["Albums"]

    def display_albums(self):
        albums = self.get_albums()
        if not albums:
            print("No albums found.")
            return
        
        sorted_albums = self.sort_util.merge_sort(list(albums.keys()))
        print("Albums:")
        for idx, album in enumerate(sorted_albums, start=1):
            print(f"{idx}. {album}")

    def display_tracks_by_album(self, album_name):
        albums = self.get_albums()
        if album_name not in albums:
            print(f"No tracks found for album: {album_name}")
            return

        print(f"Tracks in Album '{album_name}':")
        for idx, track in enumerate(albums[album_name], start=1):
            print(f"{idx}. {track['title']} by {track['artist']} ({track['duration']})")

    def add_album(self):
        title = input("Enter Track Title: ")
        artist = input("Enter Track Artist: ")
        album = input("Enter Album Name: ")
        duration = input("Enter Track Duration (mm:ss): ")

        try:
            if "Tracks" not in self.data:
                self.data["Tracks"] = []
            if "Albums" not in self.data:
                self.data["Albums"] = {}

            track_id = len(self.data["Tracks"]) + 1
            new_track = Track(track_id, title, artist, album, duration)
            self.data["Tracks"].append(new_track.to_dict())

            if album not in self.data["Albums"]:
                self.data["Albums"][album] = []
            self.data["Albums"][album].append(new_track.to_dict())

            save(self.data)
            print(f"Track '{title}' added successfully to album '{album}'!")
        except ValueError as e:
            print(f"Error adding track: {e}")
