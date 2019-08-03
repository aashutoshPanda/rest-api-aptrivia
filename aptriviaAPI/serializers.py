from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('id','name1','name2','schoolName','group','marks','stateRank','award')
