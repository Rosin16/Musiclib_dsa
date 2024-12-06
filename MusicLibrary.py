# from Track import Track
# import json


# class MusicLibrary:
#     def __init__(self):
#         self.tracks = self.load_data()

#     def load_data(self):
#         with open('store.json', 'r') as file:
#             tracks = json.load(file)["tracks"]
#         for track in tracks:
#             track.setdefault("date_added", "")  

#         return tracks
    
#     def merge_sort(self, tracks, key, tie_breakers=None):
#         if len(tracks) <= 1:
#             return tracks

#         mid = len(tracks) // 2
#         left = self.merge_sort(tracks[:mid], key, tie_breakers)
#         right = self.merge_sort(tracks[mid:], key, tie_breakers)

#         return self.merge(left, right, key, tie_breakers)

#     def merge(self, left, right, key, tie_breakers):
#         sorted_tracks = []
#         i, j = 0, 0

#         while i < len(left) and j < len(right):
#             comparison = self.compare_items(left[i], right[j], key, tie_breakers)
#             if comparison <= 0:
#                 sorted_tracks.append(left[i])
#                 i += 1
#             else:
#                 sorted_tracks.append(right[j])
#                 j += 1

#         sorted_tracks.extend(left[i:])
#         sorted_tracks.extend(right[j:])
#         return sorted_tracks

#     def compare_items(self, item1, item2, primary_key, tie_breakers=None):
#         if item1[primary_key] != item2[primary_key]:
#             return (item1[primary_key] > item2[primary_key]) - (item1[primary_key] < item2[primary_key])

#         if tie_breakers:
#             for tie_key in tie_breakers:
#                 if item1.get(tie_key) != item2.get(tie_key):
#                     return (item1.get(tie_key, "") > item2.get(tie_key, "")) - (item1.get(tie_key, "") < item2.get(tie_key, ""))

#         return (item1.get("date_added", "") > item2.get("date_added", "")) - \
#                (item1.get("date_added", "") < item2.get("date_added", ""))
    
#     def sort_by_date_added(self):
#         tie_breakers = ["title", "artist", "album", "duration"]

#         sorted_tracks = self.merge_sort(self.tracks, key="date_added", tie_breakers=tie_breakers)

#         print("\nTracks sorted by Date Added:")
#         for track_data in sorted_tracks:
#             track = Track.from_dict(track_data)
#             print(f"Track: {track.getTitle()}, Artist: {track.getArtist()}, Album: {track.getAlbum()}, "
#                   f"Duration: {track.getDuration()}, Date Added: {track_data['date_added']}")

#     def display_sorted_tracks(self, key="date_added"):
#         tie_breakers = ["title", "artist", "album", "duration", "date_added"]
#         sorted_tracks = self.merge_sort(self.tracks, key, tie_breakers)

#         print("\nTracks:")
#         for track_data in sorted_tracks:
#             track = Track.from_dict(track_data)
#             print(f"Track: {track.getTitle()}, Artist: {track.getArtist()}, Album: {track.getAlbum()}, "
#                   f"Duration: {track.getDuration()}, Date Added: {track_data['date_added']}")

#     def duration_tracks(self):
#         total_duration = sum(self.convert_duration_to_seconds(track["duration"]) for track in self.tracks)
#         print(f"\nTotal duration of tracks: {total_duration} seconds\n")

#     def convert_duration_to_seconds(self, duration):
#         minutes, seconds = map(int, duration.split(":"))
#         return minutes * 60 + seconds


# if __name__ == "__main__":
#     library = MusicLibrary()
#     library.display_sorted_tracks(key="title")  
#     library.duration_tracks()

import json

class MusicLibrary:
    def __init__(self, data_file="music_library.json"):
        self.data_file = data_file
        self.tracks = self.load_tracks()

    def load_tracks(self):
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file).get('tracks', [])
        except FileNotFoundError:
            return []

    def save_tracks(self):
        with open(self.data_file, 'w') as file:
            json.dump({"tracks": self.tracks}, file, indent=4)

    def create_track(self):
        title = input("Enter track title: ")
        artist = input("Enter artist: ")
        album = input("Enter album: ")
        duration = input("Enter duration (mm:ss): ")

        self.tracks.append({
            "title": title,
            "artist": artist,
            "album": album,
            "duration": duration
        })
        self.tracks = self.merge_sort(self.tracks)
        self.save_tracks()
        print(f"Track '{title}' added to the library.")

    def display_tracks(self):
        if not self.tracks:
            print("No tracks available in the library.")
            return

        print("Tracks in Library (Sorted):")
        for idx, track in enumerate(self.tracks, start=1):
            print(f"{idx}. {track['title']} - {track['artist']} ({track['album']}) [{track['duration']}]")

    def search_tracks(self, keyword):
        results = [track for track in self.tracks if keyword.lower() in track["title"].lower()]
        if not results:
            print("No tracks found matching your search.")
            return

        print("Search Results:")
        for idx, track in enumerate(results, start=1):
            print(f"{idx}. {track['title']} - {track['artist']} ({track['album']}) [{track['duration']}]")

    def merge_sort(self, tracks):
        if len(tracks) <= 1:
            return tracks

        mid = len(tracks) // 2
        left = self.merge_sort(tracks[:mid])
        right = self.merge_sort(tracks[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        sorted_list = []
        while left and right:
            if self.compare_tracks(left[0], right[0]) <= 0:
                sorted_list.append(left.pop(0))
            else:
                sorted_list.append(right.pop(0))
        sorted_list.extend(left or right)
        return sorted_list

    @staticmethod
    def compare_tracks(track1, track2):
        if track1["title"] != track2["title"]:
            return -1 if track1["title"] < track2["title"] else 1
        if track1["artist"] != track2["artist"]:
            return -1 if track1["artist"] < track2["artist"] else 1
        if track1["album"] != track2["album"]:
            return -1 if track1["album"] < track2["album"] else 1
        return -1 if track1["duration"] < track2["duration"] else (1 if track1["duration"] > track2["duration"] else 0)
