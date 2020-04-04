from bs4 import BeautifulSoup
import requests

url= 'https://nameless-meadow-64755.herokuapp.com/questions/5cdd8a864d0f6000174e8fd5/solutions'
r=requests.get(url)
data = r.text
soup = BeautifulSoup(data,'html.parser')

filename= "comment.csv"
f= open(filename,"w")
headers="Title_name, author, description\n"
f.write(headers)

contains= soup.find("div",{"class":"show_question"})
climate= contains.find("div",{"class":"ui huge header"}).text
f.write(climate)
info = contains.find("div",{"class":"ui raised main text container segment"})

for comments in info.findAll("div",{"class":"content"}):
    author= comments.find("div",{"class":"author"}).text
    description = comments.find("div",{"class":"text"}).text
    f.write(author+","+description+"\n")

f.close()
    



