import datetime
import pickle
import os.path
from googleapiclient.discovery import build 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import requests

#creamos una constante que va a ser una ul de nuestra api de google calendar 
SCOPES = ['https://www.googleapis.com/auth/calendar']

#nombre del archivo json que se descargó de google calendari 
CREDENTIALS_FILE = 'credenciales.json'