import requests


def make_post_request(url, body):
    
    return requests.post(url, json=body)
