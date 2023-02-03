from bs4 import BeautifulSoup
import requests

def movieName(url):
    soup=BeautifulSoup(source.text,'html.parser')

    movies=soup.find('tbody', class_='lister-list').findAll('tr')  #It Gives an Array i.e. We have to use for loop
    for movie in movies:
        name=movie.find('td',class_='titleColumn').a.text
        print(name)
    return 0
def rank(url):
    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody', class_='lister-list').findAll('tr')  #It Gives an Array i.e. We have to use for loop
    for movie in movies:
        rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
        print(rank)
def year(url):

    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody', class_='lister-list').findAll('tr')  #It Gives an Array i.e. We have to use for loop
    
    for movie in movies:
        year=movie.find('td',class_='titleColumn').span.text.strip('()')
        print(year)
    return 0
def rating(url):
    soup=BeautifulSoup(source.text,'html.parser')
    movies=soup.find('tbody', class_='lister-list').findAll('tr')  #It Gives an Array i.e. We have to use for loop
    for movie in movies:
        name=movie.find('td',class_='ratingColumn imdbRating').strong.text
        print(name)
    return 0




try:
    source=requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250')
    source.raise_for_status()  #Just For Convenience-Used to throw an error for wrong url input
    movieName(source) #Calling Function to Scrap Movie Name
    rank(source)  #Calling Funcrion to get Rank
    year(source)    #Calling Function to get Year
    rating(source)



except Exception as e: #Just to catch any error from the input URL
    print(e)
    print("Error")