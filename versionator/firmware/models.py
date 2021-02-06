import os
import uuid
import unicodedata

from django.db import models

from .validators import (
    validate_file_extension,
    validate_version_format,
    validate_version_only_number
)


def file_rename(instance, filename):
    upload_to = 'firmmware'
    ext = filename.split('.')[-1]
    normalized_project_name = instance.normalized_project_name()
    normalized_version = instance.normalized_version()
    filename = '{}_v{}.{}'.format(normalized_project_name, normalized_version, ext)

    return os.path.join(upload_to, filename)


class Firmmware(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project_name = models.CharField(max_length=255)
    version = models.CharField(max_length=12, validators=[validate_version_format, validate_version_only_number])
    compatible_card_name = models.CharField(max_length=255)
    file = models.FileField(upload_to=file_rename, validators=[validate_file_extension])

    def normalized_project_name(self):
        project_name = self.project_name.lower().replace(' ', '_')
        nfkd_project_name = unicodedata.normalize('NFKD', project_name)
        ascii_project_name = nfkd_project_name.encode('ASCII', 'ignore').strip()
        return ascii_project_name.decode("utf-8")

    def normalized_version(self):
        version = self.version.replace('.', '_')
        return version
