
class MusicLib:
    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            L = arr[:mid]
            R = arr[mid:]

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        return arr

    def MusicNames(self, music_names):
        
        sorted_music_names = self.merge_sort(music_names)

       
        categorized_music = {chr(i): [] for i in range(ord('A'), ord('Z') + 1)}

        
        for name in sorted_music_names:
            first_letter = name[0].upper()
            if first_letter in categorized_music:
                categorized_music[first_letter].append(name)

        return categorized_music

    def paginate_MusicNames(self, categorized_music, page_size=10):
        paginated_music = {}
        for letter, names in categorized_music.items():
            paginated_music[letter] = [names[i:i + page_size] for i in range(0, len(names), page_size)]
        return paginated_music

music_names = [
    "Another One Bites the dust","Bohemian Rhapsody",
    "Stairway to Heaven", "Believer","Despacito","Eye of the Tiger" 
    "Imagine", "Hey Jude", "Smells Like Teen Spirit", 
    "Sweet Child O' Mine", "Black Parade",
    "Purple Haze", "Counting Stars", "Wish You Were Here",
    "Let It Be", "Yesterday", "Come Together",
    "Payphone", "Hey You", "Shine On You Crazy Diamond"
]

music_lib = MusicLib()

categorized_music = music_lib.MusicNames(music_names)

paginated_music = music_lib.paginate_MusicNames(categorized_music, page_size=10)

def print_paginated_music(paginated_music):
    print("Page 1:")
    for letter, pages in paginated_music.items():
        if pages:
            print(f"{letter}:")
            for i in range(len(pages[0])):
                col1 = pages[0][i] if i < len(pages[0]) else ""
                print(f"    {col1}")


print_paginated_music(paginated_music)