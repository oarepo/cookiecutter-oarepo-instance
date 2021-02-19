{% include 'misc/header.py' %}

from . import config


class RecordsApp:
    def __init__(self, app=None, db=None):
        self.init_app(app, db)

    def init_app(self, app, db):
        self.init_config(app, db)

    def init_config(self, app, db):
        app.config.setdefault('RECORDS_DRAFT_ENDPOINTS', {}).update(
            config.RECORDS_DRAFT_ENDPOINTS
        )
        app.config.setdefault('RECORDS_REST_ENDPOINTS', {}).update(
            config.RECORDS_REST_ENDPOINTS
        )
        app.config.setdefault('RECORDS_REST_FACETS', {}).update(
            config.RECORDS_REST_FACETS
        )

        app.config.setdefault('RECORDS_REST_DEFAULT_SORT', {}).update(
            config.RECORDS_REST_DEFAULT_SORT
        )

        app.config.setdefault('RECORDS_REST_SORT_OPTIONS', {}).update(
            config.RECORDS_REST_SORT_OPTIONS
        )
