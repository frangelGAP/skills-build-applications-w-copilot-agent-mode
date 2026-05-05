from rest_framework import serializers
from .models import User, Team, Activity, Workout, Leaderboard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'team']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'user', 'type', 'duration', 'distance', 'timestamp']

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'description', 'suggested_for']

class LeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ['id', 'team', 'points']
