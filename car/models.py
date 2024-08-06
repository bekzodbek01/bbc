from django.db import models


class Logo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='Logo/image/', blank=True, null=True)
    order = models.IntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Logo'
        verbose_name_plural = 'Logo'

    def __str__(self):
        return self.title


class Car(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    filed_km = models.IntegerField()
    year = models.IntegerField()
    order = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    logo = models.ForeignKey(Logo, on_delete=models.CASCADE, related_name='logo', blank=True, null=True)
    color = models.CharField(max_length=15, blank=True, null=True)
    image = models.FileField(upload_to='Car/image/', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.title


class Contract(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='cars', blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contract'
        verbose_name_plural = 'Contract'


class Contractsub(models.Model):
    inital_payment = models.IntegerField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='contract', blank=True, null=True)

    def __str__(self):
        return f"{self.inital_payment}  {self.month} oy % {self.year} yil 20 % "


class Slider(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='Slider/image/', blank=True, null=True)
    order = models.IntegerField(default=0)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Slider'

    def __str__(self):
        return self.title


