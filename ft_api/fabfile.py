from fabric.decorators import task
from fabric.operations import local


@task()
def pysetup():
    local('./pysetup.sh')


@task()
def runserver():
    manage("runserver 0.0.0.0:8000")


@task()
def manage(command):
    local('./pyenv.sh ./manage.py {command}'.format(command=command))


@task
def load_data(path):
    manage('loaddata {path}'.format(path=path))


@task()
def makemigrations():
    manage('makemigrations')


@task()
def migrate():
    manage('migrate --run-syncdb')


@task(alias='rdb')
def recreate_database():
    local('rm -rf ./db.sqlite3')
    migrate()
