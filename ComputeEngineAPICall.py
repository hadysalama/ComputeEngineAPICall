"""
Created on Sunday 1/19/20 ‏‎11:54:16 PM

@author: Hady S. Salama
Personal Project
"""
from google.oauth2 import service_account
import googleapiclient.discovery
import pprint

# Finally worked by creating a service account after 4 hours of intense digging. This is a general way to access any Ouath2 secured Google API.

# Create variables for the key file and scopes.
SERVICE_ACCOUNT_FILE = 'deep-learning-245721-9eb380c477af.json'
SCOPES = ["https://www.googleapis.com/auth/compute", "https://www.googleapis.com/auth/devstorage.full_control", "https://www.googleapis.com/auth/compute.readonly",
          "https://www.googleapis.com/auth/devstorage.read_only", "https://www.googleapis.com/auth/devstorage.read_write", "https://www.googleapis.com/auth/cloud-platform"]

# Creates credential object for API call.
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Creates compute_engine API object through the build function. build("google-service", "version", credentials=credentials )
compute_engine = googleapiclient.discovery.build(
    'compute', 'v1', credentials=credentials)

# The API's endpoints are used as functions here instead of a raw link.
# Must specify project, zone, and instance just like in the HTTP call.
# https://compute.googleapis.com/compute/v1/projects/deep-learning-245721/zones/us-west1-b/instances/my-fastai-instance/stop
response = compute_engine.instances().stop(
    project='deep-learning-245721', zone="us-west1-b", instance="my-fastai-instance").execute()

# This call lists the instances in your project.
# https://compute.googleapis.com/compute/v1/projects/deep-learning-245721/zones/us-west1-b/instances/my-fastai-instance/list
response = compute_engine.instances().list(
    project='deep-learning-245721', zone="us-west1-b").execute()


pp = pprint.PrettyPrinter(indent=2)
pp.pprint(response)


# Didn't work by creating a 'Ouathlib Flow' because these only worked for web apps and installed applications
# Opens a sign in with google portal in your browser and asks for permission.
"""
from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    'client_secrets.json',
    scopes=['profile', 'email'])

flow.run_local_server()

# Redirect the user to auth_uri on your platform.
auth_uri = flow.authorization_url()


# The user will get an authorization code. This code is used to get the access token.
code = input('Enter the authorization code: ')
flow.fetch_token(code=code)
"""


# Didn't work as a raw http call because Google has an added layer of security on their APIs called OAuth2.
# Tried to add the security information using an HTTP Header. Doesn't work also not recommended by Google.

"""
import requests

headers = {
  "type": "xxxxxxxxx",
  "project_id": "xxxxxxxxx",
  "private_key_id": "xxxxxxxxx",
  "private_key": "xxxxxxxxx"
  "client_email": "xxxxxxxxx",
  "client_id": "xxxxxxxxx",
  "auth_uri": "xxxxxxxxx",
  "token_uri": "xxxxxxxxx",
  "auth_provider_x509_cert_url": "xxxxxxxxx",
  "client_x509_cert_url": "xxxxxxxxx"
}

url = "https://compute.googleapis.com/compute/v1/projects/deep-learning-245721/zones/us-west1-b/instances/my-fastai-instance/start"

headers = {"API-KEY": "xxxxxxxxx"}

r = requests.post(url)

print("Request:")
print(r)
print()

data = r.json

print("Response: ")
print(data)
"""
