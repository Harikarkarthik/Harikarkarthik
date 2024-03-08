from rest_framework import serializers
from .models import Singer,Song

class Singerserializer(serializers.ModelSerializer):
    # song = serializers.SlugRelatedField(many=True ,read_only=True,slug_field='title')
    # song = Songserializer(many=True,read_only=True)
    class Meta:
        model = Singer
        fields = ['id','name','gender'] 

class Songserializer(serializers.ModelSerializer):
    # singer = Singerserializer()
    class Meta:
        model = Song
        fields = ['id','title','duration','singer']

     