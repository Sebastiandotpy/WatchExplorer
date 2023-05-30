from django.core.management.base import BaseCommand
from watchlist.models import WatchData
from crawler import scrape_watch_data
from datetime import datetime, timedelta

def convert_post_date(post_date):
    if post_date == "0 min ago":
        new_date = datetime.now() - timedelta(minutes=1)
        post_date = new_date.strftime("%Y-%m-%d %H:%M:%S")
    return post_date

class Command(BaseCommand):
    help = 'Crawls watch data and saves it to the database'

    def handle(self, *args, **options):
        scrape_watch_data()
        watch_data_list = WatchData.objects.all()
        for watch_data in watch_data_list:
            watch_data.post_date = convert_post_date(watch_data.post_date)
            watch_data.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully saved watch data: {watch_data}'))
