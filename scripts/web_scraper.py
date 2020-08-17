#import libraries
import requests
from bs4 import BeautifulSoup
import pandas  as pd


url = 'https://www.classcentral.com/subject/programming-and-software-development'

def get_pages(url, number_results):
    pages = []
    pages.append(url)
    total_results = 0
    page_no = 2 #50 results per page 
    while total_results < number_results:
        primary_url = url
        url_extra = '?page='
        mod_url = primary_url + url_extra + str(page_no)
        pages.append(mod_url)
        page_no += 1
        total_results+=50
    return pages

pages = get_pages(url, 1200)

#init data lists
names = []
institutes = []
providers = []
dates = []
reviews = []
ratings = []

def get_reviews(string):
    index = string.find('Reviews')
    review = string[index - 10: index + 10]
    reviews.append(review.strip())
    
def append_institute(institute):
    if institute is not None:
        institutes.append(institute.text.strip())
    else:
        institutes.append(-1)
        
def append_provider(provider):
    if provider is not None:
        providers.append(provider.text.strip())
    else:
        providers.append(-1)
        
def append_date(date):
    if date is not None:
        dates.append(date.text.strip())
    else:
        dates.append('Self Paced')
        
def append_rating(rating):
    if rating is not None:
        ratings.append(rating.text.strip())
    else:
        ratings.append(-1)
        
def append_name(name):
    names.append(name)
    
    
def get_data(pages):
    for page in pages:
        r = requests.get(page)
        soup = BeautifulSoup(r.content, 'html.parser')
        rows = soup.select('tbody tr')

        for row in rows:
            #name
            name = row.select_one('span',{ 'class': 'text-1 line-tight'}).text.strip()
            append_name(name)

            #institute
            institute = row.find('a', {'class': 'color-charcoal small-down-text-2 text-3'})
            append_institute(institute)

            #provider
            provider = row.find('span', {'class': 'hidden medium-up-inline-block'})
            append_provider(provider)

            #date
            date = row.find('td', {'itemprop': 'startDate'})
            append_date(date)

            #reviews
            rev = row.find('span', {'class': 'large-down-hidden block line-tight text-4 color-gray'})
            string = str(rev)
            get_reviews(string)

            #rating
            rating = row.find('span', attrs = {'class': 'xlarge-up-hidden color-charcoal text-center'})
            append_rating(rating)
            
    df = pd.DataFrame({'name': names,
                         'institute': institutes,
                         'provider': providers,
                         'date': dates,
                         'review': reviews,
                         'rating': ratings})
    return df

programming_df = get_data(pages)
