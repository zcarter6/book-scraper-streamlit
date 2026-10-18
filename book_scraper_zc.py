import requests
from bs4 import BeautifulSoup
import streamlit as st

url = 'https://books.toscrape.com/'
response = requests.get(url)
btoscrape = BeautifulSoup(response.text, 'html.parser')

def get_genre():
    links = btoscrape.find('ul', class_= 'nav nav-list').find_all('a')

    genre_dict = {}
    for link in links:
        name = link.text.strip() #only pull text - extra space
        click_link = link['href']
        genre_dict[name] = 'https://books.toscrape.com/' + click_link

    return genre_dict

def user_input(genre_dict):
    try:
        select = st.text_input('Please select a genre to search from.')
        if not select:
            return None
    except ValueError:
        st.error('Please do not enter a number.')
        return None

    if select in genre_dict:
        return genre_dict[select]
    else:
        st.write('Genre not found.')
        return None
    
def scrape_books(genre_selected, keyword, rating):
    results = []
    current_url = genre_selected
    while current_url:
        page = requests.get(current_url)
        Bsoup = BeautifulSoup(page.text, 'html.parser')
        books = Bsoup.find_all('article', class_='product_pod')
        for book in books:
            title = book.find('h3').a['title']
            price = book.find('p', class_='price_color').text.strip()
            rating_star = book.find('p', class_='star-rating')['class'][1]
            rating_number = rating[rating_star]
            if keyword.lower() in title.lower():
                results.append({'title':title, 'price': price, 'rating':rating_number})
        next_1 = Bsoup.find('li', class_='next')
        if next_1:
             next_href = next_1.find('a')['href']
             base = current_url.rsplit('/', 1)[0]#split url to add next href for page 
             current_url = base + '/' + next_href
        else:
             current_url = None
    return results

def keyword_search(genre_selected):
    keyword = st.text_input('Enter a keyword to search')
    rating = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
    results = []
    if st.button('Search'):
        def book_rating(book):
            return book['rating']
        results = scrape_books(genre_selected, keyword, rating)
        results = sorted(results, key=book_rating, reverse = True) #sort by rating
        if len(results) == 0:
            st.write('Not found.')
        else:
            st.write(f'Found {len(results)} books:')
            for book in results:
                st.write(f'{book['title']} | {book['rating']}/5 | {book['price']}')
            with open('results.txt', 'a', encoding='utf-8') as file: #utf-8 fixed encoding error giving access to more symbols, append not write so it dosent rewrite saved info
                file.write('Here are your results!\n ')
                for book in results:
                    file.write(f"Title: {book['title']} | Price: {book['price']} | Rating: {book['rating']}/5\n")
    return None

genre_dict = get_genre()
genre_selected = user_input(genre_dict)
if genre_selected:
    keyword_search(genre_selected)


        
