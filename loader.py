import os

from pytube import YouTube, Playlist


class Loader:

    def load_video(self):
        link = input("Enter the YouTube video URL: ")
        path = input('Enter path to download: ')

        if not os.path.exists(path):
            print('Wrong path.\nEnd of path must be directory.\nTry again')
            self.load_video()

        try:
            YouTube(link).streams.get_highest_resolution().download(output_path=path)
            print("Download is completed successfully")

        except:
            print('Something went wrong...')

    def load_playlist(self):
        link = input("Enter the YouTube playlist URL: ")
        path = input('Enter path to download: ')

        if not os.path.exists(path):
            print('Wrong path.\nEnd of path must be directory.\nTry again')
            self.load_playlist()

        try:
            playlist = Playlist(link)
            playlist_len = len(playlist.videos)
            for index, video in enumerate(playlist.videos):
                video.streams.first().download(output_path=path)
                print(f'\r{index + 1}\\{playlist_len}', end='')

            print('\nSuccess!\n')

        except:
            print('Something went wrong...')
