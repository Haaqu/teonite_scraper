# Teonite Blog Scraper
This project was created for the purpose of Teonite recrutation process. Main goal of this project is to scrape data from the company blog http://teonite.com/blog and provide stats about authors and most commonly used words.

* Scraper goes through all the blog pages and retrieves information about the title, content and author of every article
* REST API provides stats about 10 most common words on the blog as well as 10 most common words per author.
* The Scraping is executed every 5 hours to keep database updated and be able to provide new stats.

## Great! How can i use this?

### Prerequisites
* `docker` and `docker-compose` must be installed on the system.
For instructions please read the official [Docker Documentation](https://docs.docker.com/)

### How to run it
Open terminal and type
```sh
docker-compose up
```
And that's it!
Please wait about a minute before making any server request for database to be populated.

## Requests and Answers
Server is running at * *localhost:8080* *.
To view 10 most common words use **/stats/**:
```sh
curl http://localhost:8080/stats/
```
You should receive following **response**:
```sh
{
    "data": 175,
    "one": 154,
    "project": 136,
    "time": 135,
    "also": 125,
    "like": 119,
    "us": 116,
    "open": 109,
    "team": 104,
    "work": 103
}
```
To view 10 most common words for specific author use **/stats/{author}/**
```sh
curl http://localhost:8080/stats/kamilchudy/
```
**Response:**
```sh
{
    "software": 17,
    "project": 16,
    "system": 15,
    "development": 15,
    "ultraviolet": 14,
    "team": 13,
    "time": 11,
    "work": 11,
    "new": 11,
    "also": 10
}
```
To get list of available authors use **/authors/**
```sh
curl http://localhost:8080/authors/
```
**Response:**
```sh
{
    "antekmilkowski": "Antek Miłkowski",
    "michalgryczka": "Michał Gryczka",
    "andrzejpiasecki": "Andrzej Piasecki",
    "martakoziel": "Marta Kozieł",
    "jacekchmielewski": "Jacek Chmielewski",
    "lukaszpilatowski": "Łukasz Piłatowski",
    "krystiankur": "Krystian Kur",
    "kamilchudy": "Kamil Chudy",
    "paulinamaludy": "Paulina Maludy",
    "robertolejnik": "Robert Olejnik",
    "jaroslawmarciniak": "Jarosław Marciniak",
    "januszgadek": "Janusz Gądek",
    "krzysztofkrzysztofik": "Krzysztof Krzysztofik"
}
```
## Built With
* [Django](https://www.djangoproject.com/) with [Django Rest Framework](https://www.django-rest-framework.org/)
* [PostgreSQL](https://www.postgresql.org/)
* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) with [Requests](https://2.python-requests.org/en/master/)
* [NLTK](https://www.nltk.org/)
* [Django-crontab](https://github.com/kraiz/django-crontab)
* [Docker](https://www.docker.com/)

## More detailed description
I've used [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [Requests](https://2.python-requests.org/en/master/) for scraping and pulling the data from the website. [NLTK](https://www.nltk.org/) was used to remove stopwords from every article. Without that we would get completely different results. However this doesn't remove punctuation marks, so a simple regex was used to remove them. [Django-crontab](https://github.com/kraiz/django-crontab) is used to create a cronjob that executes scraping function every 5 hours so the data can be updated when new articles show up.

## Contact
If you have any questions regarding this project, feel free to contact me at [alex.fiuk96@gmail.com](alex.fiuk96@gmail.com)
