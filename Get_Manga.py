import requests
import os
from bs4 import BeautifulSoup

def get_page(text,chapter = -1):#seems to be the same format for lelscan-vf.com and scan-fr.cc and scan-vf.net in form
    #Manga Name : Chapter X - page x ( Tales Of Demons And Gods: Chapter 270.5 - Page 1)
    temp = text.split(':') #getting Chapter X - page x with temp[1]
    temp2 = temp[1].split('-') # temp2[0] = Chapter X  and temp2[1] = page x
    page = int(temp2[1].strip().split(' ')[1])
    return page

def get_pages(soup):#working for lelscan-vf.com and scan-fr.cc and scan-vf.net
    pages = []
    tem  = soup.find_all('img',class_ = "img-responsive")
    for item in tem:
        try:
            page_number = get_page(item.attrs['alt'])
            url = item.attrs['data-src'].strip()
            pages.append([page_number,url])
        except:
            pass
    return pages

def get_chapter_list(soup):#work for lelscan-vf.com and scan-fr.cc and scan-vf.net
    s = soup.find_all('ul',class_ = "dropdown-menu")
    result = clean(s[1].contents)
    result.reverse()
    return result

def clean(list):
    for item in list:
        if item == '\n':
            list.remove('\n')
    return list

path = "https://www.lelscan-vf.com/manga/the-gamer/339/1"
r = requests.get(path)
soup = BeautifulSoup(r.text,'html.parser')

result = get_chapter_list(soup)
print('Found {} chapters !\nThe first is chapter number {}'.format(len(result),result[0].contents[0].attrs['href'].split('/')[-1]))
for chapter in result:
    url = chapter.contents[0].attrs['href']
    chapter_number = url.split('/')[-1]
    print(chapter_number)
    chapter_request = requests.get(url)
    chapter_soup = BeautifulSoup(chapter_request.text,'html.parser')
    pages = get_pages(chapter_soup)
    for page in pages:
        page_url = page[1]
        image = requests.get(page_url)
        if image.status_code==404:
            print("error 404")
        with open('Chapter '+str(chapter_number)+' page '+str(page[0])+".png",'wb') as f:
            f.write(image.content)
