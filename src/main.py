from fastapi import FastAPI, Request, HTTPException
from starlette.responses import RedirectResponse

import requests

from core import log

app = FastAPI()


@app.post("/hook")
async def hook(request: Request):
    raw_request = await request.body()
    log.info(f'{raw_request=}')
    request_dict = await request.json()
    code = request_dict['data']['installation']['code']
    install_id = request_dict['data']['installation']['uuid']

    if not code or not install_id:
        raise HTTPException(status_code=400, detail="Code or Installation ID not provided")

    url = f'https://sentry.io/api/0/sentry-app-installations/{install_id}/authorizations/'

    payload = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': '',
        'client_secret': '',
    }

    resp = requests.post(url, json=payload)
    data = resp.json()

    token = data.get('token')
    refresh_token = data.get('refreshToken')
    print(f'{token=} {refresh_token=}')
    # ... Securely store the install_id, token and refresh_token in DB ...

    data = requests.put(
        u'https://sentry.io/api/0/sentry-app-installations/{}/'.format(install_id),
        json={'status': 'installed'},
        headers={
            'Authorization': f'Bearer {token}'
        }
    )

    print(f'{data.json()=}')

    return RedirectResponse(url='https://sentry.io/settings/')


@app.get("/alert-rule/options/users/")
async def hook(request: Request):
    return {"reqeust": 'ok'}


@app.get("/alert-rule-settings")
async def hook(request: Request):
    return {"reqeust": 'ok'}
