from bs4 import BeautifulSoup
import requests ,csv



try:
    source=requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
    source.raise_for_status()  #Just For Convenience-Used to throw an error for wrong url input

    soup=BeautifulSoup(source.text,'html.parser')

    movies=soup.find('tbody', class_='lister-list').findAll('tr')  #It Gives an Array i.e. We have to use for loop

    
    with open('scrap.csv','w',newline='') as file:
        the_writer=csv.writer(file)
        header=['Rank',"Movie Name","Year","IMDB Ratings"]
        the_writer.writerow(header)
        for movie in movies: 
            name=movie.find('td',class_='titleColumn').a.text
            rank=movie.find('td',class_='titleColumn').get_text(strip=True).split('.')[0]
            year=movie.find('td',class_='titleColumn').span.text.strip('()')
            rating=movie.find('td',class_='ratingColumn imdbRating').strong.text
            row=[rank,name,year,rating]
            the_writer.writerow(row)

except Exception as e: #Just to catch any error from the input URL
    print(e)
    print("Error")