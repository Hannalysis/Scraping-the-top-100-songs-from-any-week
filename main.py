from bs4 import BeautifulSoup
import lxml
import requests
from datetime import date

user_date = input("What date would you like to musically travel back to?: (in YYYY/MM/DD): ")

#Convert the data into a tuple and remove the /
music_date = tuple(map(int, user_date.split('/')))
#Pull out the elements of the tuple and into the datetime class object
convert_date = date(music_date[0], music_date[1], music_date[2])
print(convert_date)

response = requests.get(f"https://www.billboard.com/charts/hot-100/{convert_date}/", headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"})
one_hundred_songs_page = response.text

soup = BeautifulSoup(one_hundred_songs_page,"lxml")

# First song
first_song_name = soup.find(name = "h3", class_ = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet")
first_song = first_song_name.getText().split()

# The other 99 songs
ninety_nine_song_names = soup.find_all(name = "h3", class_ = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")

# First artist
first_artist_name = soup.find(name = "span", class_ = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet")
first_artist = first_artist_name.getText().split()

# The other 99 Artists
ninety_nine_song_artists = soup.find_all(name = "span", class_ = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

song_list = [song.getText().strip("\n\t") for song in ninety_nine_song_names]
# Adding the first song into the list as the first item
song_list.insert(0, first_song[0])
print(song_list)


artist_list = [artist.getText().strip("\n\t") for artist in ninety_nine_song_artists]
artist_list.insert(0, first_artist[0])
print(artist_list)

#List amount checks
print(len(song_list))
print(len(artist_list))

top_one_hundred_songs = dict(zip(artist_list, song_list))
print(top_one_hundred_songs)

i = 1
# Saving as a local txt file
for song in top_one_hundred_songs:
    if i > 1: 
         with open(f"100_Songs_from_{convert_date}.txt", mode = 'a') as file:
            file.write(f"{song}, {top_one_hundred_songs[song]}\n")
    else:
         with open(f"100_Songs_from_{convert_date}.txt", mode = 'w') as file:
            file.write(f"{song}, {top_one_hundred_songs[song]}\n")
            i +=1
