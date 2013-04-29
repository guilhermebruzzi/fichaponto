root_dir		= $(realpath .)
src_dir			= ${root_dir}/fichaponto

help:
	@echo 'install - instala as dependencias no seu virtualenv'
	@echo 'create_db - cria as tabelas do mysql configurado (padrao é no db fichaponto em localhost)'
	@echo 'run - roda a aplicacao'

install:
	@pip install -r requirements.txt
	@pip install -r requirements-local.txt

create_db:
	@python ${src_dir}/create_db.py

clean:
	@find . -type f -name "*.pyc" -exec rm -rf {} \;

kill_run:
	@ps aux | awk '(make run && $$0 !~ /awk/){ system("kill -9 "$$2) }'

run: clean
	@python ${src_dir}/app.py
