import requests
import csv
from bs4 import BeautifulSoup as soup

url_content=requests.get("https://www.amazon.in/gp/bestsellers/books/")

page_content=soup(url_content.content,"html.parser")

itemlist = page_content.findAll('div', attrs={'class':'a-section a-spacing-none aok-relative'})
#print(itemlist[0].prettify())

f = open("in_book.csv","w")
csv_file=csv.writer(f, delimiter =';')
csv_file.writerow(["Name","URL","Author","Price","Number of Ratings","Average Ratings"])
for item in itemlist:
    csv_list=[]
    name = item.find('span', attrs={'class':'zg-text-center-align'})
    nstr = name.find_all('img', alt=True)
    if name is not None:
        csv_list.append(nstr[0]['alt'])
    else:
        csv_list.append("Not available")
    
    ur=item.find('a',attrs={'class':'a-link-normal'})
    if ur is not None:
        csv_list.append("https://www.amazon.in"+ur['href'])
    else:
        csv_list.append("Not Available")
    
    author=item.find('a', attrs={'class':'a-size-small a-link-child'})
    if author is not None:
        csv_list.append(author.string)
    else:
        csv_list.append("Not Available")
    
    price=item.find('span', attrs={'class':'p13n-sc-price'})
    if price is not None:
        csv_list.append(price.string)
    else:
        csv_list.append("Not Available")
    
    num_ratings=item.find('a', attrs={'class':'a-size-small a-link-normal'})
    if num_ratings is not None:
        csv_list.append(num_ratings.string)
    else:
        csv_list.append("Not Available")
    
    avg_ratings=item.find('span', attrs={'class':'a-icon-alt'})
    if avg_ratings is not None:
        csv_list.append(avg_ratings.string)
    else:
        csv_list.append("Not Available")
    
    csv_file.writerow(csv_list)

f.close()
    