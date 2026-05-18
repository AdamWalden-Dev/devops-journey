from datetime import datetime
import sys
import os
import psutil


def get_timestamp():
    timestamp = datetime.now()
    print(f"{timestamp: %B %d, %Y  %I:%M:%S}")

get_timestamp()