from Track import Track
import json
from datetime import datetime


class MusicLibrary:
    def __init__(self):
        self.tracks = self.load_data()

    def load_data(self):
        with open('store.json', 'r') as file:
            return json.load(file)["tracks"]

    def merge_sort(self, tracks, key):
        if len(tracks) <= 1:
            return tracks

        mid = len(tracks) // 2
        left = self.merge_sort(tracks[:mid], key)
        right = self.merge_sort(tracks[mid:], key)

        return self.merge(left, right, key)
    
    def merge(self, left, right, key):
        sorted_tracks = []

        while left and right:
            comparison = self.compare_tracks(left[0], right[0], key)

            if comparison < 0:
                sorted_tracks.append(left.pop(0))
            elif comparison > 0:
                sorted_tracks.append(right.pop(0))
            else:
                sorted_tracks.append(left.pop(0))  

        sorted_tracks.extend(left)
        sorted_tracks.extend(right)

        return sorted_tracks
    
    def compare_tracks(self, track1, track2, key):
        if track1[key] != track2[key]:
            return (track1[key] > track2[key]) - (track1[key] < track2[key])

        attributes = ['title', 'artist', 'album', 'duration', 'id']  
        for attribute in attributes:
            if track1[attribute] != track2[attribute]:
                return (track1[attribute] > track2[attribute]) - (track1[attribute] < track2[attribute])

        return 0
    
    def display_sorted_tracks(self):
        unique_tracks = []
        seen = set()

        for track in self.tracks:
            track_tuple = (track["title"], track["artist"], track["album"], track["duration"])
            if track_tuple not in seen:
                seen.add(track_tuple)
                unique_tracks.append(track)

        sorted_tracks = self.merge_sort(unique_tracks, key="title")

        print("\nTracks:")
        for track_data in sorted_tracks:
            track = Track.from_dict(track_data)
            print(f"Track: {track.getTitle()}, Artist: {track.getArtist()}, Album: {track.getAlbum()}, Duration: {track.getDuration()}")

    def duration_tracks(self):
        unique_tracks = []
        seen = set()

        for track in self.tracks:
            track_tuple= (track["title"], track["artist"], track["album"], track["duration"])
            if track_tuple not in seen:
                seen.add(track_tuple)
                unique_tracks.append(track)

        total_duration = sum(self.convert_duration_to_seconds(track["duration"]) for track in unique_tracks)

        print(f"\nTotal duration of unique tracks: {total_duration} seconds\n")

    def convert_duration_to_seconds(self, duration):
        """Convert duration in the format 'MM:SS' to seconds."""
        minutes, seconds = map(int, duration.split(":"))
        return minutes * 60 + seconds


if __name__ == "__main__":
    library = MusicLibrary()
    library.display_sorted_tracks()
    library.duration_tracks()

            

  
  