import requests
from bs4 import BeautifulSoup




r = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
# will print out the entire html elements for us...so it will look like "inspect"
print(soup.prettify())

# will find all divs with property row
all = soup.find_all("div", {"class": "propertyRow"})

all[0].find("h4", {"class": "propPrice"})

# print(all)
# extracting all prices from h4 div 
for item in all:
    print(item.find("h4",{"class", "propPrice"}).text.replace("\n", "").replace(" ", ""))
    # item.find_all("span",{"class", "propAddressCollapse"}[0].text)
    try:
        item.find("span", {"class", "infoBed"}.find("b").text)
    except:
        # if you cant find the span tag, move on to the next iteration of the loop
        print(None)
    try:
        item.find("span", {"class", "infoSqft"}.find("b").text)
    except:
        # if you cant find the span tag, move on to the next iteration of the loop
        print(None)
    try:
        item.find("span", {"class", "infoValueFullBath"}.find("b").text)
    except:
        # if you cant find the span tag, move on to the next iteration of the loop
        print(None)
    try:
        item.find("span", {"class", "infoValueHalfBath"}.find("b").text)
    except:
        # if you cant find the span tag, move on to the next iteration of the loop
        print(None)
    


