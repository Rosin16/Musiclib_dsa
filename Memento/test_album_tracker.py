from AlbumTracker import AlbumTracker

def main():
    tracker = AlbumTracker()

    while True:
        print("\nAlbum Tracker Test Menu:")
        print("1. Display All Albums")
        print("2. Display Tracks in an Album")
        print("3. Add a New Track and Album")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            tracker.display_albums()
        elif choice == "2":
            album_name = input("Enter Album Name: ")
            tracker.display_tracks_by_album(album_name)
        elif choice == "3":
            tracker.add_album()
        elif choice == "0":
            print("Exiting Album Tracker Test. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
