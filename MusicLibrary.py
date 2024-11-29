from Track import Track
import Main  
import random  

def merge_sort(tracks):
    if len(tracks) <= 1:
        return tracks

    mid = len(tracks) // 2
    left = merge_sort(tracks[:mid])
    right = merge_sort(tracks[mid:])

    return merge(left, right)


def merge(left, right):
    sorted_tracks = []
    while left and right:
        if left[0]["album"] < right[0]["album"]:
            sorted_tracks.append(left.pop(0))
        elif left[0]["album"] > right[0]["album"]:
            sorted_tracks.append(right.pop(0))
        else:  
            if left[0]["artist"] <= right[0]["artist"]:
                sorted_tracks.append(left.pop(0))
            else:
                sorted_tracks.append(right.pop(0))

    sorted_tracks.extend(left)
    sorted_tracks.extend(right)

    return sorted_tracks


def display_sorted_tracks():
    data = Main.load_data()  
    tracks = data["tracks"]


    unique_tracks = []
    seen = set()
    for track in tracks:
        track_tuple = (track["title"], track["artist"], track["album"], track["duration"])
        if track_tuple not in seen:
            seen.add(track_tuple)
            unique_tracks.append(track)

    sorted_tracks = merge_sort(unique_tracks)

    print("\nTracks:")
    for track_data in sorted_tracks:
        track = Track.from_dict(track_data)  
        print(
            f"Track: {track.getTitle()}, Artist: {track.getArtist()}, Album: {track.getAlbum()}\n"
        )


display_sorted_tracks()
