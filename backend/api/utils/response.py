from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def success_response(status_code: int, message: str, data: Optional[dict] = None) -> JSONResponse:
    """
    Returns a JSON response for success responses.

    Parameters:
    - status_code (int): The HTTP status code for the response.
    - message (str): A message to be included in the response.
    - data (Optional[dict], optional): Additional data to be included in the response. Defaults to None.

    Returns:
    - JSONResponse: A FastAPI JSONResponse object containing the success response data.
    """

    response_data = {
        "status_code": status_code,
        "success": True,
        "message": message
    }

    if data is not None:
        response_data["data"] = data

    return JSONResponse(status_code=status_code, content=jsonable_encoder(response_data))

