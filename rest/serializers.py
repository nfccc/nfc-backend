from rest_framework import serializers
# from.models import Beach
# from.models import Video
from.models import Girls ,  Photo , Video , User , Creator , Auction , Adverts
from cloudinary.uploader import upload








class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']




class GirlsSerializer(serializers.ModelSerializer):
 class Meta:
   model = Girls
   fields = '__all__'
   

        
        
class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'
        
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'




class CreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creator
        fields = '__all__'
   


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ['id', 'name', 'description', 'category', 'price', 'condition', 'image']



class AdvertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adverts
        fields = ['id', 'image', 'name', 'description', 'price']
   





