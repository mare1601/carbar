from fabric.api import cd, env, local, run, sudo
from fabric.context_managers import hide, settings

def serve(listen='127.0.0.1', port=8000):
    local('./manage.py runserver %s:%s' % (listen, port))

def errserve(listen='127.0.0.1', port=8000):
    local('./manage.py runserver %s:%s %s' % (listen, port, '--insecure'))
