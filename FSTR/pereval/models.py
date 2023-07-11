from django.db import models


class User(models.Model):
    """Класс модели пользователя"""
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=12)
    fam = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    otc = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Coords(models.Model):
    """Класс модели координат перевала"""
    latitude = models.DecimalField(verbose_name='Latitude', max_digits=9, decimal_places=6, null=True)
    longitude = models.DecimalField(verbose_name='Longitude', max_digits=9, decimal_places=6, null=True)
    height = models.IntegerField(verbose_name='Height', null=True)


class Level(models.Model):
    winter = models.CharField(max_length=10, verbose_name='Winter', null=True, blank=True)
    summer = models.CharField(max_length=10, verbose_name='Summer', null=True, blank=True)
    autumn = models.CharField(max_length=10, verbose_name='Autumn', null=True, blank=True)
    spring = models.CharField(max_length=10, verbose_name='Spring', null=True, blank=True)

    def __str__(self):
        return f'{self.winter} {self.summer} {self.autumn} {self.spring}'


class Image(models.Model):
    title = models.CharField(blank=True, null=True)
    data_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'id: {self.pk}, title:{self.title} {self.image}'


class Pereval(models.Model):

    NEW = 'new'
    PENDING = 'pending'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'

    CHOICES_MODER = [
        (NEW, 'new'),
        (PENDING, 'pending'),
        (ACCEPTED, 'accepted'),
        (REJECTED, 'rejected'),
    ]

    beauty_title = models.CharField(max_length=30, null=False)
    title = models.CharField(max_length=30, null=False)
    other_titles = models.CharField(max_length=30, null=False)
    connect = models.CharField(max_length=30, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=CHOICES_MODER, default=NEW)
    coords = models.ForeignKey('Coords', on_delete=models.CASCADE)
    image = models.ForeignKey('Image', on_delete=models.CASCADE)
    level = models.ForeignKey('Level', on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.beauty_title} {self.title} {self.other_titles} id: {self.pk}'