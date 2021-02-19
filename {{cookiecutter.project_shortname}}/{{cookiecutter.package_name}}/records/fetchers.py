{% include 'misc/header.py' %}

from collections import namedtuple
from flask import current_app

from invenio_pidstore.providers.recordid import RecordIdProvider

FetchedPID = namedtuple('FetchedPID', ['provider', 'pid_type', 'pid_value'])


# TODO: Change it, this is invenio fetcher
def recid_fetcher(record_uuid, data):
    """Legacy way to fetch a record's identifiers.
    :param record_uuid: The record UUID.
    :param data: The record metadata.
    :returns: A :data:`invenio_pidstore.fetchers.FetchedPID` instance.
    """
    pid_field = current_app.config['PIDSTORE_RECID_FIELD']
    return FetchedPID(
        provider=RecordIdProvider,
        pid_type=RecordIdProvider.pid_type,
        pid_value=str(data[pid_field]),
    )

def restoration_object_all_fetcher(record_uuid, data):
    fetched_pid = recid_fetcher(record_uuid, data)
    print(data)
    if 'oarepo:validity' in data:
        return FetchedPID(
            provider=fetched_pid.provider,
            pid_type='drcid',
            pid_value=fetched_pid.pid_value,
        )
    else:
        return fetched_pid
