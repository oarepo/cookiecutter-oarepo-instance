{% include 'misc/header.py' %}
"""JSON Schemas."""

from invenio_records_rest.schemas import StrictKeysMixin
from oarepo_dc.marshmallow import DCObjectSchemaV2Mixin
from oarepo_invenio_model.marshmallow import InvenioRecordMetadataSchemaV1Mixin, \
    InvenioRecordMetadataFilesMixin


class RecordMetadataSchemaV1(
    InvenioRecordMetadataFilesMixin,
    InvenioRecordMetadataSchemaV1Mixin,
    DCObjectSchemaV2Mixin,
    StrictKeysMixin):
    """Schema for records drafts metadata."""

    pass
