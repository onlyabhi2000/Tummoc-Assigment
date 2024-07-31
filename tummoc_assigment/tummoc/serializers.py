from rest_framework import serializers
from .models import Teacher, Student


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DistanceSerializer(serializers.Serializer):
    latitude1 = serializers.FloatField()
    longitude1 = serializers.FloatField()
    latitude2 = serializers.FloatField()
    longitude2 = serializers.FloatField()
