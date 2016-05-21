from fabric.context_managers import lcd
from fabric.decorators import task
from fabric.operations import local

API_PATH = 'ft_api'


@task()
def pysetup():
    with lcd('./ft_api'):
        local('fab pysetup')


@task()
def ft(command):
    with lcd(API_PATH):
        local('fab {command}'.format(command))
