from django.conf import settings
from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=25, null=False)
    last_name = models.CharField(max_length=25, null=False)
    email = models.EmailField(max_length=100,
                              null=False)
    phone = models.CharField(max_length=20, null=False)
    mobile = models.CharField(max_length=20, null=False)
    company_name = models.CharField(max_length=250, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name} [{self.company_name}]"


class Contract(models.Model):
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                      on_delete=models.PROTECT)
    client = models.ForeignKey(to='Client',
                               on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    amount = models.FloatField()
    payment_due = models.DateTimeField()

    def __str__(self):
        return f"{self.client.__str__()} - {self.status}"


class Event(models.Model):
    client = models.ForeignKey(to='Client',
                               on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                        on_delete=models.PROTECT)
    event_status = models.ForeignKey(to='EventStatus',
                                     on_delete=models.PROTECT)
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField(max_length=1000, blank=True)
    contract = models.ForeignKey(to='Contract',
                                 on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.client.__str__()} - {self.event_date}"


class EventStatus(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.status}"
