import subprocess
import os
import re
import sys


def run(old_ip: str, new_ip: str):
    if os.geteuid() != 0:
        subprocess.call(['sudo', sys.argv[0], 'ec2', 'replace-hosts', old_ip, new_ip])
    else:
        with open ('/etc/hosts', 'r' ) as f:
            content = f.read()
            content_new = re.sub(f'{old_ip}', rf'{new_ip}', content, flags = re.M)

            with open('/etc/hosts', 'w') as f:
                f.write(content_new)
                return "Hosts file updated successfully."
      

