from rest_framework import serializers

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class StringIdModelSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['id'] = str(instance.pk)
        return data


class TeamSerializer(StringIdModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'motto')


class UserSerializer(StringIdModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'team')


class ActivitySerializer(StringIdModelSerializer):
    class Meta:
        model = Activity
        fields = ('id', 'user', 'activity_type', 'duration_minutes', 'calories_burned', 'logged_at')


class LeaderboardSerializer(StringIdModelSerializer):
    class Meta:
        model = Leaderboard
        fields = ('id', 'user', 'score', 'rank')


class WorkoutSerializer(StringIdModelSerializer):
    class Meta:
        model = Workout
        fields = ('id', 'user', 'name', 'difficulty', 'description')
