# Data analysis
- Document here the project: Project-YODA_frontend
- Description: Frontend package for the Le Wagon graduation project Project-Yoda, which uses a CNN to classify LEGO minifigure images and generates new pictures utilizing a DCGAN. 

# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for Project-YODA_frontend in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/Project-YODA_frontend`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "Project-YODA_frontend"
git remote add origin git@github.com:{group}/Project-YODA_frontend.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
Project-YODA_frontend-run
```

# Install

Go to `https://github.com/{group}/Project-YODA_frontend` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/Project-YODA_frontend.git
cd Project-YODA_frontend
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
Project-YODA_frontend-run
```
