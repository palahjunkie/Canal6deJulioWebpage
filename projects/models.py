from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

FISICO = (
    (0, "No Disponible"),
    (1, "Disponible")
)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)     
    def __str__(self):
        return self.name

class Project(models.Model):
    #owner =
    title = models.CharField(max_length=200)
    year = models.IntegerField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, default='default.png')
    vimeo_link = models.CharField(max_length=1000, null=True, blank=True)
    renta_link = models.CharField(max_length=1000, null=True, blank=True)
    source_link = models.CharField(max_length=1000, null=True, blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    disponible_fisico = models.IntegerField(choices=FISICO, default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
        
     
    def __str__(self):
        return self.title
    
    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img        
    

class Entrada(models.Model):
     

    #owner =
    title = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    fotografo = models.TextField(max_length=280, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    subtitle = models.TextField(max_length=280, null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    class Meta:
        ordering = ['-created_on'] 
    def __str__(self):
        return self.title  
    @property
    def imageURL(self):
        try:
            img = self.featured_image.url
        except:
            img = ''
        return img   
   
class Review(models.Model):
    
    VOTE_TYPE = (
        ('up', 'up'),
        ('down', 'down'),
    )
    
    #owner =
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    def __str__(self):
        return self.value
    
class Contacto(models.Model):
    
    nombre = models.CharField(max_length=280)
    mail = models.EmailField()
    titulo= models.CharField(max_length=280)
    contenido = models.TextField(max_length=4000)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.nombre + '    ' + self.titulo
        