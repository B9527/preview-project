# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from preview.models import PreviewConfig, TableData, Database

# Register your models here.

admin.site.register(PreviewConfig)
admin.site.register(TableData)
admin.site.register(Database)
