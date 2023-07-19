import uvicorn
from fastapi import FastAPI


def http_server(route="/predict", method="POST"):
    def decorator(func):
        app = FastAPI()

        method_decorator = getattr(app, method.lower())

        @method_decorator(route)
        async def wrapper():
            return func()

        # Run the FastAPI app with uvicorn
        def run_with_uvicorn(*args, **kwargs):
            uvicorn.run(app, *args, **kwargs)

        # Include the main code inside the decorator
        if __name__ == "__main__":
            # Run the FastAPI app with uvicorn if this module is the main module
            run_with_uvicorn(host="127.0.0.1", port=8000)

    # Return the wrapped function (optional, but usually useful for other purposes)
    return decorator
