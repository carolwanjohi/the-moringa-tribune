from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    '''
    Class that defines an Editor for an article
    '''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        # return ' %s' %  (self.first_name)
        return self.first_name

    class Meta:
        ordering = ['first_name']

    def save_editor(self):
        '''
        Method to save a new Editor to the database
        '''
        self.save()

    def delete_editor(self):
        '''
        Method to delete an Editor from the database
        '''
        self.delete()

    @classmethod
    def get_editors(cls):
        '''
        Method that gets all editors from the database

        Returns:
            editors : list of editor objects from the database
        '''
        editors = Editor.objects.all()
        return editors


class tags(models.Model):
    '''
    Class that defines Tags for an Article
    '''
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tag(self):
        '''
        Method to save a new tag to the database
        '''
        self.save()

    def delete_tag(self):
        '''
        Method to delete a tag from the database
        '''
        self.delete()

    @classmethod
    def get_tags(cls):
        '''
        Method that gets all tags from the database

        Returns:
            gotten_tags : list of tag objects from the database
        '''
        gotten_tags = tags.objects.all()
        return gotten_tags

class Article(models.Model):
    '''
    Class that defines an Article
    '''
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def save_article(self):
        '''
        Method to save a new Article to the database
        '''
        self.save()

    def delete_article(self):
        '''
        Method to delete an Article from the database
        '''
        self.delete()

    @classmethod
    def get_articles(cls):
        '''
        Method that gets all articles from the database

        Returns:
            articles : list of article objects from the database
        '''
        articles = Article.objects.all()
        return articles

    @classmethod
    def todays_news(cls):
        '''
        Method that gets today's news

        Returns:
            news : list of today's news objects from the database
        '''
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news

    @classmethod
    def days_news(cls,date):
        '''
        Method that gets news of a specific date

        Args:
            date : specific date from the user

        Returns
            news : list of news objects from the database with the specified date
        '''
        news = cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        '''
        Method that gets news matching the specific search term

        Args:
            search_term : specific title from the user

        Returns
            news : list of news objects from the database matching the specific search term
        '''
        news = cls.objects.filter(title__icontains=search_term)
        return news


