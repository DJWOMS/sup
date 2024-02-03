from functools import wraps

from fastapi import HTTPException, status
from src.lib.exceptions import NotFoundError, AlreadyExistError


def error_handler(func):
    @wraps(func)
    async def decorator(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except NotFoundError as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"{e}")
        except (ValueError, AlreadyExistError) as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")
        # except Exception as e:
        #     raise HTTPException(
        #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        #         detail=f"Server Error - {e}"
        #     )

    return decorator
