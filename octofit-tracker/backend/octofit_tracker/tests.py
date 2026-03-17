from django.test import TestCase
from rest_framework.test import APIClient

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class OctofitCollectionsApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        marvel_team = Team.objects.create(name='marvel 팀', motto='Avengers Assemble')
        user = User.objects.create(name='Iron Man', email='ironman@test.com', team=marvel_team)
        Activity.objects.create(
            user=user,
            activity_type='Running',
            duration_minutes=30,
            calories_burned=300,
        )
        Leaderboard.objects.create(user=user, score=1000, rank=1)
        Workout.objects.create(
            user=user,
            name='Arc Reactor Core',
            difficulty='hard',
            description='Full-body strength circuit',
        )

    def test_users_endpoint_returns_200(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_teams_endpoint_returns_200(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_activities_endpoint_returns_200(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_leaderboard_endpoint_returns_200(self):
        response = self.client.get('/api/leaderboard/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)

    def test_workouts_endpoint_returns_200(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.json()), 1)
