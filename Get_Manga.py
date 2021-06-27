import requests
import os
from bs4 import BeautifulSoup

def get_page(text):
    if english:#mangatx
        temp = text.split('-')[1]
        return temp
    else:
        #Manga Name : Chapter X - page x ( Tales Of Demons And Gods: Chapter 270.5 - Page 1)
        temp = text.split(':') #getting Chapter X - page x with temp[1]
        temp2 = temp[1].split('-') # temp2[0] = Chapter X  and temp2[1] = page x
        page = int(temp2[1].strip().split(' ')[1])
        return page

def get_pages(soup):#mangatx
    pages = []
    if english:
        temp = soup.find_all('div',class_ = "page-break no-gaps")
    else:#working for lelscan-vf.com and scan-fr.cc and scan-vf.net
        temp  = soup.find_all('img',class_ = "img-responsive")
    for item in temp:
        try:
            if english:
                page_number = get_page(item.contents[1].attrs['id'])
                url = item.contents[1].attrs["data-src"].strip()
            else:#working for lelscan-vf.com and scan-fr.cc and scan-vf.net
                page_number = get_page(item.attrs['alt'])
                url = item.attrs['data-src'].strip()
            pages.append([page_number,url])
        except:
            pass
    return pages

def get_chapter_list(soup):
    if english:#mangatx
        s = soup.find_all('select',class_ = "selectpicker single-chapter-select")
        result = clean(s[0].contents)
    else:
        #work for lelscan-vf.com and scan-fr.cc and scan-vf.net
        s = soup.find_all('ul',class_ = "dropdown-menu")
        result = clean(s[1].contents)
        result.reverse()
    return result

def clean(list):
    for item in list:
        if item == '\n':
            list.remove('\n')
    return list
english = True
path = "https://mangatx.com/manga/above-all-gods/chapter-1/"
dirName = "Above All Gods"
if not(os.path.exists(dirName)):
    os.mkdir(dirName)

r = requests.get(path)
soup = BeautifulSoup(r.text,'html.parser')
result = get_chapter_list(soup)
print('Found {} chapters !\nThe first is chapter number {}'.format(len(result),result[0].contents[0]))
#print('Found {} chapters !\nThe first is chapter number {}'.format(len(result),result[0].attrs['data-redirect'].split('/')[-1]))
for chapter in result:
    nBroken = 0
    if english:
        url = chapter.attrs['data-redirect']
    else:
        url = chapter.contents[0].attrs['href']
    chapter_number = url.split('/')[-2].lstrip('chapter-')
    print(chapter_number)
    chapter_request = requests.get(url)
    chapter_soup = BeautifulSoup(chapter_request.text,'html.parser')
    pages = get_pages(chapter_soup)
    for page in pages:
        page_url = page[1]
        image = requests.get(page_url)
        if image.status_code==404:
            nBroken += 1
            print("error 404")
        with open(dirName+"/Chapter "+str(chapter_number)+' page '+str(int(page[0])+1)+".png",'wb') as f:
            f.write(image.content)
