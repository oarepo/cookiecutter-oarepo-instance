#!/bin/bash

pybabel extract -o {{cookiecutter.project_shortname}}/translations/messages.pot {{cookiecutter.project_shortname}}
pybabel update -d {{cookiecutter.project_shortname}}/translations -i {{cookiecutter.project_shortname}}/translations/messages.pot -l cs
pybabel update -d {{cookiecutter.project_shortname}}/translations -i {{cookiecutter.project_shortname}}/translations/messages.pot -l en
pybabel compile -d {{cookiecutter.project_shortname}}/translations
