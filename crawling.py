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


def get_genre_list(url):
  movie_links_list = get_movie_link(url)
  genre_list = []
  for movie_url in movie_links_list:
    print(movie_url)
    res = requests.get(movie_url)
    soup = BeautifulSoup(res.text, 'html5lib')
    genres = soup.find_all('table', class_='info_area')
    for genre in genres:
      genre_list.append(genre.a.get_text())
      print(genre.a.get_text())
  return genre_list
  

url = "http://movie.naver.com/movie/point/af/list.nhn"
movie_links_list = get_genre_list(url)


res = requests.get("http://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=187322&target=after")
content = res.text
soup = BeautifulSoup(content, 'html5lib')
page_links = soup.select('a[href]')
page_link_list = []
for link in page_links:
  if re.search(r'&target=after', link['href']):
    target_url='http://movie.naver.com'+str(link['href'])
    page_link_list.append(target_url)
print(page_link_list)