from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework import mixins
from rest_framework.response import Response

from .serializers import *
from .models import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class ImageViewSet(generics.ListAPIView):
    queryset = Image.objects.all().order_by('-date_added')
    serializer_class = ImageSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PerevalListView(ListAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class SubmitDataViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        generics.GenericAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class PerevalUpdateView(RetrieveUpdateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalUpdateSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Status not "new"')
            serializer.save()
            return Response({'state': 1, 'message': 'Update successfully'})
        else:
            return Response({'state': 0, 'message': serializer.errors})

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=instance)
        if serializer.is_valid():
            if instance.status != 'new':
                raise ValidationError(f'Status not "new"')
            serializer.save()
            return Response({'state': 1, 'message': 'Update successfully'})
        else:
            return Response({'state': 0, 'message': serializer.errors})
