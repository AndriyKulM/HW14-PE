from datetime import datetime
from email.policy import default
from marshmallow import Schema, fields
from marshmallow.validate import Length


class PupilSchema(Schema):
    id = fields.Integer(required=True, dump_only=True)
    name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True, validate=Length(min=10, max=355))
    home_tasks = fields.Str(required=True)
    created_on = fields.DateTime()