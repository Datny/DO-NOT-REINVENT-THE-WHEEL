from datetime import date
from pprint import pprint

from marshmallow import Schema, fields


class BookSchema(Schema):
    name = fields.Str()


