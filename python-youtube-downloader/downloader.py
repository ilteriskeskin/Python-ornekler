import youtube_dl


class Downloader:
    def __init__(self):
        self.d1 = youtube_dl.YoutubeDL(self.getOptions())

    def hook(self, d):
        if d['status'] == 'finished':
            print('Done downloading, converting now.')

    def getOptions(self):
        return {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'progress_hooks': [self.hook],
        }

    def startDownloading(self, youtube_url):
        self.d1.download([youtube_url])


downloader = Downloader()

youtube_url = input('Enter Youtube URL: ')
downloader.startDownloading(youtube_url)
