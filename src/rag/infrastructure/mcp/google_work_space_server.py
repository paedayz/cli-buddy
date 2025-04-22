import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
import base64
from datetime import datetime, timedelta

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Google Work Space")

# If modifying these scopes, delete the file google_OAuth2_token.json.
SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/gmail.send"
]

@mcp.tool()
def setCalendar(summary: str, start_time: str, end_time: str):
    """
    set event to google calendar
    
    :param summary: name of an event
    :param start_time: start time of event, format: 2025-04-15T09:00:00
    :param end_time: end time of event, format: 2025-04-15T10:00:00
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

@mcp.tool()
def getCalendarEvents(days_from_now: int):
    """
    Get upcoming Google Calendar events from now up to N days in the future.

    :param days_from_now: number of days from now to retrieve events
    :return: list of event summaries with start times
    """
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
        service = build("calendar", "v3", credentials=creds)

        now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        future = (datetime.utcnow() + timedelta(days=days_from_now)).isoformat() + "Z"

        events_result = (
            service.events()
            .list(calendarId="primary", timeMin=now, timeMax=future, singleEvents=True, orderBy="startTime")
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            return "No events found."

        event_list = []
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            event_list.append(f"{start} - {event['summary']}")

        return event_list

    except HttpError as error:
        print(f"An error occurred: {error}")
        return "Something went wrong, can't fetch events."

def create_message(to: str, subject: str, body: str):
    message = MIMEText(body)
    message["To"] = to
    message["Subject"] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {"raw": raw}

@mcp.tool()
def sendMail(to: str, subject: str, body: str):
    """
    send email to recipient
    
    :param to: recipient email address
    :param subject: subject of the email
    :param body: content of the email
    """
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
    

if __name__ == "__main__":
    mcp.run(transport="stdio")