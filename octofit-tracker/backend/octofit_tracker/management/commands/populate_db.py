from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        marvel_team = Team.objects.create(name='marvel 팀', motto='Avengers Assemble')
        dc_team = Team.objects.create(name='dc 팀', motto='Justice League Unite')

        users = [
            User.objects.create(name='Iron Man', email='ironman@octofit.com', team=marvel_team),
            User.objects.create(name='Captain America', email='captain@octofit.com', team=marvel_team),
            User.objects.create(name='Spider-Man', email='spiderman@octofit.com', team=marvel_team),
            User.objects.create(name='Superman', email='superman@octofit.com', team=dc_team),
            User.objects.create(name='Batman', email='batman@octofit.com', team=dc_team),
            User.objects.create(name='Wonder Woman', email='wonderwoman@octofit.com', team=dc_team),
        ]

        activities = [
            ('Running', 45, 430),
            ('Cycling', 60, 520),
            ('HIIT', 30, 350),
            ('Swimming', 40, 410),
            ('Strength Training', 50, 480),
            ('Yoga', 35, 210),
        ]

        for user, activity in zip(users, activities):
            activity_type, duration, calories = activity
            Activity.objects.create(
                user=user,
                activity_type=activity_type,
                duration_minutes=duration,
                calories_burned=calories,
            )

        scores = [980, 930, 900, 970, 940, 910]
        sorted_user_score = sorted(zip(users, scores), key=lambda item: item[1], reverse=True)
        for rank_index, (user, score) in enumerate(sorted_user_score, start=1):
            Leaderboard.objects.create(user=user, score=score, rank=rank_index)

        workouts = [
            ('Arc Reactor Core', 'hard', 'Full-body strength circuit'),
            ('Shield Sprint', 'medium', 'Interval running with resistance bands'),
            ('Web Mobility', 'easy', 'Agility and mobility focused workout'),
            ('Krypton Power', 'hard', 'Heavy lifting with short rests'),
            ('Gotham Core', 'medium', 'Core endurance and bodyweight routine'),
            ('Amazon Balance', 'easy', 'Balance and flexibility session'),
        ]

        for user, workout in zip(users, workouts):
            workout_name, difficulty, description = workout
            Workout.objects.create(
                user=user,
                name=workout_name,
                difficulty=difficulty,
                description=description,
            )

        self.stdout.write(self.style.SUCCESS('octofit_db 테스트 데이터 적재 완료'))
