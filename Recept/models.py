from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    primary = models.CharField(max_length=255)
    secondary = models.CharField(max_length=255, blank=True)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)

    def get_absolute_url(self):
        return '/recipes/%s/' % self.pk

    class Meta:
        ordering = ['name']


class RecipeForWeek(models.Model):
    recipes = models.ManyToManyField(Recipe)

    year = models.IntegerField()
    week = models.IntegerField()

    def __str__(self):
        return '%sw%s' % (self.year, self.week)

    def __repr__(self):
        return str(self)

    def get_absolute_url(self):
        return '/history/%s/' % self.pk

    class Meta:
        ordering = ['year', 'week']
        unique_together = ('year', 'week')
