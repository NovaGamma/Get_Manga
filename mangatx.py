def get_name(path):
    return path.split('/')[4]


def get_chapter_list(soup):
    s = soup.find_all('select', class_="selectpicker single-chapter-select")
    result = [item for item in s[0].contents if not (item == '\n' or item == ' ')]
    return clean(result)


def get_chapter_url(chapter):
    return chapter.attrs['data-redirect']


def get_chapter_number(chapter):
    url = get_chapter_url(chapter)
    return url.split('/')[-2].lstrip('chapter-')


def get_page(text):
    return text.split('-')[1]


def get_pages(soup):
    pages = []
    temp = soup.find_all('div', class_="page-break no-gaps")
    for item in temp:
        page_number = get_page(item.contents[1].attrs['id'])
        url = item.contents[1].attrs["data-src"].strip()
        pages.append([page_number, url])
    return pages


def get_headers():
    return {}


def clean(input_list):
    for item in input_list:
        if item == '\n':
            input_list.remove('\n')
    return input_list
