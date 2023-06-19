# This File contains the functions for the communication between the frontend (Client) and the backend (Server).
# The following Communication Channels are implemented:
# - REST API
# - Websocket

# Import of the required packages
import os
import requests
import websocket
import streamlit as st

# Loading of Custom Modules
from functions.help_env import load_env_file


# Function to build the URL for the REST API
def build_url_rest_api() -> str:
    """
    This function builds the URL for the REST API.
    :return: URL for the REST API
    """
    # Load the environment variables
    load_env_file()

    # Get the required environment variables
    SERVER_HOST = os.getenv("SERVER_HOST")
    SERVER_PORT = os.getenv("SERVER_PORT")
    API_ENTRYPOINT = os.getenv("API_ENTRYPOINT")

    # Return the URL
    return f"https://{SERVER_HOST}:{SERVER_PORT}/{API_ENTRYPOINT}/"


# Function to send a request to the REST API

def send_request_rest_api(request_type: str, request_data: dict = None, api_path: str = "") -> dict:
    """
    This function sends a request to the REST API.
    :param request_type: Type of the request
    :param request_data: Data of the request
    :param api_path: Path of the API
    :return: Response of the request
    """
    # Build the URL
    url_api_base = build_url_rest_api()
    url_api = url_api_base + api_path

    # Send the request
    response = requests.request(request_type, url_api, json=request_data)

    # Return the response
    return response.json()
