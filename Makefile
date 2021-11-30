# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* Project-YODA_frontend/*.py

black:
	@black scripts/* Project-YODA_frontend/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr Project-YODA_frontend-*.dist-info
	@rm -fr Project-YODA_frontend.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)


# ----------------------------------
#  Create docker file and publsih via gcloud
# ----------------------------------

# set configurations for glcoud -> specify the project ID

config_gcloud:
	gcloud config set project project-yoda-333014

# build a docker image with M1/apple silicon chip
# select project ID and give an image name

docker_build_m1:
	docker build --platform linux/amd64 -t eu.gcr.io/project-yoda-333014/project_yoda_frontend .

# build a docker image with intel chip
# select project ID and give an image name

docker_build_intel:
	docker build -t eu.gcr.io/project-yoda-333014/project_yoda_frontend .

# run the docker image locally to double check that it's working, terminate the run before using docker_push
# select project ID and give an image name

docker_run:
	docker run -e PORT=8000 -p 8000:8000 eu.gcr.io/project-yoda-333014/project_yoda_frontend

# push the docker image to gcloud
# select project ID and give an image name

docker_push:
	docker push eu.gcr.io/project-yoda-333014/project_yoda_frontend

# deploy the image on gcloud run
# select project ID and give an image name

docker_deploy:
	gcloud run deploy --image eu.gcr.io/project-yoda-333014/project_yoda_frontend --platform managed --region europe-west1
