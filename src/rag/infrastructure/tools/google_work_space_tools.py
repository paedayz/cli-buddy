from typing_extensions import Annotated, TypedDict

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
import base64

# If modifying these scopes, delete the file google_OAuth2_token.json.
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send"
]

# {
#     "summary": "My Python Event",
#     "colorId": 6,
#     "start": {
#         "dateTime": "2025-04-15T09:00:00",
#         "timeZone": "GMT+07:00",
#     },
#     "end": {
#         "dateTime": "2025-04-15T10:00:00",
#         "timeZone": "GMT+07:00",
#     },
# }
class SetCalendar(TypedDict):
    """set event to google calendar"""
    summary: Annotated[str, ..., "name of an event"]
    start_time: Annotated[str, ..., "start time of event, format: 2025-04-15T09:00:00"]
    end_time: Annotated[str, ..., "end time of event, format: 2025-04-15T10:00:00"]

def setCalendar(summary: str, start_time: str, end_time: str):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file google_OAuth2_token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("google_OAuth2_token.json"):
        creds = Credentials.from_authorized_user_file("google_OAuth2_token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
            "google_credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("google_OAuth2_token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("calendar", "v3", credentials=creds)
        
        event = {
            "summary": summary,
            "colorId": 6,
            "start": {
                "dateTime": start_time,
                "timeZone": "GMT+07:00",
            },
            "end": {
                "dateTime": end_time,
                "timeZone": "GMT+07:00",
            },
        }
        
        service.events().insert(calendarId="primary", body=event).execute()
        return "Event was created sucessfully"

    except HttpError as error:
        print(f"An error occurred: {error}")
        return "somthing went wrong can't set event"

class SendMail(TypedDict):
    """send email to recipient"""
    to: Annotated[str, ..., "recipient email address"]
    subject: Annotated[str, ..., "subject of the email"]
    body: Annotated[str, ..., "content of the email"]

def create_message(to: str, subject: str, body: str):
    message = MIMEText(body)
    message["To"] = to
    message["Subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}

def sendMail(to: str, subject: str, body: str):
    creds = None
    if os.path.exists("google_OAuth2_token.json"):
        creds = Credentials.from_authorized_user_file("google_OAuth2_token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "google_credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("google_OAuth2_token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("gmail", "v1", credentials=creds)
        message = create_message(to, subject, body)
        send_result = service.users().messages().send(userId="me", body=message).execute()
        return f"Email sent successfully: ID {send_result['id']}"
    except HttpError as error:
        print(f"An error occurred: {error}")
        return "something went wrong, can't send email"