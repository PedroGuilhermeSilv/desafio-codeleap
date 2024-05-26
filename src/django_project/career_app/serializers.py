from rest_framework import serializers


class CareersResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, allow_blank=False)
    content = serializers.CharField()
    username = serializers.CharField(max_length=255, allow_blank=False)
    created_datetime = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")


class RetrieveCareerResponseSerializer(serializers.Serializer):
    data = CareersResponseSerializer(source="*")


class RetrieveCareerRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class CreateCareerRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, allow_blank=False)
    content = serializers.CharField()
    username = serializers.CharField(max_length=255, allow_blank=False)


class CreateCareerResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class UpdateCareerRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255, allow_blank=False)
    content = serializers.CharField()


class DeleteCareerRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class ListCareerResponseSerializer(serializers.Serializer):
    data = CareersResponseSerializer(many=True)


class DeleteCategoryRequestSerializer(serializers.Serializer):
    id = serializers.UUIDField()
