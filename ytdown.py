from pytube import YouTube
form sys import atgv 

link = argv[1]
yt = YouTube(link)

printf("Titulo: ", yt.title)
printf("Visualizações: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('url')