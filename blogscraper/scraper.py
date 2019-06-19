import requests
from bs4 import BeautifulSoup
from blogscraper.models import BlogPost, Author
"""
The dictionary below is used to remove polish characters
and assign english letters in authors names
"""
dict={
       'ę':'e',
       'ó':'o',
       'ą':'a',
       'ś':'s',
       'ł':'l',
       'ż':'z',
       'ź':'z',
       'ć':'c',
       'ń':'n',
       }
mainurl = "https://teonite.com/" #used as a base for adding urls to next pages and articles

#returns list of all article urls on page
def articles_on_page(soup):
    article_links=[]
    page_posts = soup.find_all("h2", {"class": "post-title"}) #get all posts on the page
    for post in page_posts:
        article_links.append(mainurl + post.a["href"].replace("../","")) #this line 'generates' full link to the article and adds it to list
    return article_links

#scrapes all the necessary data from the article
def scrape_article(soup, post):
    title = soup.find("h1", {"class": "post-title"})
    author = soup.find("span", {"class":"author-name"}).text

    nickname = author.lower().replace(" ", "")
    for i in dict.keys():
        nickname = str.replace(nickname, i, dict[i])    #replace polish signs and assign standard english letters

    author_name = Author(name=author, nickname=nickname)
    if not Author.objects.all().filter(name=author).exists():   #since we can have multiple articles by the same author, we are checking if this author is already in the database
        author_name.save()

    content = soup.find("div", {"class":"post-content"})

    BlogPost.objects.update_or_create(title=title.text, author=author_name, text=content.text, defaults={
    'title':title.text, 'author':author_name, 'text':content.text})


def find_next_page(soup):
    find_url = soup.find("i", {"class": "fa fa-chevron-right"})    #Looking for an arrow pointing to the next page

    if find_url is not None:
        find_url = find_url.parent
        next_page = find_url.parent.a["href"].replace("../","")
        full_next_page = mainurl + next_page
        return requests.get(full_next_page)
    else:
        return None

def scrape_all():
    page = requests.get("https://teonite.com/blog/") #start from the first blog site
    while page:
        soup = BeautifulSoup(page.content, 'html.parser')

        page_articles = articles_on_page(soup)
        for post in page_articles:
            article = requests.get(post)
            a_soup = BeautifulSoup(article.content, 'html.parser')
            scrape_article(a_soup, post)

        page = find_next_page(soup) #get the next site until function returns None
