from fabric.api import local


def run():
    local("poetry run python manage.py runserver")
