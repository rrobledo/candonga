from jinja2 import Environment, PackageLoader

env = Environment(loader=PackageLoader('config', 'templates'))


def gen_nginx_config(cores=1):
    template = env.get_template('nginx.conf')
    output = template.render(cores=cores)
    return output
