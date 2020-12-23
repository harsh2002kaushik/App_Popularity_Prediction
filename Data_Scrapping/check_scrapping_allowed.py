
import requests

from bs4 import BeautifulSoup 

r=requests.get("LINK TO THE WEBSITE")

r.status_code
# data can be extracted with ease if it returns 200 else some difficulty might be there
