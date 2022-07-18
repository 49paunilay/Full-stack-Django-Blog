from tabnanny import verbose
from django.db import models
from django.utils.html import format_html

# Create your models here.

class Category(models.Model):
    cat_Id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/category')
    add_date = models.DateTimeField(auto_now_add=True,null=True) 

    def __str__(self):
        return str(self.title) + ' ' +str(self.cat_Id)
    
    def image_tag(self):
        return format_html('<img src="/{}" style="width:40px;height:40px"/>'.format(self.image))
    
    class Meta:
        verbose_name_plural = "categories"
 

class Post(models.Model):
    postId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category,on_delete=models.CASCADE)
    mage = models.ImageField(upload_to='media/posts')
    author = models.CharField(max_length=250,blank=True)
    likes = models.IntegerField(default=0)
    


    def image_tag(self):
        return format_html('<img src="/{}" style="width:40px;height:40px"/>'.format(self.mage))

class ContactUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    contact_comment = models.TextField()
    date_time_of_comment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + ' ' +'has commented ' + self.contact_comment


class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    username = models.CharField(max_length=350)
    body=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']
        verbose_name_plural = "Comments"
        
    
    def __str__(self):
        return '{} has made {} comment '.format(self.username,self.body)

class AdminTasks(models.Model):
    taskName = models.CharField(max_length=500)
    description = models.TextField(default='Admin E-Mail Address')

    class Meta:
        verbose_name_plural = " Admin Tasks"

    def __str__(self):
        return self.taskName


