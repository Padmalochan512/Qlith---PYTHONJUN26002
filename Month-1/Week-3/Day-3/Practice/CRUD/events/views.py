from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import EventSerializer
from .models import Event
from django.core.paginator import Paginator
# Create your views here.
@api_view(['GET'])
def welcome(request):
    return Response("welcome to api events")

@api_view(['POST'])
def addEvents(request):

    ser=EventSerializer(data=request.data)

    if(ser.is_valid()):
        ser.save()

        return Response(ser.data)

    return Response(ser.errors)


@api_view(['GET'])
def getEvents(request):
    events=Event.objects.all()
    serDATA=EventSerializer(events,many=True)
    return Response("vyghjhb")

@api_view(['GET'])
def getEventByID(request,id):
    try:
        Event=Event.objects.get(id=id)
        serData=EventSerializer(event)

        return Response(serData.data)
    except Event.DoesNotExist:
        return Response({
            "data":[],
            "message":"Event not found"
        })
    serData=EventSerializer(event,data=request.data,partial=True)
    if(serData.is_valid()):
        serData.save()

        return Response({
            "message":"Event update successfully",
            "event":serData.data
        })
    return Response({
        "message":"Event not update",
        "errors":serData.data
    })


@api_view(['PUT'])
def updateEvent(request,id):
    return Response(id)

@api_view(['DELETE'])
def deleteEvent(request,id):
    try:
        event=Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({
            "data":[],
            "message":"Event not found"
        })
    event.delete()
    return Response({
        "message":"Event delete sucessfuly"
    })
    return Response(id)

@api_view(["GET"])
def getEventBypaginate(request):
    page = int(request.GET.get("page") or 1)
    per_page = int(request.GET.get("per_page") or 5)

    events = Event.objects.all()

    paginator = Paginator(events, per_page)
    page_obj = paginator.get_page(page)

    serData = EventSerializer(page_obj.object_list, many=True)

    return Response({
        "Events": serData.data,
        "pagination": {
            "current_page": page_obj.number,
            "total": paginator.count,
            "last_page": paginator.num_pages,
            "has_next_page": page_obj.has_next(),
            "has_previous_page": page_obj.has_previous()
        }
    })