from django.db import models

# Create your models here.
class Reader:
    def __init__(self, path, result):
        self.path = path
        self.result = result