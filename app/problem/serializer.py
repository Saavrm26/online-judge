from rest_framework import serializers
from problem.models import Problem, Tag, TPjoin
from django.utils.translation import gettext as _


class TPjoinSerializer(serializers.Serializer):
    name = serializers.CharField()

    def validate(self, attrs):
        print('Inside tp join vlaidate')
        return attrs

    def create(self, validated_data):
        print("Inside tpjoin")
        print(validated_data)


class TagSerializer(serializers.Serializer):

    name = serializers.CharField()

    def validate(self, attrs):
        print('inside tag ser')
        return attrs

    # def create(self, validated_data):
    #     print("insdie tag ser create")
    #     return validated_data


class ProblemSerializer(serializers.ModelSerializer):

    tags = serializers.ListField(child=serializers.CharField(), read_only=True)

    class Meta:
        model = Problem
        fields = ['id', 'name', 'statement', 'difficulty', 'tags']

    def to_internal_value(self, data):
        return data

    def to_representation(self, instance):
        tags = [tag.name for tag in instance.tags.all()]
        dict_instance = {}
        dict_instance['id'] = instance.id
        dict_instance['name'] = instance.name
        dict_instance['statement'] = instance.statement
        dict_instance['difficulty'] = instance.difficulty
        dict_instance['tags'] = tags

        return super().to_representation(dict_instance)

    def create(self, validated_data):
        print(validated_data)
        if ('tags' not in validated_data) or (not validated_data['tags']):
            msg = _('Atleast one tag must be provided')
            raise serializers.FieldDoesNotExist(msg)
        tags_changelist = validated_data.pop('tags')
        problem = Problem.objects.create(**validated_data)
        print(tags_changelist)
        problem.tags.add(*tags_changelist)
        return problem

    def update(self, instance, validated_data):
        tags_changelist = []
        if ('tags' in validated_data):
            tags_changelist = validated_data.pop('tags')
        problem = super().update(instance, validated_data)

        for tag in tags_changelist:
            change = tag[0]
            tag = tag[1:]
            if (change == '+'):
                problem.tags.add(tag)
            else:
                problem.tags.remove(tag)

        return problem
