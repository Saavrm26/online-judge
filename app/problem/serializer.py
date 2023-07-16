from rest_framework import serializers
from problem.models import Problem


class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Problem
        fields = ['id', 'name', 'statement', 'difficulty']
