from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from apps.mountains.models import Mountain, Climb


class ClimbTest(TestCase):
    def setUp(self):
        User.objects.create(
            username = "test_user",
            email = "test@testemail.com",
            password = "testpassword",
        )

        Mountain.objects.create(
            name = "Test Mountain",
            elevation = 14000,
            difficulty = "So Hard",
            lat = 2.4584,
            long = -204.4548,
        )


    def test_save_climb_with_correct_info(self):
        now = datetime.now()

        test_climb = Climb.objects.create(
            climber = User.objects.get(username="test_user"),
            mountain = Mountain.objects.get(name="Test Mountain"),
            start_date = now.strftime('%Y-%m-%d'),
            summit_date = now.strftime('%Y-%m-%d'),
            finish_date = now.strftime('%Y-%m-%d'),
            start_time = now.strftime("%X"),
            summit_time = now.strftime("%X"),
            finish_time = now.strftime("%X"),
            total_distance = 5,
            notes = "Climbed a mountain"
        )

        self.assertEquals(test_climb, Climb.objects.get(mountain="Test Mountain"), "Mountain could not be created.")


    def test_save_with_missing_field(self):
        now = datetime.now()

        try:
            test_climb = Climb.objects.create(
                climber = User.objects.get(username="test_user"),
                mountain = Mountain.objects.get(name="Test Mountain"),
                summit_date = now.strftime('%Y-%m-%d'),
                finish_date = now.strftime('%Y-%m-%d'),
                start_time = now.strftime("%X"),
                summit_time = now.strftime("%X"),
                finish_time = now.strftime("%X"),
                total_distance = 5,
                notes = "Climbed a mountain"
            )
        except:
            test_climb = None

        self.assertEquals(test_climb, None, "Climb should not save without missing field")


    def test_save_with_invalid_date(self):
        now = datetime.now()

        try:
            test_climb = Climb.objects.create(
                climber = User.objects.get(username="test_user"),
                mountain = Mountain.objects.get(name="Test Mountain"),
                summit_date = now.isoformat(),
                finish_date = now.strftime('%Y-%m-%d'),
                start_time = now.strftime("%X"),
                summit_time = now.strftime("%X"),
                finish_time = now.strftime("%X"),
                total_distance = 5,
                notes = "Climbed a mountain"
            )
        except:
            test_climb = None

        self.assertEquals(test_climb, None, "Climb should not save with incorrect date format")
