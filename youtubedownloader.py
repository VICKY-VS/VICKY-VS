from pytube import YouTube

video=input("enter the video link :")

yt=YouTube(video)

print(yt.streams[0].title)

#print(yt.streams.all)

stream=yt.streams.filter(resolution="360p",file_extension="mp4").first()

stream.download("youtubeVideo/")