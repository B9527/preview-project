# -*- coding: utf-8 -*-

from __future__ import unicode_literals

# restapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from preview.serialize import PreviewConfigSerializer
from preview.models import PreviewConfig, TableData


class UploadSettingViews(APIView):
    def post(self, request, format=None):
        file_obj = self.request.data['file']
        return_data = {
            "msg": "success",
            "code": 200,
            "result": {"file_name": file_obj.name}
        }

        return Response(return_data, status=status.HTTP_200_OK) 


class InputSettingViews(APIView):
    def post(self, request, format=None):
        request_data = self.request.data
        serializer = PreviewConfigSerializer(data=request_data, many=False)
        if serializer.is_valid():
            serializer.save()
        else:
            raise
        return_data = {
            "msg": "success",
            "code": 200,
            "result": {"request_data": request_data}
        }

        return Response(return_data, status=status.HTTP_200_OK) 


class PreviewConfigListViews(APIView):
    def get(self, request, foramt=None):
        pageNum = 1
        pageSize = 20
        args = {}
        if 'pageNum' in self.request.GET.keys():
            pageNum = int(self.request.GET['pageNum'])
        if 'pageSize' in self.request.GET.keys():
            pageSize = int(self.request.GET['pageSize'])
        
        if 'status' in self.request.GET.keys():
            config_status = self.request.GET['status']
            if config_status == "all":
                pass
            else:
                args['status'] = config_status
        if 'table' in self.request.GET.keys():
            table = self.request.GET['table']
            args['table__icontains'] = table

        task_list = PreviewConfig.objects.filter(**args).order_by('-id')
        total = task_list.count()
        task_list = task_list[(pageNum-1)*pageSize:pageNum*pageSize]
        task_list_data = PreviewConfigSerializer(task_list, many=True).data

        # 返回数据格式
        return_data = {
            "msg": "success",
            "code": 200,
            "result": {"task_list": task_list_data, "pageSize": pageSize, "pageNum": pageNum, "total": total, }
        }
        return Response(return_data, status=status.HTTP_200_OK)


class PreviewTableFieldsViews(APIView):
    def get(self, request, format=None):
        id = self.request.GET['id']
        preview_config = PreviewConfig.objects.get(id=id)
        host_temp = preview_config.host
        database_temp = preview_config.database
        table_temp = preview_config.table

        fields = TableData.objects.filter(database__host=host_temp, database__database=database_temp, table=table_temp).values('field').order_by('field').distinct('field')
        fields_value_list = [item['field'] for item in fields]

        # 返回数据格式
        return_data = {
            "msg": "success",
            "code": 200,
            "result": {"tableInfo":{"host": host_temp, "database": database_temp, "table": table_temp}, "fields": fields_value_list}
        }
        return Response(return_data, status=status.HTTP_200_OK)


class PreviewTableDataViews(APIView):
    def get(self, request, format=None):
        host = self.request.GET['host']
        database = self.request.GET['database']
        table = self.request.GET['table']
        field = self.request.GET['field']
        data_list = []

        table_data = TableData.objects.filter(database__host=host, database__database=database, table=table, field=field).values('data')
        for table in table_data:
            data_list.append(table['data'])

        # 返回数据格式
        return_data = {
            "msg": "success",
            "code": 200,
            "result": {"data": data_list}
        }
        return Response(return_data, status=status.HTTP_200_OK)
