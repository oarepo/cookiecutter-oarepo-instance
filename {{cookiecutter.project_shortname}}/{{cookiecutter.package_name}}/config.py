# Database
# ========
#: Database URI including user and password
{%- if cookiecutter.database == 'postgresql'%}
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{{cookiecutter.project_shortname}}:{{cookiecutter.project_shortname}}@localhost/{{cookiecutter.project_shortname}}'
{%- elif cookiecutter.database == 'mysql'%}
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{{cookiecutter.project_shortname}}:{{cookiecutter.project_shortname}}@localhost/{{cookiecutter.project_shortname}}'

# Disable Flask-DebugToolbar SQLAlchemy pane since it cannnot handle
# UUID in bytes format
# https://github.com/mgood/flask-debugtoolbar/issues/112
DEBUG_TB_ENABLED = False
{%- endif %}


PIDSTORE_RECID_FIELD = '{{ cookiecutter.datamodel_pid_name }}'
