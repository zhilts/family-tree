from fabric.decorators import task
from fabric.operations import local, os

DJ_PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

@task()
def pysetup():
    local('{project_path}/pysetup.sh'.format(project_path=DJ_PROJECT_PATH))


@task()
def runserver():
    manage("runserver 0.0.0.0:8000")


@task()
def manage(command):
    local('{project_path}/pyenv.sh {project_path}/manage.py {command}'
          .format(command=command, project_path=DJ_PROJECT_PATH)
          )


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
    local('rm -rf {project_path}/db.sqlite3'.format(project_path=DJ_PROJECT_PATH))
    migrate()
