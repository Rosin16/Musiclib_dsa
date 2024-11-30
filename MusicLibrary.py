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

  