from Track import Track
import Main  
import random  

class MusicLibrary:
    def __init__(self, tracks):
        self.tracks = [Track.from_dict(track) for track in tracks]

    def sort_tracks_by_artist(self):
        n = len(self.tracks)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.tracks[j].getArtist().lower() > self.tracks[j + 1].getArtist().lower():
                    self.tracks[j], self.tracks[j + 1] = self.tracks[j + 1], self.tracks[j]

    def get_sorted_tracks(self):
        self.sort_tracks_by_artist()
        return self.tracks

    def display_sorted_tracks(self):
        self.sort_tracks_by_artist()
        print("\nSorted Tracks by Artist Name:")
        for idx, track in enumerate(self.tracks, start=1):
            print(f"{idx}. {track.getTitle()} - {track.getArtist()} ({track.getAlbum()}, {track.getDuration()})")
