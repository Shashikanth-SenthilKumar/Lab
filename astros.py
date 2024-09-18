import requests
def get_endpoint(endpoint):
    response = requests.get(endpoint)
    resp_dict = response.json()
    return resp_dict
def post_endpoint(endpoint):
    try:
        response = requests.post(endpoint)
        resp_dict = response.json()
        return resp_dict
    except:
         return response.reason