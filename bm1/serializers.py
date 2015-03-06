# -*- coding: UTF-8 -*-
'''
Created on 2015年3月5日

@author: carey.yang
'''
from bm1.models import Note
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'content', 'create_time')

# ViewSets define the view behavior.
class NoteViewSet(viewsets.ModelViewSet):
    """
        允许查看和编辑Note 的 API endpoint
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

