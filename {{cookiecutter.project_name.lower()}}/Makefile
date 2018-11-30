CWD=$(shell pwd)
SERVICE={{cookiecutter.project_name.lower()}}

init:
	python3 -m metaendpoints.tools.esp_init

esp:
	python3 -m metaendpoints.tools.esp_deploy --service=$(SERVICE) --lang=python --workdir=$(CWD)

dev:
	python3 -m metaendpoints.tools.esp_dev --service=$(SERVICE)
    
build_docs:
	# Для автоматической сборки общей документации
	git clone https://github.com/devision-io/hugo-theme-docs.git docs/themes/devision-docs
	cd docs && hugo

dev_docs:
	# Локальный тест сборки документации
	cd docs && hugo server
