from fastapi import FastAPI

from genai_stack.genai_platform.routers import stack_routes, component_routes
from genai_stack.genai_server.routers import session_routes


app = FastAPI(
    title="GenAI Stack",
    version="0.2.0"
)


"""Add middleware if required."""
# app.middleware()


"""Run Server"""
# to run this file locally, execute:
# uvicorn genai_stack.genai_platform.genai_stack_server:app --reload


"""Connecting all the routers to app."""
app.include_router(stack_routes.router)
app.include_router(component_routes.router)

app.include_router(session_routes.router)

    


