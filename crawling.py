import requests
from bs4 import BeautifulSoup
import re

def get_movie_link(url):
  res = requests.get(url)
  soup = BeautifulSoup(res.text, 'html5lib')

  movie_links = soup.select("a[href]")

  movie_links_list = []
  for link in movie_links:
    if re.search(r'st=mcode&sword' and r'&target=after', link['href']):
      target_url = url + str(link['href'])
      movie_links_list.append(target_url)
  return movie_links_list

url = "http://movie.naver.com/movie/point/af/list.nhn"
movie_links_list = get_movie_link(url)
for movie_link in movie_links_list:
  res = requests.get(movie_link)
  soup = BeautifulSoup(res.text, 'html5lib')
  genres = soup.find_all('#old_content > div.choice_movie_box > div.choice_movie_info > table > tbody > tr:nth-child(1) > td > a:nth-child(1)')
  print(movie_link, genres)
  for genre in genres:
    print(genre)  
  
