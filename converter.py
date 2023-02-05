from pytube import YouTube

def download(link, format):
    try:
        video = YouTube(link)
        if format == 'video':
            video = video.streams.get_highest_resolution()
            print("Video downloading...")
            video.download()
        elif format == 'audio': 
            video = video.streams.get_audio_only()
            print("Audio downloading...")
            video.download()
        else:
            format = input('Please enter a valid format honey\n')
            download(link, format)
        print("Yay, download completed successfully!!")
    except:
        link = input('Enter a valid link sunshine\n')
        download(link, format)

if __name__ == '__main__':
    link = input('Hi love, what video would you like to convert?\n')
    format = input('Would you like that as video or audio?\n').lower() #if empty just do to mp4
    download(link, format)