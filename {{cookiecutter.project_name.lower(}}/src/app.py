from metaendpoints.apiserver import serve

from src.routes_{{cookiecutter.api_version}} import reg_server_{{cookiecutter.api_version}}

if __name__ == '__main__':
    serve([
        reg_server_{{cookiecutter.api_version}},
    ])
