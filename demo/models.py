from django.db import models

from versions.models import Versionable, VersionedManyToManyField

class FirstModel(Versionable):
    f = models.TextField()

class SecondModel(Versionable):
    g = models.TextField()

    other = VersionedManyToManyField(FirstModel)

