"""RPGuru Fabric deployment script"""

import os
from datetime import datetime

from fabric import task

hosts = ['rpguru@staging.visei.net', ]
repository = 'https://github.com/ghdpro/rpguru.git'
user = 'rpguru'
home = f'/home/{user}'
builds = f'{home}/builds'
venv = f'{home}/venv'
dump = f'{home}/dump'


@task(hosts=hosts)
def deploy(c):
    # Get latest commit ID
    rev = c.local('git rev-parse --short HEAD', timeout=1, hide=True).stdout.strip()
    _clone(c, rev)
    _venv(c, rev)
    _migrate(c, rev)
    _update_symlinks(c, rev)
    _generate_id(c, rev)


@task(hosts=hosts)
def init(c):
    """Initializes project"""
    rev = 'current'
    c.run(f'source {venv}/{rev}/bin/activate && cd {builds}'
          f'/current/ && python3 manage.py migrate --settings=settings.staging', echo=True)


def _clone(c, rev):
    """"Clone current build"""
    c.run(f'mkdir -p {builds}', echo=True)
    c.run(f'cd {builds} && rm -r -f {rev}', echo=True)
    c.run(f'cd {builds} && git clone {repository} {rev}', echo=True)


def _venv(c, rev):
    """Create virtualenv & install all requirements"""
    c.run(f'mkdir -p {venv}', echo=True)
    c.run(f'cd {venv} && rm -r -f {rev}', echo=True)
    c.run(f'cd {venv} && python3 -m venv {rev}', echo=True)
    c.run(f'source {venv}/{rev}/bin/activate && pip install -Uq pip', echo=True)
    c.run(f'source {venv}/{rev}/bin/activate && pip install -Uq setuptools', echo=True)
    c.run(f'source {venv}/{rev}/bin/activate && pip install -Uqr {builds}/{rev}/requirements.txt', echo=True)


def _migrate(c, rev):
    # Collect static files
    c.run(f'source {venv}/{rev}/bin/activate && cd {builds}'
          f'/current/ && python3 manage.py collectstatic --clear --no-input --settings=settings.staging', echo=True)
    # Run migrations
    c.run(f'source {venv}/{rev}/bin/activate && cd {builds}'
          f'/current/ && python3 manage.py migrate --settings=settings.staging', echo=True)
    # Run tests
    c.run(f'source {venv}/{rev}/bin/activate && cd {builds}'
          f'/current/ && python3 manage.py test --settings=settings.staging', echo=True)
    # Run check
    c.run(f'source {venv}/{rev}/bin/activate && cd {builds}'
          f'/current/ && python3 manage.py check --settings=settings.staging', echo=True)


def _update_symlinks(c, rev):
    """Updates 'current' symlinks"""
    c.run(f'cd {builds} && rm -r -f {rev}', echo=True)
    c.run(f'cd {builds} && ln -s {rev} current', echo=True)
    c.run(f'cd {venv} && rm -r -f {rev}', echo=True)
    c.run(f'cd {venv} && ln -s {rev} current', echo=True)


def _generate_id(c, rev):
    """Generates a small template with commit number, id string and date"""
    count = c.local('git rev-list --count HEAD', timeout=1, hide=True)
    id = c.local('git rev-parse --short HEAD', timeout=1, hide=True)
    id_file = "{}/templates/id.html".format(os.path.dirname(__file__))
    # Date is always the deployment date, assumes the latest commit was made the same day
    output = f'Version {count.stdout.strip()}:{id.stdout.strip()} ({datetime.now().date().isoformat()})'
    c.local(f'echo "{output}" > {id_file}', timeout=1, echo=True)
    c.put(id_file, f'{builds}/{rev}/templates/')
