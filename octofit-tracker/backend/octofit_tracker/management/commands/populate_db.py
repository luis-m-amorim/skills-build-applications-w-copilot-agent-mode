from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(_id=ObjectId(), username='thundergod', email='thundergod@mhigh.edu', password='thundergodpassword'),
            User(_id=ObjectId(), username='metalgeek', email='metalgeek@mhigh.edu', password='metalgeekpassword'),
            User(_id=ObjectId(), username='zerocool', email='zerocool@mhigh.edu', password='zerocoolpassword'),
            User(_id=ObjectId(), username='crashoverride', email='crashoverride@mhigh.edu', password='crashoverridepassword'),
            User(_id=ObjectId(), username='sleeptoken', email='sleeptoken@mhigh.edu', password='sleeptokenpassword'),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(_id=ObjectId(), name='Blue Team', members=[str(users[0]._id), str(users[1]._id)]),
            Team(_id=ObjectId(), name='Gold Team', members=[str(users[2]._id), str(users[3]._id), str(users[4]._id)]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(_id=ObjectId(), user=users[0]._id, activity_type='Cycling', duration=int(timedelta(hours=1).total_seconds())),
            Activity(_id=ObjectId(), user=users[1]._id, activity_type='Crossfit', duration=int(timedelta(hours=2).total_seconds())),
            Activity(_id=ObjectId(), user=users[2]._id, activity_type='Running', duration=int(timedelta(hours=1, minutes=30).total_seconds())),
            Activity(_id=ObjectId(), user=users[3]._id, activity_type='Strength', duration=int(timedelta(minutes=30).total_seconds())),
            Activity(_id=ObjectId(), user=users[4]._id, activity_type='Swimming', duration=int(timedelta(hours=1, minutes=15).total_seconds())),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(_id=ObjectId(), user=users[0], score=100),
            Leaderboard(_id=ObjectId(), user=users[1], score=90),
            Leaderboard(_id=ObjectId(), user=users[2], score=95),
            Leaderboard(_id=ObjectId(), user=users[3], score=85),
            Leaderboard(_id=ObjectId(), user=users[4], score=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(_id=ObjectId(), name='Cycling Training', description='Training for a road cycling event'),
            Workout(_id=ObjectId(), name='Crossfit', description='Training for a crossfit competition'),
            Workout(_id=ObjectId(), name='Running Training', description='Training for a marathon'),
            Workout(_id=ObjectId(), name='Strength Training', description='Training for strength'),
            Workout(_id=ObjectId(), name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        # Print counts for each collection
        collections = {
            'User': User,
            'Team': Team,
            'Activity': Activity,
            'Leaderboard': Leaderboard,
            'Workout': Workout,
        }

        for name, model in collections.items():
            count = model.objects.count()
            self.stdout.write(f"{name} - Count: {count}")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
