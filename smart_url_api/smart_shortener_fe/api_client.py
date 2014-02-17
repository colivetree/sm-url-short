import requests
import json
BASE_API_URL = "http://localhost:8080/api/v1/"
SHORTEN_ENDPOINT ="shorten/"

def get_full_url(short_url):
    r = requests.get(BASE_API_URL+SHORTEN_ENDPOINT+short_url)
    print r.json()
    return r.json()['full_URL']

def get_endpoint_stats():
    return None