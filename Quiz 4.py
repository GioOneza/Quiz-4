import bs4
from bs4 import BeautifulSoup
import  requests
import  csv


url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
r = requests.get(url)
print(r)
print(r.status_code)
content = r.text
soup = BeautifulSoup(content, 'html.parser')




img_file = open('img1', 'wb')

soup_title= soup.findAll("h2",{"class":"title"})
len(soup_title)
for x in range(5):
   print(soup_title[x].a['href'])
for x in range(5):
   print(soup_title[x].a['title'])


print(soup.title)
print(soup.a)


f = open("data.csv", "a")
write_obj = csv.writer(f)
write_obj.writerow(["The Shawshank Redemption", "9.2"])