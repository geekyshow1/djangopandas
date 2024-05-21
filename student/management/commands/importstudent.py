import pandas as pd
from django.core.management.base import BaseCommand
from student.models import Student
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Import student from csv file'

    def handle(self, *args, **kwargs):

        # Define the path to the 'data' folder.
        data_dir = os.path.join(settings.BASE_DIR, 'data')

        # Create the full path to the csv file.
        csv_file_path = os.path.join(data_dir, 'sample.csv')

        try:
            # Load the CSV file into a DataFrame
            df = pd.read_csv(csv_file_path)

            # Fill missing values
            df['name'] = df['name'].fillna(value='Unknown')
            df['age'] = df['age'].ffill()
            df['city'] = df['city'].fillna(value='Unknown')

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('CSV file not found.'))
            return

        for _, row in df.iterrows():
            Student.objects.create(
                name=row['name'],
                age=row['age'],
                city=row['city']
            )
        self.stdout.write(self.style.SUCCESS(
            'Successfully imported students.'))
