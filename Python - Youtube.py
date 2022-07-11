from pytube import YouTube, streams

url = input(str('Insira aqui o URL para download: '))
video = YouTube(url)
stream = video.streams.get_highest_resolution()

stream.download(output_path=r'LOCAL-DE-DOWNLOAD')

print("Download realizado com sucesso!")
