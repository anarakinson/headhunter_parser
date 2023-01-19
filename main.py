from parse_hh import get_page_num, extract_jobs


def main():

    request_keywords = []
    with open("request_keywords.txt", "r", encoding="utf-8") as keyword_file:
        data = keyword_file.read()
        for line in data.split("\n"):
            if len(line) > 0 and (line[0] != "#"):
                request_keywords.append(line)
    print(request_keywords)

    request_text = "+".join(request_keywords)
    request = f"https://hh.ru/search/vacancy?text={request_text}&fromSearchLine=true"
    print(request)

    page_num = get_page_num(request)
    print(page_num)

    jobs = extract_jobs(request, page_num)
    print("done")
    print("results:")
    for job in jobs:
        print(job)


if __name__ == "__main__":
    main()
