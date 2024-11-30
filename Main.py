from Track import Track
from MusicLibrary import MusicLibrary
from Playlist import Playlist

class main:
    def __init__ (self):
        self.library = MusicLibrary()
        self.playlist = Playlist()

    @staticmethod
    def prompt(args:str) -> str:
        return input(args).lower()

    def main (self):
        while True:
            print ("\n========= WELCOME =========")
            print ("   [P] Open Music Player")
            print ("===========================")
            print ("MENU:\n    1 >> Create new Track\n    2 >> View All Tracks\n    3 >> Create Playlist\n    4 >> View All Playlist\n    0 >> Exit Program")
            choice = main.prompt("\nEnter choice: ")

            if choice == "p":
                while True:
                    print ("\n========= MUSIC PLAYER =========")
                    print ("1 >> Library\n2 >> Playlist\n0 >> Exit main menu")
                    choice = main.prompt("\nEnter choice: ")

                    if choice == '1':
                        pass

                    elif choice == '2':
                        pass

                    elif choice == '0':
                        break
                
            elif choice == '1':
                self.library.create_track()
                print ("\nTrack Successfully Added to the Library!\n")

            elif choice == '2':
                print ("=" * 45)
                print ("\t       Music Library")
                print ("=" * 45)
                self.library.display_all_tracks()
                input("HI :>")

if __name__ == "__main__":
    run = main()
    run.main()