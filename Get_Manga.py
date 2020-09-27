import requests
import os
from bs4 import BeautifulSoup

'''def get_page(text,chapter = -1):#seems to be the same format for lelscan-vf.com and scan-fr.cc and scan-vf.net in form
    #Manga Name : Chapter X - page x ( Tales Of Demons And Gods: Chapter 270.5 - Page 1)
    temp = text.split(':') #getting Chapter X - page x with temp[1]
    temp2 = temp[1].split('-') # temp2[0] = Chapter X  and temp2[1] = page x
    page = int(temp2[1].strip().split(' ')[1])
    return page'''

def get_page(text):#mangatx
    temp = text.split('-')[1]
    return temp

'''def get_pages(soup):#working for lelscan-vf.com and scan-fr.cc and scan-vf.net
    pages = []
    tem  = soup.find_all('img',class_ = "img-responsive")
    for item in tem:
        try:
            page_number = get_page(item.attrs['alt'])
            url = item.attrs['data-src'].strip()
            pages.append([page_number,url])
        except:
            pass
    return pages'''

def get_pages(soup):#mangatx
    pages = []
    temp = soup.find_all('div',class_ = "page-break no-gaps")
    for item in temp:
        try:
            page_number = get_page(item.contents[1].attrs['id'])
            url = item.contents[1].attrs["data-src"].strip()
            pages.append([page_number,url])
        except:
            pass
    return pages

'''def get_chapter_list(soup):#work for lelscan-vf.com and scan-fr.cc and scan-vf.net
    s = soup.find_all('ul',class_ = "dropdown-menu")
    result = clean(s[1].contents)
    result.reverse()
    return result'''

def get_chapter_list(soup):#mangatx
    s= soup.find_all('select',class_ = "selectpicker single-chapter-select")
    result = clean(s[0].contents)
    return result

def clean(list):
    for item in list:
        if item == '\n':
            list.remove('\n')
    return list

path = "https://mangatx.com/manga/above-all-gods/chapter-1/"
r = requests.get(path)
soup = BeautifulSoup(r.text,'html.parser')

result = get_chapter_list(soup)
print('Found {} chapters !\nThe first is chapter number {}'.format(len(result),result[0].contents[0]))
#print('Found {} chapters !\nThe first is chapter number {}'.format(len(result),result[0].attrs['data-redirect'].split('/')[-1]))
for chapter in result:
    '''url = chapter.contents[0].attrs['href']'''
    url = chapter.attrs['data-redirect']
    chapter_number = url.split('/')[-2].lstrip('chapter-')
    print(chapter_number)
    chapter_request = requests.get(url)
    chapter_soup = BeautifulSoup(chapter_request.text,'html.parser')
    pages = get_pages(chapter_soup)
    for page in pages:
        page_url = page[1]
        image = requests.get(page_url)
        if image.status_code==404:
            print("error 404")
        with open("Above All Gods/Chapter "+str(chapter_number)+' page '+str(int(page[0])+1)+".png",'wb') as f:
            f.write(image.content)
