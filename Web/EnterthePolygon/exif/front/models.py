from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from uuid import uuid4
from exif.settings import MEDIA_ROOT, RABBIT_HOST

from django.db.models.signals import post_save
from django.dispatch import receiver

import pickle, pika
from base64 import b64encode


def upld_dir(instance, filename):
    return 'user-{0}/{1}'.format(instance.user.id, uuid4())

class images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(default="image", max_length=60, blank=False)
    ifile = models.ImageField(unique=True, upload_to=upld_dir)
    rating = models.IntegerField(default = 0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    #comment = models.CharField(max_length=120)

    def get_upldName(self):
        return self.ifile.name.split('/')[-1]

    def get_renderUrl(self):
        return None

@receiver(post_save, sender=images)
def victimVisit(sender, instance, **kwargs):
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBIT_HOST))
    channel = connection.channel()
    channel.queue_declare(queue='victim')
    channel.basic_publish(exchange='',
                      routing_key='victim',
                      body=b64encode(pickle.dumps({"user_id":instance.user_id, "filename":instance.ifile.name.split('/')[-1]})))
