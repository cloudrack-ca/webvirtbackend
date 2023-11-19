from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from webvirtcloud.views import error_message_response
from .models import FloatIP
from .tasks import delete_floating_ip
from .serializers import FloatIPSerializer, FloatIPActionSerializer


class FloatingIPListAPI(APIView):
    class_serializer = FloatIPSerializer

    def get_queryset(self):
        virtance_id = self.request.query_params.get("virtance_id")

        queryset = FloatIP.objects.filter(user=self.request.user, is_deleted=False)
        
        if virtance_id:
            queryset = queryset.filter(ipaddress__virtance_id=virtance_id)

        return queryset

    def get(self, request, *args, **kwargs):
        serializer = self.class_serializer(self.get_queryset(), many=True)
        return Response({"floating_ips": serializer.data})

    def post(self, request, *args, **kwargs):
        serializer = self.class_serializer(data=request.data, context={"user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"floating_ip": serializer.data}, status=status.HTTP_201_CREATED)
  

class FloatingIPDataAPI(APIView):
    class_serializer = FloatIPSerializer

    def get_object(self):
        return get_object_or_404(
            FloatIP, ipaddress__address=self.kwargs.get("ip"), user=self.request.user, is_deleted=False
        )

    def get(self, request, *args, **kwargs):
        serializer = self.class_serializer(self.get_object(), many=False)
        return Response({"floating_ip": serializer.data})

    def delete(self, request, *args, **kwargs):
        floatip = self.get_object()

        if floatip.event is not None:
            return error_message_response("The floating ip already has event.")


        floatip.event = FloatIP.DELETE
        floatip.save()

        delete_floating_ip.delay(floatip.id)

        return Response(status=status.HTTP_204_NO_CONTENT)


class FloatingIPActionAPI(APIView):
    class_serializer = FloatIPActionSerializer

    def get_object(self):
        return get_object_or_404(
            FloatIP, ipaddress__address=self.kwargs.get("ip"), user=self.request.user, is_deleted=False
        )
    
    def post(self, request, *args, **kwargs):
        floatip = self.get_object()

        if floatip.event is not None:
            return error_message_response("The floating ip already has event.")

        serializer = self.class_serializer(data=request.data, context={"floatip": floatip})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
