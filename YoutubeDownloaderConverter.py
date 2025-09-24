import yt_dlp
import subprocess
import requests

print('1. Download video from YouTube\n'
      '2. Download video as MP3\n'
      'Downloading copyrighted YouTube videos is illegal!\n'
      'I am not responsible for your downloads! Go at your own risk')


def desktop_user_name():
    windows_user_name = subprocess.getoutput('whoami')
    return windows_user_name

def mp3_downloader(url,path):
    print('Your music will be saved on desktop!')
    ydl_opts  = {
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '0',
        }],
        'format':'bestaudio/best',
        'outtmpl':'{}/%(title)s.%(ext)s'.format(path),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url,download = True)


def video_downloader(url,path):
    print('Your video will be saved on desktop!')
    ydl_opts ={
        'format':'bestvideo[height<=720]+bestaudio/best',
        'outtmpl': '{}/%(title)s.%(ext)s'.format(path),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(url,download=True)

def main():
    user_choice = int(input('Enter your choice: '))
    letter_list = []
    cmd_user_name = desktop_user_name()
    index = cmd_user_name.find('\\')
    for i in range(index + 1,len(cmd_user_name)):
        user_name = cmd_user_name[i]
        letter_list.append(user_name)
    user = ''.join(letter_list)
    path = 'C:\\Users\\{}\\Desktop'.format(user)
    url = input('Enter your url: ')
    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/117 Safari/537.36'
    }
    response = requests.get(url,headers=header)
    status_code = response.status_code
    if status_code== 200:
        if user_choice ==1 :
            video_downloader(url, path)
        if user_choice ==2:
            mp3_downloader(url,path)

if __name__ == '__main__':
    main()