# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models


class Database(models.Model):

    host = models.TextField()
    database = models.TextField()
    schema = models.TextField(null=True, blank=True)
    username = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = "mdatabase"


class TableData(models.Model):

    database = models.ForeignKey(Database)
    table = models.TextField()
    field = models.TextField()
    data = JSONField() # one row data represented by dict {field: value}

    class Meta:
        db_table = "table_data"


class PreviewConfig(models.Model):

    host = models.TextField()
    database = models.TextField()
    schema = models.TextField(null=True, blank=True)
    table = models.TextField()
    status = models.TextField(default="submit") # submit, executing, success, fail
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User)

    class Meta:
        db_table = "preview_config"

    def __str__(self):
        return "%s" % (self.id)

