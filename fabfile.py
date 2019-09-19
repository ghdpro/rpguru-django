"""RPGuru Fabric deployment script"""

import os
from datetime import datetime

from fabric import task


@task(hosts=['staging.visei.net'])
def deploy(c):
    _generate_id(c)


def _generate_id(c):
    """Generates a small template with commit number, id string and date"""
    count = c.local('git rev-list --count HEAD', timeout=1, hide=True)
    id = c.local('git rev-parse --short HEAD', timeout=1, hide=True)
    id_file = "{}/templates/id.html".format(os.path.dirname(__file__))
    output = f'Version {count.stdout.strip()}:{id.stdout.strip()} ({datetime.now().date().isoformat()})'
    c.local(f'echo "{output}" > {id_file}', timeout=1, hide=True)
