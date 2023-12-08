import requests
import os

from bs4 import BeautifulSoup
from collections import Counter
#Это из файла!
# i=0
# directory='C:/Users/pyote/Downloads'
# with open('D:/musical/musiclist.txt','w',encoding='UTF-8') as music:
#     for file in os.listdir(directory):
#         if (file[-4::]=='.mp3') or  (file[-4::]=='.mp4'):
#             music.write(file + '\r')
#             i=i+1
#             print(file)
#
#     music.write('Всего было считано : ' + str(i))
# #"\r\n" - ENTER
# #"\r#- тоже ener

#ПАРСИНГ ПЛЕЙЛИСТА ЯНДЕКС МУЗЫКА
url = 'https://music.yandex.ru/users/pyoter.poliakov/playlists/1032'
response= requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
if response.status_code==200:
    print('Успешно!')
    autor = soup.find_all('span', class_='d-track__artists')
    playlist = soup.find('h1', class_='page-playlist__title typo-h1 typo-h1_big')
    name = soup.find_all('a', class_='d-track__title deco-link deco-link_stronger')
    user = soup.find('span', class_='user__info')
    autors_mass=[]
    names_mass=[]
    nameplaylist=playlist.text
    username=user
    dict={}
    i=0
    print('Плейлист:',nameplaylist)
    print('Пользователь:',username)
    for autors in autor:
        autors_mass.append(autors.text)
    for names in name:
        names_mass.append(names.text)
    for i in range(len(names_mass)):
        dict[names_mass[i]]=autors_mass[i]
    for key , value in dict.items():
        print('Трек:',key,' испольнитель(-и):',value)
    with open('C:/Users/Пётр/OneDrive/Рабочий стол/musiclist.txt','w',encoding='utf8') as filemusic:
        filemusic.write('Плейлист:'+ nameplaylist+ '\n')
        for key,value in dict.items():
            filemusic.write(key + '('+ value + ')' + '\n')
            i=i+1
        print('Всего '+str(len(dict.items())))
else:
    print('Что-то пошло не так, статус:',response.status_code)
