import requests
def call_api(url):
  resp = requests.get(url)
  if resp.status_code == 200:
    return resp.json()
  return {}