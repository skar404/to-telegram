from typing import Callable, List

from fastapi import HTTPException
from starlette.responses import JSONResponse

_response_type = Callable[[str], JSONResponse]

ok: _response_type = lambda m: JSONResponse(
    content={'result': m},
    status_code=200
)

bad: _response_type = lambda m: JSONResponse(
    content={'result': 'bad request'},
    status_code=400
)

not_auth: JSONResponse = JSONResponse(
    content={'result': 'unauthorized'},
    status_code=403
)

not_auth_ex: HTTPException = HTTPException(
    detail={'result': 'unauthorized'},
    status_code=403,
)
