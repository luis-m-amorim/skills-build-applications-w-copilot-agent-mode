from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Check contents of the database using Django models'

    def handle(self, *args, **kwargs):
        collections = {
            'User': User,
            'Team': Team,
            'Activity': Activity,
            'Leaderboard': Leaderboard,
            'Workout': Workout,
        }

        for name, model in collections.items():
            count = model.objects.count()
            first_record = model.objects.first()
            self.stdout.write(f"{name} - Count: {count}, First Record: {first_record}")
