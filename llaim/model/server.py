import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class HttpServer:
    def predict(self, data=None):
        print(data)
        raise NotImplementedError

    async def predict_api(self, request: Request) -> JSONResponse:
        # Accessing request data
        request_body = await request.body()

        response_data = self.predict(request_body)
        return JSONResponse(content=response_data)

    def run_http_server(self):
        self.app = FastAPI(
            title="LLAIM Model Server",
            description="LLAIM HTTP Model Server using FastAPI",
        )
        app: FastAPI = self.app

        app.post("/predict")(self.predict_api)

        uvicorn.run(app, host="127.0.0.1", port=8082)


# import asyncio

# import uvicorn
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse


# class HttpServer:
#     def __init__(self):
#         self.version = "0.0.1"

#         self.app = FastAPI(
#             title="LLAIM Model Server",
#             description="LLAIM HTTP Model Server using FastAPI",
#         )
#         self.serving_task: Optional[asyncio.Task] = None

#     async def serve(self):
#         app: FastAPI = self.app

#         @app.post("/version")
#         async def predict(request: Request) -> JSONResponse:
#             # Accessing request data
#             request_body = await request.json()

#             return JSONResponse(
#                 {
#                     "Request body": request_body,
#                 }
#             )

#         # serve
#         config = uvicorn.Config(app, host="127.0.0.1", port=8082)
#         server = uvicorn.Server(config)
#         await server.serve()


# if __name__ == "__main__":
#     instance = HttpServer()
#     asyncio.run(instance.serve())
