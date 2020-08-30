
import os
import datetime
import requests
import sys, cgitb
from markdownify import markdownify

def timestamp():
    return '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())

def create_log_record(error = False):
    data = {"records": [
        {
          "fields": {
            "date": timestamp(),
            "app_name": "love_you_mom",
            "notes": "Message sent" if not error else create_trace()
          }
        }]}
    
    return data

def create_trace():
    trace = cgitb.html(sys.exc_info())
    trace = markdownify(trace).strip()
    return trace

def push_log(error = False):
    url = os.environ.get("URL") + os.environ.get("KEY")
    data = create_log_record(error=error)
    requests.post(url, json=data)
