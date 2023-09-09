#!/usr/bin/python3
""" 1-pack_web_static module """

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a .tgz archive from the web_static folder.
    """
    try:
        # Create the 'versions' directory if it doesn't exist
        local("mkdir -p versions")

        # Generate the archive name using the current date and time
        now = datetime.now()
        archive_name = f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"

        # Use the tar command to create the .tgz archive
        local(f"tar -czvf versions/{archive_name} web_static")

        # Return the archive path if successful
        return f"versions/{archive_name}"
    except Exception:
        return None


if __name__ == "__main__":
    result = do_pack()
    if result:
        print(f"Archive created: {result}")
    else:
        print("Archive creation failed.")
