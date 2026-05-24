import os
from datetime import datetime
import time
import shutil
import sys

DAYS_OLD = 30
SOURCE_FOLDER = "files"
ARCHIVE_FOLDER = "archive"


def check_folders():
    if not os.path.isdir(SOURCE_FOLDER):
        print("ERROR: Source folder not found")
        sys.exit(1)
    if not os.path.isdir(ARCHIVE_FOLDER):
        os.makedirs(ARCHIVE_FOLDER, exist_ok=True)


def get_file_age(filepath):
    age_in_days = (time.time() - os.path.getmtime(filepath)) / 86400
    return age_in_days

def archive_file(filepath, filename):
    try:
        shutil.move(filepath, ARCHIVE_FOLDER)
        print(f"Archived: {filename}")
        with open("ArchiveLog.txt", "a") as f:
            f.write(f"{datetime.now()} - Moved {filename} to {ARCHIVE_FOLDER}\n")
    except FileNotFoundError:
        print("File/Folder doesn't exist, check path again")
    except Exception as e:
        print(f"ERROR: {e}")

  