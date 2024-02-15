from rest_framework import views
from rest_framework.response import Response
from rest_framework import status

from apps.event.services import (
    EventListService,
    EventRetrieveService,
    EventCreateService,
    EventUpdateService,
    EventDeleteService,
)


class EventListView(views.APIView):
    def get(self, request):
        service = EventListService.get_events()
        return Response(service, status=status.HTTP_200_OK)


class EventRetrieveView(views.APIView):
    def get(self, request, pk=None):
        service = EventRetrieveService.get_event(pk=pk)
        return Response(service, status=status.HTTP_200_OK)


class EventCreateView(views.APIView):
    def post(self, request):
        service, status = EventCreateService.create_event(event=request)
        return Response(service, status=status)


class EventUpdateView(views.APIView):
    def put(self, request, pk):
        service, status = EventUpdateService.update_event(event_data=request.data, pk=pk)
        return Response(service, status=status)


class EventDeleteView(views.APIView):
    def delete(self, request, pk):
        service = EventDeleteService.delete_event(pk)
        return Response(service)
