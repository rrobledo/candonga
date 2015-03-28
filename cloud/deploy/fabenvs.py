import os
import fabric.api

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CERTS_DIR = os.path.join(BASE_DIR, 'certs')


def local():
    fabric.api.env.env_name = 'local'
    fabric.api.env.roledefs = {
        'webserver_python': ['127.0.0.1', ],
        'mongodb': ['127.0.0.1'],
        'log_server': [],
    }
    fabric.api.env.user = "ubuntu"


def aws():
    fabric.api.env.env_name = 'aws'
    fabric.api.env.roledefs = {
        'webserver_python': ['52.1.85.106', ],
        'mongodb': ['52.1.85.106'],
        'log_server': [],
    }

    fabric.api.env.user = "ubuntu"
    #fabric.api.env.gateway = "ubuntu@54.86.157.176"
    path = os.path.join(CERTS_DIR, "aws.pem")
    fabric.api.env.key_filename = path
