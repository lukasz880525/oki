#coding: utf-8
from __future__ import unicode_literals,absolute_import
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(verbose_name=_('first_name'),max_length=20)
    last_name = models.CharField(verbose_name=_('last_name'),max_length=50)

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name,last_name=self.last_name)


    class Meta:
        ordering = ('last_name','first_name')
        verbose_name = _('author')
        verbose_name_plural = _('authors')



class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)
    # author = models.ForeignKey(Author)


    def __str__(self):
        return self.title

    def get_absolute_url(self):   # drugi sposób wyswietlania - zobacz author_detail.html
        return reverse_lazy('shelf:book-detail',kwargs={'pk':self.id})

class BookEdition(models.Model):
    isbn = models.CharField(max_length=17,blank=True)
    publisher = models.ForeignKey(Publisher)
    book = models.ForeignKey(Book, related_name='editions')
    date = models.DateField()

    def __str__(self):
        return '{book.title},{publisher.name}'.format(book=self.book,publisher=self.publisher)




COVER_TYPES = (
    ('soft','soft'),
    ('hard','hard')
)

class BookItem(models.Model):
    edition = models.ForeignKey(BookEdition)
    catalogue_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4,choices=COVER_TYPES)

    def __str__(self):
        return '(edition),(cover)'.format(edition=self.edition,cover=self.cover_type_display())
















