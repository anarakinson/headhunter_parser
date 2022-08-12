import requests
from bs4 import BeautifulSoup

HEADERS = {
    "Host" : "hh.ru",
    "User-Agent" : "Mozilla",
    # "Accept" : "*/*",
    # "Accept-Encoding" : "gzip, deflate, br",
    # "Connection" : "keep-alive",
}

def get_page_num(url):

    response = requests.get(url, headers=HEADERS)
    print(response)

    soup = BeautifulSoup(response.text, "html.parser")

    pages = []
    # pager = soup.find_all("span", {"class" : "pager-item-not-in-short-range"})
    # for page in pager:
    #     pages.append(page.find("a").text)

    pager = soup.find("div", {"class" : "pager"})
    if pager is None:
        return 1

    for page in pager:
        button = page.find_all("a")
        if len(button) > 0:
            pages.append(int(button[0].text))

    if len(pages) == 0:
        return 1
    return sorted(pages)[-1]

class JobInfo():
    def __init__(self, html_code):
        self.title = html_code.find("a").text
        self.company = html_code.find("div", {"class" : "vacancy-serp-item__meta-info-company"}).find("a").text

def extract_jobs(url, num_pages):
    jobs = []
    for page in range(num_pages):
        response = requests.get(f"{url}&page={page}", headers=HEADERS)
        print(response)
        soup = BeautifulSoup(response.text, "html.parser")
        results = soup.find_all("div", {"class" : "serp-item"})
        # print(results)
        for result in results:
            job_info = JobInfo(result)
            print(job_info.title)
            print(job_info.company)
            print()

        break
    return jobs



if __name__ == "__main__":
    request = 'https://hh.ru/search/vacancy?text=python+junior&fromSearchLine=true&customDomain=1'
    page_num = get_page_num(request)
    print(page_num)
    extract_jobs(request, page_num)
