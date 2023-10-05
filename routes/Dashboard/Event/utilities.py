from flask import current_app as app
import requests
from flask import session

def get_daftar_event(kode=None):
    if kode == None:
        url = app.config['BACKEND_URL'] + '/event/'
    else:
        url = app.config['BACKEND_URL'] + f'/event/kode/{kode}'
    response = requests.request(
        method='GET',
        url=url,
        headers={
            'Authorization' : f'Bearer {session["user"]["access_token"]}'
        }
    )
    if response.status_code == 200:
        return response.json().get('data')
    else:
        return []

