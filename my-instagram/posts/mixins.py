from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CanLikeMixin:

    @action(['PATCH'], True, permission_classes=[IsAuthenticated])
    def like(self, request, pk):
        obj = self.get_object()

        if request.user in obj.likes.all():
            obj.likes.remove(request.user)
        else:
            obj.likes.add(request.user)
        serializer = self.get_serializer(obj)
        return Response(serializer.data)
