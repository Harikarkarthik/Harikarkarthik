from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.decorators import action


 # Create your views here.


class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = Singerserializer
    # filter_backends = [SearchFilter]
    # search_fields = ['^name']
    

class SongViewSet(viewsets.ModelViewSet):
    queryset= Song.objects.all()
    serializer_class= Songserializer
    # filter_backends = [SearchFilter]
    # search_fields = ['^title']
    #*****************By using super().list()method --it goes to to the default list() method********************
    def list(self, request):
        song_duration = request.query_params.get('duration')
        singer_gender = request.query_params.get('gender')
        singer_name = request.query_params.get('name')
        start_letter = request.query_params.get('search')
        #filtering based on duration of song and singer gender featching singer name
        if song_duration is not None:
                song_duration = int(song_duration)
                filtered_songs = Song.objects.filter(duration=song_duration,singer__gender=singer_gender) #AND
                # filtered_songs = Song.objects.filter(duration=song_duration) | Song.objects.filter(singer__gender=singer_gender) #OR
                singer_names = set(song.singer.name for song in filtered_songs)
                return Response({"singer_names":list(singer_names)})
        #filtering based on gender featching singer name
        elif singer_gender is not None:
             filtered_songs = Song.objects.filter(singer__gender=singer_gender)
             filtered_songs = filtered_songs.order_by('singer__name')
             singer_names = set(song.singer.name for song in filtered_songs)
             ordered_singer_names = sorted(singer_names)
             return Response({"singer_names":list(ordered_singer_names)})  
        #filtering based on singer featching song title
        elif singer_name is not None:
             filter_name = Song.objects.filter(singer__name=singer_name)
             singer_title = [song.title for song in filter_name] 
             ordered_singer_names = sorted(singer_title)
             return Response({"song_title":ordered_singer_names})
        
        elif start_letter is not None:
             filter_title = Song.objects.filter(title__istartswith=start_letter)
             song_title = [song.title for song in filter_title]
             singer_name = [song.singer.name for song in filter_title]
             return Response({"songs_startswith":song_title,"Singer_name":singer_name})

        else:
            return super().list(request) 

      #**********By action Decorators***********
    # @action(detail=False, methods=['get'])
    # def retrive_fun(self, request, *args, **kwargs):
    #     song_duration = (request.query_params.get('duration'))
    #     if song_duration is not None:
    #             song_duration = int(song_duration)
    #             filtered_songs = Song.objects.filter(duration=song_duration)
    #             singer_names = [song.singer.name for song in filtered_songs]
    #             return Response({"singer_names": singer_names})
    #     else:
    #          return Response({"error": "Invalid song_duration value. It should be an integer."}, status=400)        
        



   
        

    
#**************retriving in the different class*********************************
# class SingerWithSongDurationViewSet(viewsets.ViewSet):
    # serializer_class = Songserializer
    # def list(self, request, *args, **kwargs):
        # song_duration = request.query_params.get('duration')
        # if song_duration is not None:
        #     try:
        #         song_duration = int(song_duration)
        #         filtered_songs = Song.objects.filter(duration=song_duration)
        #         singer_names = [song.singer.name for song in filtered_songs]
        #         return Response({"singer_names": singer_names})
        #     except ValueError:
        #         return Response({"error": "Invalid song_duration value. It should be an integer."}, status=400)
            
        
             
    


























#     serializer_class = Songserializer
#     def list(self, request):

#         song_duration = int(request.query_params.get('duration', 0))

#         # Filter songs with song_duration equal to 3
#         songs_with_duration_3 = Song.objects.filter(duration = song_duration)

#         # Extract the names of the singers from the filtered songs
#         singer_names = [song.title for song in songs_with_duration_3]

#         serializer = self.get_serializer(singer_names, many=True)

#         return Response(serializer.data)
    
      #*******Queryset for unique value*************
    # def list(self, request, *args, **kwargs):
    #     song_duration = request.query_params.get('duration')
    #     if song_duration is not None:
    #         try:
    #             song_duration = int(song_duration)
    #             filtered_songs = Song.objects.filter(duration=song_duration)

    #             # Use a set to store unique singer names
    #             unique_singer_names = set(song.singer.name for song in filtered_songs)

    #             return Response({"singer_names": list(unique_singer_names)})
    #         except ValueError:
    #             return Response({"error": "Invalid song_duration value. It should be an integer."}, status=400)
    #     else:
    #         return super().list(request, *args, **kwargs) 
        