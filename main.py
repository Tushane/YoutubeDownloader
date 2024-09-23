from datetime import date
from datetime import datetime

import pytube
from moviepy.editor import *

my_date = date.today()
my_datetime = datetime(my_date.year, my_date.month, my_date.day)
xbox_chan_url = 'https://www.youtube.com/user/xbox/hub/videos'
ps_chan_url = 'https://www.youtube.com/c/PlayStation/videos'
hchan = 'https://www.youtube.com/c/Halo/videos'
apex = 'https://www.youtube.com/c/playapex/videos'

#print(xbox_chan_url)
#chan = pytube.Channel(xbox_chan_url)
#print(chan)
#for url in chan.video_urls:
url ='https://www.youtube.com/watch?v=m7qjR1S5njU'
yt = pytube.YouTube(url)
print(yt)
if yt.title.find('Trailer') != -1: #& yt.title.find('Halo') != -1:
      # if (yt.publish_date == my_datetime):
    if yt.title.find('Trailer') != -1:
        print('download ' + yt.title)
        video = yt.streams.filter(file_extension='mp4').order_by('resolution').desc().first()
        print(video)
        audio = yt.streams.get_by_itag(140)
        audio.download(r'C:\Users\tusha\Documents\YoutubeDownloads\audio')
        video.download(r'C:\Users\tusha\Documents\YoutubeDownloads\video')

        file_name = video.title.replace('|', '').replace(':', '').replace("'", '').replace('#', '').replace('.','').replace(',', '')

        video_url =fr'C:\Users\tusha\Documents\YoutubeDownloads\video\{file_name}.mp4'
        audio_url =fr'C:\Users\tusha\Documents\YoutubeDownloads\audio\{file_name}.mp4'

        clip = VideoFileClip(video_url)
        audioClip = AudioFileClip(audio_url)

        videoclip = clip.set_audio(audioClip)
        videoclip.write_videofile(fr'C:\Users\tusha\Documents\YoutubeDownloads\output\{file_name}.mp4' ,fps=60)
           # break;
else:
  print('could not download ' + yt.title)
     # break;