
from Track import Track
from json_utilz import load, save

class MusicLibrary:
    def __init__(self) -> None:
        self.data = load()

    def create_track(self):
        title = input("Enter Track Title: ")
        artist = input("Enter Track Artist: ")
        album = input("Enter Track Album: ")
        duration = input("Enter Track Duration (mm:ss): ")

        try:
            if "Tracks" not in self.data:
                self.data["Tracks"] = []
            track_id = len(self.data["Tracks"]) + 1  
            new_track = Track(track_id, title, artist, album, duration)
            self.data["Tracks"].append(new_track.to_dict())
            save(self.data)
            print("Track added successfully!")
        except ValueError as e:
            print(f"Error adding track: {e}")

    def display_all_tracks(self):
        if "Tracks" not in self.data or not self.data["Tracks"]:
            print("No tracks found.")
            return
        print ("Tracks:")
        counter = 1
        for track in (self.data["Tracks"]):
            print(f"\t{counter}. {track['title']} by {track['artist']}")
            counter += 1

