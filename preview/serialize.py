#!/usr/bin/python
# coding:utf-8

from rest_framework import serializers
from preview.models import PreviewConfig


class PreviewConfigSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreviewConfig
        fields = ('host', 'database', 'table', 'schema', 'user', 'status', 'start_time', 'end_time', 'id')

    def save(self):
        print self.validated_data
        host = self.validated_data['host']
        database = self.validated_data['database']
        table = self.validated_data['table']
        schema = self.validated_data['schema']
        user = self.validated_data['user']
        preview_config = PreviewConfig(host=host, database=database, table=table, schema=schema, user=user)
        preview_config.save()

