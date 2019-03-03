from faker import Faker
import csv
from datetime import time,datetime,timedelta
import datetime

record_count=100
import random

fake=Faker()
"""
def create_csv_file():
    with open('CustomerData.csv', 'w', newline='') as csvfile:
        fieldnames=['Name','Address','Mobile_No','Intime','Outtime','Date','Day','Pax']
        writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()

        for i in range(record_count):
            start_date = datetime.date(year=2015, month=1, day=1)
            end_date = datetime.date(year=2016, month=1, day=1)

            date=fake.date_between(start_date=start_date, end_date=end_date)
            day=date.strftime("%A")
            it=fake.time()
            hour, minute, second = (int(x) for x in it.split(':'))
            #import datetime

            d1 = datetime.datetime(2000, 1, 1, hour, minute, second)



            a = random.randint(1, 10)

            if a==1:
                d2 = d1 + timedelta(minutes=15)
            elif a >= 2 and a <=5:
                d2 = d1 + timedelta(minutes=35)
            else:
                d2 = d1 + timedelta(hours=1,minutes=5)



            writer.writerow({'Name':fake.name(),
                             'Address': fake.address(),
                             'Mobile_No': fake.phone_number(),
                             'Intime': it,
                             'Outtime': d2.time(),
                             'Date':date,
                             'Day':day,
                             'Pax':a,
                            }

                            )
            #print("successfully")

create_csv_file()

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'User.settings'
from django.conf import settings

#settings.configure(DEBUG=True)

from django.conf import settings
if not settings.configured:
    settings.configure( DEBUG=False)
    """
import os
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Project.settings'
os.environ.setdefault('DJANGO_SETTINGS_VALUE','Project.settings')

import django
django.setup()

from User.models import Customer
def save_data():
    for i in range(record_count):
        start_date = datetime.date(year=2015, month=1, day=1)
        end_date = datetime.date(year=2016, month=1, day=1)

        date = fake.date_between(start_date=start_date, end_date=end_date)
        day = date.strftime("%A")
        it = fake.time()
        hour, minute, second = (int(x) for x in it.split(':'))
        # import datetime

        d1 = datetime.datetime(2000, 1, 1, hour, minute, second)

        a = random.randint(1, 10)

        if a == 1:
            d2 = d1 + timedelta(minutes=15)
        elif a >= 2 and a <= 5:
            d2 = d1 + timedelta(minutes=35)
        else:
            d2 = d1 + timedelta(hours=1, minutes=5)
        foo_instance = Customer.objects.create(Name=fake.name(),Address= fake.address(),Mobile_No= fake.phone_number(),Intime= it,Outtime= d2.time(),Date=date,Day=day,Pax=a,)
        foo_instance.save()


save_data()
