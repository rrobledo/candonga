from config import nginx_settings
from fabric.api import *
import fabutils
import tempfile


def deploy():
    _install_nginx()
    _configure_nginx()


def _install_nginx():
    with cd('/tmp'):
        sudo("wget '{0}'".format(nginx_settings.NGINX_DONWLOAD_URL))
        sudo("wget '{0}'".format(nginx_settings.NGINX_HEADERS_MODULE_DONWLOAD_URL))
        sudo("tar -xzvf {0}".format(nginx_settings.NGINX_DONWLOAD_FILE))
        sudo("tar -xzvf {0}".format(nginx_settings.NGINX_HEADERS_MODULE_DONWLOAD_FILE))
    with cd('/tmp/{0}'.format(nginx_settings.NGINX_UNZIP_FOLDER)):
        sudo("apt-get install libpcre3 libpcre3-dev")
        sudo("./configure --prefix=/opt/nginx \
                          --add-module=/tmp/{0}".format(nginx_settings.NGINX_HEADERS_MODULE_UNZIP_FOLDER))
        sudo("make")
        sudo("make install")


def _configure_nginx():
    sudo("killall nginx", warn_only=True)
    put("./config/templates/limits.conf", "/etc/security/limits.conf", use_sudo=True)
    sudo('mkdir -p /var/log/nginx', warn_only=True)
    cores = sudo("nproc")
    ngnix_conf = fabutils.gen_nginx_config(int(cores))
    fp = tempfile.NamedTemporaryFile(delete=False)
    fp.write(ngnix_conf)
    fp.close()
    put(fp.name, "/opt/nginx/conf/nginx.conf", use_sudo=True)
    fp.unlink(fp.name)
    sudo("update-rc.d -f nginx remove")
    sudo("rm -rf /etc/init.d/nginx", warn_only=True)
    put("./config/templates/init.d.nginx", "/etc/init.d/nginx", use_sudo=True)
    with cd('/etc/init.d'):
        sudo('chmod +x nginx')
        sudo("update-rc.d nginx defaults")
    sudo("service nginx start")
