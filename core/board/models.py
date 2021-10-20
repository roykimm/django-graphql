from django.db import models

# Create your models here.
class Board(models.Model):
    no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    note = models.TextField()
    writer = models.CharField(max_length=255)
    parent_no = models.IntegerField(default=0)
    count = models.IntegerField(default=0)
    insert_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now_add=True)
    usage_flag = models.CharField(max_length=10, default='1')

    def __str__(self):
        return f"제목: {self.title}, 작성자 : {self.writer}"