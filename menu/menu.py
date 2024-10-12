from tabnanny import check
from typing import Any
from manager_venv.manager_venv import ManagerVenv
from manager_project.manager_django import ManagerDjango
from manager_project.manager_flask import ManagerFlask
from menu.options import Options
from utils.terminal_utils import pause_and_clear, clean_screen, print_line


def menu() -> None:
    print(
        """
▀█░█▀ █▀▀ █▀▀▄ ▀█░█▀ 　 █▀▄▀█ █▀▀█ █▀▀▄ █▀▀█ █▀▀▀ █▀▀ █▀▀█ 
░█▄█░ █▀▀ █░░█ ░█▄█░ 　 █░▀░█ █▄▄█ █░░█ █▄▄█ █░▀█ █▀▀ █▄▄▀ 
░░▀░░ ▀▀▀ ▀░░▀ ░░▀░░ 　 ▀░░░▀ ▀░░▀ ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀░▀▀
        \n"""
    )
    venv = create_venv()
    show_main_menu(venv)


def show_main_menu(venv: ManagerVenv) -> None:
    clean_screen()
    banner = """
█░█ █▀▀ █▄░█ █░█   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
▀▄▀ ██▄ █░▀█ ▀▄▀   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█"""
    main_menu = Options(
        {
            1: ("Create project", lambda: create_project_options(venv)),
            2: ("Install library", lambda: install_library(venv)),
            3: ("List libraries", lambda: list_library(venv)),
            4: ("Execute command", lambda: execute_command(venv)),
        },
        banner,
    )
    main_menu.choice()
    clean_screen()


def create_project_options(venv: ManagerVenv) -> None:
    clean_screen()
    banner = """
█▀█ █▀█ █▀█ ░░█ █▀▀ █▀▀ ▀█▀   █▀█ █▀█ ▀█▀ █ █▀█ █▄░█ █▀
█▀▀ █▀▄ █▄█ █▄█ ██▄ █▄▄ ░█░   █▄█ █▀▀ ░█░ █ █▄█ █░▀█ ▄█"""

    project_menu = Options(
        {
            1: ("Create Django project", lambda: create_project(venv, "Django")),
            2: ("Create Flask project", lambda: create_project(venv, "Flask")),
            # 3: ("Create Custom project", lambda: create_project(venv, "Custom")),
        },
        banner,
    )
    project_menu.choice()
    clean_screen()


def create_venv() -> ManagerVenv:
    venv_name: str = input("Virtual environment name (default venv): ")
    return ManagerVenv(venv_name) if venv_name else ManagerVenv()


def create_project(venv: ManagerVenv, project_type: str) -> ManagerVenv:
    project_name: str = input("Project name: ")
    project: ManagerVenv = Any
    print("Creating...\n")
    if project_type == "Django":
        project = ManagerDjango(venv, project_name)
        pause_and_clear()
        return project
    elif project_type == "Flask":
        project = ManagerFlask(venv, project_name)
        pause_and_clear()
        return project
    # elif project_type == "Custom":
    # return None


def install_library(venv: ManagerVenv) -> None:
    clean_screen()
    library_name: str = input("Library name: ")
    print("Installing...\n")
    print_line(venv.install_library(library_name))
    pause_and_clear()


def list_library(venv: ManagerVenv) -> None:
    clean_screen()
    print("Finding...\n")
    print_line(venv.list_library())
    pause_and_clear()


def execute_command(venv: ManagerVenv) -> None:
    clean_screen()
    command: str = input("Command: ")
    print("\nRunning...\n")
    print_line(venv.execute_venv_command(command))
    pause_and_clear()
