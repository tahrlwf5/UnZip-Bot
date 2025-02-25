import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5194126976:AAGGCPHBrRoiSjAHzjf57pqW2r1LzcJNkUw")
    API_ID = int(os.environ.get("APP_ID", 14460556 ))
    API_HASH = os.environ.get("API_HASH", "4397b2defe1f3023e5a89e058543d4a9")
    
    
