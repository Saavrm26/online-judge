"""
Django command to wait for database to initialize
"""

import time


from psycopg2 import OperationalError as Psycopg2OpError

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    help = "Wait for database to setup itself"

    def handle(self, *args, **options):
        """ Entrypoint for command """
        self.stdout.write('Waiting for database')
        db_conn = connections['default']
        db_ready = False
        while (not db_ready):
            try:
                db_conn.cursor()
                db_ready = True

            except OperationalError:
                self.stdout.write('Databse not ready. retrying after 1 second')
                time.sleep(1)
            except Psycopg2OpError:
                self.stdout.write(
                    'Database not ready, retrying after 1 second')
                time.sleep(1)
            except Exception as e:
                self.stdout.write(e)
                exit(1)
        self.stdout.write(self.style.SUCCESS('Database Ready'))
