
from django.core.management.base import BaseCommand
from django.test.runner import DiscoverRunner
import io
import sys

class Command(BaseCommand):
    help = 'Run tests and output results'

    def handle(self, *args, **kwargs):
        test_runner = DiscoverRunner()
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        failures = test_runner.run_tests(['news'])  # Adjust the app name as needed

        sys.stdout = old_stdout
        test_output = new_stdout.getvalue()

        self.stdout.write(self.style.SUCCESS('Test results:\n'))
        self.stdout.write(test_output)
        if failures:
            self.stdout.write(self.style.ERROR('Some tests failed.'))
        else:
            self.stdout.write(self.style.SUCCESS('All tests passed.'))
