from .models import User, Team, Activity, Leaderboard, Workout
from rest_framework.serializers import ModelSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.hashers import make_password
import os

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['_id', 'username', 'email']

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

class ActivitySerializer(ModelSerializer):
    class Meta:
        model = Activity
        fields = ['_id', 'user', 'activity_type', 'duration']

class LeaderboardSerializer(ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['_id', 'user', 'score']

class WorkoutSerializer(ModelSerializer):
    class Meta:
        model = Workout
        fields = ['_id', 'name', 'description']

@api_view(['GET'])
def api_root(request, format=None):
    base_url = "https://reimagined-space-invention-69gpvxv4rgxr357x6-8000.app.github.dev/api/"  # Explicitly include the codespace name
    return Response({
        'users': f"{base_url}users/",
        'teams': f"{base_url}teams/",
        'activities': f"{base_url}activity/",
        'leaderboard': f"{base_url}leaderboard/",
        'workouts': f"{base_url}workouts/",
    })

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Hash the password before saving the user
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
