import os
from django.core.exceptions import ValidationError


def validate_file(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ['.csv', '.xlsx', '.txt', '.sqlite']:
        raise ValidationError('.csc, .xlsx, .txt, .sqliteのみアップロードできます．')
