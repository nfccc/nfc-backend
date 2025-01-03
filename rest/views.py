from django.http import JsonResponse
# from.models import Beach
# from.serializers import BeachSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# from .models import Video
# from .serializers import VideoSerializer
from rest_framework import generics
from .models import Girls
from .serializers import GirlsSerializer
from  django.contrib.auth import logout
from  django.shortcuts import render , redirect
from .models import User , Photo , Video , Creator , Password , Auction , Adverts
from .serializers import UserSerializer , PhotoSerializer, VideoSerializer , CreatorSerializer  , AuctionSerializer  , AdvertsSerializer
from django.shortcuts import get_object_or_404
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")





def logout_view(request):
    logout(request)
    return redirect("/")
    

@api_view(['GET', 'POST'])
def girls_list(request):
    if request.method == 'GET':
        name = request.GET.get('name', None)
        if name:
            girls = Girls.objects.filter(name=name)
        else:
            girls = Girls.objects.all()
        serializer = GirlsSerializer(girls, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = GirlsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def girls_detail(request, pk):
    try:
        girl = Girls.objects.get(pk=pk)
    except Girls.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GirlsSerializer(girl)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GirlsSerializer(girl, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        girl.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def girl_by_name(request, name):
    try:
        girl = Girls.objects.get(name=name)
    except Girls.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = GirlsSerializer(girl)
    return Response(serializer.data)






@api_view(['GET'])
def girls_photos(request, pk):
    try:
        girl = Girls.objects.get(pk=pk)
    except Girls.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    photos = Photo.objects.filter(girl=girl)
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)




@csrf_exempt
def create_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('password')
        Password.objects.create(password=password)
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)

@csrf_exempt
def get_passwords(request):
    if request.method == 'GET':
        passwords = Password.objects.all().values('password')
        return JsonResponse({'passwords': list(passwords)})
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)






    

   
# USERS

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            existing_user = User.objects.filter(email=email).first()
            if existing_user:
                serializer = UserSerializer(existing_user)
                return Response(serializer.data, status=status.HTTP_200_OK)
        
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
    
    
    
    
    
#NEW VIDEO
@api_view(['GET', 'POST'])
def video_list(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, pk):
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET'])
def videos_by_girl(request, girl_id):
    try:
        videos = Video.objects.filter(girl_id=girl_id)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)
    except Video.DoesNotExist:
        return Response({'message': 'Videos not found for the specified girl ID'}, status=status.HTTP_404_NOT_FOUND)



   
   

   ### CREATORS
@api_view(['GET', 'POST'])
def creator_list(request):
    if request.method == 'GET':
        name = request.GET.get('name', None)
        if name:
            try:
                creator = Creator.objects.get(name=name)
                serializer = CreatorSerializer(creator)
                return Response(serializer.data)
            except Creator.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            creators = Creator.objects.all()
            serializer = CreatorSerializer(creators, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CreatorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def creator_detail(request, pk):
    try:
        creator = Creator.objects.get(pk=pk)
    except Creator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreatorSerializer(creator)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CreatorSerializer(creator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        creator.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

 #getting creator by name   

@api_view(['GET'])
def creator_by_name(request, username):
    try:
        user = User.objects.get(username=username)
        creator = Creator.objects.get(user=user)
    except (User.DoesNotExist, Creator.DoesNotExist):
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = CreatorSerializer(creator)
    return Response(serializer.data)


##GET CREATOR BY USERNAME
def get_creator_by_username(request, username):
    user = get_object_or_404(User, username=username)
    creator = getattr(user, 'creator_profile', None)

    data = {field.name: getattr(creator, field.name, None) for field in Creator._meta.fields} if creator else {}

    return JsonResponse(data)
   
   
   
   



@api_view(['GET', 'PUT'])
# @permission_classes([IsAuthenticated])
def user_creator_profile(request):
    try:
        creator = request.user.creator_profile
    except Creator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CreatorSerializer(creator)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CreatorSerializer(creator, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    




### 
### SERIOUS STUFF HERE BELOW
### THE BELOW HERE IS SERIOUS STUFF
###

# 1. ##GET CREATOR BY USERNAME THAT HE/ SHE LOGGED IN WITH
def get_creator_by_username(request, username):
    user = get_object_or_404(User, username=username)
    creator = getattr(user, 'creator_profile', None)

    data = {field.name: getattr(creator, field.name, None) for field in Creator._meta.fields} if creator else {}

    return JsonResponse(data)





### 
### SERIOUS STUFF HERE BELOW
### THE BELOW HERE IS SERIOUS STUFF
###


# 1. NEED USER TO FILL IN THE HEADER , AVATAR , USERNAME, DISPLAY NAME , BIO , SUBSCRIPTION PER MONTH





@api_view(['GET', 'POST'])
def auction_list(request):
    if request.method == 'GET':
        auctions = Auction.objects.all()
        serializer = AuctionSerializer(auctions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuctionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def auction_detail(request, pk):
    try:
        auction = Auction.objects.get(pk=pk)
    except Auction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AuctionSerializer(auction)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AuctionSerializer(auction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        auction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    






@api_view(['GET', 'POST'])
def adverts_list(request):
    if request.method == 'GET':
        adverts = Adverts.objects.all()
        serializer = AdvertsSerializer(adverts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def adverts_detail(request, pk):
    try:
        advert = Adverts.objects.get(pk=pk)
    except Adverts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertsSerializer(advert)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdvertsSerializer(advert, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        advert.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)