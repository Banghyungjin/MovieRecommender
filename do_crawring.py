import crawling_1

from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
# crawring.print_test()

page = 13323069
age=str(page)
url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"

with ThreadPoolExecutor(max_workers=3) as executor:
  executor.submit(crawling_1.do_crawl, url)
  page = int


# while page >13323060 :
#   page=str(page)
#   url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"

#   with ThreadPoolExecutor(max_workers=3) as executor:
#     executor.submit(crawling_1.do_crawl, url)
#     print(page)
#     page = int(page)
#     page -= 1