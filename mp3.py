import os
import subprocess

print("Retnox MP3 dönüştürücü programını açtınız.")
print("Spotify şarkısı dönüştürmek istiyorsanız linki yapıştırınız")
print("Spotify üzerinden arama yapıp şarkı indirmek istiyosanız şarkı ismini yazınız")
print("Spotify üzerinden playlist indirmek istiyorsanız linki yapıştırınız")
print("Youtube üzerinden Şarkı indirmek istiyorsanız linki yapıştırınız\n")

link = input("Bir youtube veya spotify linki yada bir arama kriteri giriniz: ")

# Retnox
if 'open.spotify.com' in link and 'playlist' not in link:
    # Retnox
    cmd = f'spotdl download "{link}" --output "{os.path.join(os.environ["USERPROFILE"], "Desktop")}"'
    subprocess.call(cmd, shell=True)
    # Retnox
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    print("Şarkı MP3'e Başarıyla dönüştürüldü ve Desktopa atıldı!")
elif 'open.spotify.com/playlist' in link:
    # Retnox
    cmd = f'spotdl download "{link}" --output "{os.path.join(os.environ["USERPROFILE"], "Desktop", "Retnox MP3 İndirici")}"'
    subprocess.call(cmd, shell=True)
    # Retnox
    songs_folder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop', 'songs')
    print("Playlist Başarıyla Desktop/Retnox MP3 İndirici Klasörüne İndirildi!")
elif 'youtube.com' in link:
    # Retnox
    from pytube import YouTube
    from moviepy.editor import *
    # Retnox
    yt = YouTube(link)
    # Retnox
    download_dir = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
    # Retnox
    stream = yt.streams.filter(only_audio=True).first()
    stream.download(output_path=download_dir)
    # Retnox
    video_file = os.path.join(download_dir, stream.default_filename)
    mp3_file = os.path.splitext(video_file)[0] + '.mp3'
    video_clip = AudioFileClip(video_file)
    video_clip.write_audiofile(mp3_file)
    # Retnox
    os.remove(video_file)
    # Retnox
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    mp3_path = os.path.join(desktop, os.path.basename(mp3_file))
    os.rename(mp3_file, mp3_path)
    print("Şarkı Youtubedan indirilip başarıyla MP3 e dönüştürüldü.")
else:
    # Retnox
    cmd = f'spotdl download "{link}" --output "{os.path.join(os.environ["USERPROFILE"], "Desktop")}"'
    subprocess.call(cmd, shell=True)
    # Retnox
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    print(f'Yaptığınız "{link}" Aramasına Dair Şarkı indirildi!')
    
# Retnox
input("Programi kapatmak için herhangi bir tuşa basınız.")