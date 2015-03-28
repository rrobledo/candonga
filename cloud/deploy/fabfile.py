from fabric.api import *
from fabric.colors import green
from fabric.colors import red
from fabenvs import *


@roles('webserver_python')
@parallel
def webserver_python(build_key, build_number):
    if not fabric.api.env.host_string:
        return

    print green("INSTALLING PYTHON WEB_SERVER...")
    sudo("ls -l")
    print green("PYTHON WEB_SERVER TASK COMPLETED")


def deploy(build_key, build_number):
    if build_key.strip() == '' or build_number.strip() == '':
        print red("Please provide build_key and build_number. LOCAL for using local repository")
        return False

    print 'Using build_key: {}, build_number: {}'.format(build_key, build_number)
    fabric.api.execute(webserver_python, build_key, build_number)
