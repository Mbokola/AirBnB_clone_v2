#!/usr/bin/python3
""" 2-do_deploy_web_static """

from fabric.api import env, put, sudo
from os.path import exists

env.hosts = ['100.26.231.64', '107.23.16.147']  # Replace with your server IPs
env.user = 'ubuntu'  # Replace with your SSH username


def do_deploy(archive_path):
    """
    Distribute the archive to web servers and perform deployment.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ on the web servers
        put(archive_path, '/tmp/')

        # Extract archive to /data/web_static/releases/
        filename = archive_path.split('/')[-1]
        folder_name = filename.replace('.tgz', '')
        release_path = f'/data/web_static/releases/{folder_name}/'
        print("Creating directory")
        sudo(f'mkdir -p {release_path}')
        print("Extracting file")
        sudo(f'tar -xzf /tmp/{filename} -C {release_path}')

        # Delete the archive from /tmp/
        print("Deleting /tmp/")
        sudo(f'rm /tmp/{filename}')
        # Move to serving directory
        sudo(f"mv /data/web_static/releases/{folder_name}/web_static/* /data\
/web_static/releases/{folder_name}/")
        sudo(f"rm -rf /data/web_static/releases/{folder_name}/web_static")
        # Delete the current symbolic link
        print("Deleting symlink")
        current_link = '/data/web_static/current'
        sudo(f'rm -f {current_link}')

        # Create a new symbolic link
        print("Creatimg symlink")
        sudo(f'ln -s {release_path} {current_link}')

        return True
    except Exception:
        return False


if __name__ == "__main__":
    result = do_deploy()
    if not result:
        print("Failed")
    else:
        print("Succesful")