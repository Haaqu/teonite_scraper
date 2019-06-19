from blogscraper.scraper import scrape_all
"""
This file is used to setup cronjob and execute scrape_all() function once every 5 hours
see: settings.py -> CRONJOBS
"""
def hourly_scraper():
    scrape_all()
