import requests


def get_ngrok_url(host='localhost', port=4040):
    resp = requests.get(f'http://{host}:{port}/api/tunnels')
    url = resp.json()['tunnels'][0]['public_url']
    if url.startswith('http://'):
        url = url.replace('http:', 'https:')
    return url
