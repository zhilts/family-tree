from fabric.context_managers import lcd
from fabric.decorators import task
from fabric.operations import local, os

API_PATH = 'ft_api'
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


@task()
def pysetup():
    ft('pysetup')


@task()
def ft(command):
    with lcd('{root_path}/{api_path}'.format(root_path=ROOT_PATH, api_path=API_PATH)):
        local('fab {command}'.format(command))
