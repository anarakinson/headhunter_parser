from parse_hh import get_page_num, extract_jobs

request_keywords = [
    "python",
    # "go",
    # "rust",
    # "backend",
    "разработчик",
    "junior",
    # "flask",
]

request_text = "+".join(request_keywords)
request = f"https://hh.ru/search/vacancy?text={request_text}&fromSearchLine=true"
print(request)
page_num = get_page_num(request)
print(page_num)

extract_jobs(request, page_num)
