import crawring
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

page = 13323069

while page > 13321069:
    page = str(page)
    url = f"http://movie.naver.com/movie/point/af/list.nhn?st=nickname&sword={page}&target=after"

    with ThreadPoolExecutor(max_workers=3) as excutor:
        excutor.submit(crawring.do_crawl, url)

        page = int(page)
        page -= 1