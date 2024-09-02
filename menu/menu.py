from venv_creator.venv_creator import VenvCreator as Venv
from project_creator.django_creator import DjangoCreator as Django
from project_creator.flask_creator import FlaskCreator as Flask
from project_creator.project_creator import ProjectCreator as Project
from time import sleep

print('''
█▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀▀ █▀█ █▀▀ ▄▀█ ▀█▀ █▀█ █▀█
█▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄▄ █▀▄ ██▄ █▀█ ░█░ █▄█ █▀▄
      ''')


def menu() -> None:
    venv = create_venv()
    option(venv)


def option(venv: Venv) -> None:
    while True:
        print("\n1 - Create Django project")
        print("2 - Create Flask project")
        print("3 - Install library")
        print("4 - List libraries")
        print("0 - Leave")
        option = input("\nChoose an option: ")

        match option:
            case '1':
                project = create_project(venv, "Django")
                print(project)
            case '2':
                project = create_project(venv, "Flask")
                print(project)
            case '3':
                install_library(venv)
            case '4':
                list_library(venv)
            case '0':
                print("Leaving...")
                sleep(2)
                break


def create_venv() -> Venv:
    venv_name = input("Virtual environment name: ")
    print("Creating or finding venv...\n")
    if (venv_name == ""):
        venv = Venv()
    else:
        venv = Venv(venv_name)
    return venv


def create_project(venv: Venv, project_tipe: str) -> Project:
    project_name = input("Project name: ")
    project = None
    print("creating..\n")
    if (project_tipe == 'Django'):
        project = Django(venv, project_name)
    elif (project_tipe == 'Flask'):
        project = Flask(venv, project_name)
    return project


def install_library(venv: Venv) -> None:
    library_name = input("Library name: ")
    print("Installing...\n")
    if (venv.install_library(library_name)):
        print(f"Library {library_name} installed correctly")
    else:
        print(f"Library {library_name} not installed")


def list_library(venv: Venv) -> None:
    print("Finding...\n")
    if (not venv.list_library()):
        print("Failed to find libraries")