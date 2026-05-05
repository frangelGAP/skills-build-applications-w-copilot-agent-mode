from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Workout, Leaderboard

class UserTests(APITestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        url = reverse('user-list')
        data = {'username': 'testuser', 'email': 'test@example.com', 'password': 'testpass123', 'team': team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Team Alpha'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass123', team=team)
        url = reverse('activity-list')
        data = {'user': user.id, 'type': 'run', 'duration': 30, 'distance': 5.0}
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        team = Team.objects.create(name='Test Team')
        url = reverse('workout-list')
        data = {'name': 'Morning Run', 'description': 'A quick run', 'suggested_for': team.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        url = reverse('leaderboard-list')
        data = {'team': team.id, 'points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
