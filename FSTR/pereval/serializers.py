from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.serializers import ValidationError
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'phone', 'name', 'fam', 'otc', 'email']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'image']


class PerevalSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    image = ImageSerializer()

    class Meta:
        model = Pereval
        exclude = 'status'

    def validate(self, attrs):
        user_data = attrs.get('user')
        if not user_data:
            raise ValidationError("User data is missing.")

        if self.instance:
            user = self.instance.user
        else:
            try:
                user = User.objects.get(email=user_data.get('email'))  # .exists())
            except User.DoesNotExist:
                user = None

        if user is not None:
            if user.name != user_data.get('name') or \
                    user.otc != user_data.get('otc') or user.fam != user_data.get('fam') or \
                    user.phone != user_data.get('phone') or user.email != user_data.get('email'):
                raise ValidationError("Information cannot be changed")

        super().validate(attrs)

        return attrs

    def create(self, validated_data):

        user_data = validated_data.pop('user')

        coords_data = validated_data.pop('coords')
        coords = Coords.objects.create(**coords_data)

        level_data = validated_data.pop('level')
        level = Level.objects.create(**level_data)

        images_data = validated_data.pop('image')
        image = Image.objects.create(**images_data)

        if Pereval.objects.filter(user__email=user_data.get('email')).exists():
            user = User.objects.get(email=user_data.get('email')).pk
            pereval = Pereval.objects.create(**validated_data, user=User.objects.get(email=user_data.get('email')),
                                             level=level, coords=coords, image=image)
        else:
            user = User.objects.create(**user_data)
            pereval = Pereval.objects.create(**validated_data, user=user, level=level, coords=coords, image=image)
        return pereval
