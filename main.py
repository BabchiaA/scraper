from fastapi import FastAPI
import yaml
from fb_scraper import scraper

app = FastAPI()

@app.post('/scrape_fb/')
async def page(url_page : str = "https://www.facebook.com/lequipe.fr" , max_scrolls : int = 3):
    try : 
        email = ''
        password = ''
        scraper(email, password, url_page, max_scrolls)
        return "Success"
    except Exception as e :
        return str(e)