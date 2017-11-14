from django.test import TestCase
from .models import Editor,Article,tags
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):
    '''
    Test case for Editor class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up an Editor instance before each test
        '''
        self.new_editor = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')

    def test_instance(self):
        '''
        Test case to check if self.new_editor in an instance of Editor class
        '''
        self.assertTrue( isinstance(self.new_editor, Editor) )

    def test_save_editor(self):
        '''
        Test case to check is an editor is saved in the database
        '''
        self.new_editor.save_editor()
        editors = Editor.objects.all()
        self.assertTrue( len(editors) > 0 )

    def test_delete_editor(self):
        '''
        Test case to check if an editor is deleted from the database
        '''
        self.new_editor.save_editor()
        editors = Editor.objects.all()
        self.new_editor.delete_editor()
        self.assertTrue( len(editors) == 0)

    def test_get_editors(self):
        '''
        Test case to check if all editors are gotten from the database
        '''
        self.new_editor.save_editor()
        gotten_editors = Editor.get_editors()
        editors = Editor.objects.all()
        self.assertTrue( len(gotten_editors) == len(editors))

class tagsTestClass(TestCase):
    '''
    Test case for tags class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up a tags instance before each test
        '''
        self.new_tag = tags(name='Python')

    def test_instance(self):
        '''
        Test case to check if self.new_tag in an instance of tags class
        '''
        self.assertTrue( isinstance(self.new_tag, tags) )

    def test_save_editor(self):
        '''
        Test case to check is a tag is saved in the database
        '''
        self.new_tag.save_tag()
        gotten_tags = tags.objects.all()
        self.assertTrue( len(gotten_tags) > 0 )

    def test_delete_tag(self):
        '''
        Test case to check if a tag is deleted from the database
        '''
        self.new_tag.save_tag()
        gotten_tags = tags.objects.all()
        self.new_tag.delete_tag()
        self.assertTrue( len(gotten_tags) == 0 )

    def test_get_tags(self):
        '''
        Test case to check if all tags are gotten from the database
        '''
        self.new_tag.save_tag()
        gotten_tags = tags.get_tags()
        existing_tags = tags.objects.all()
        self.assertTrue( len(gotten_tags) == len(existing_tags))

class ArticleTestClass(TestCase):
    '''
    Test case for Article class
    '''

    # Set Up method
    def setUp(self):
        '''
        Method that sets up an Article instance before each test
        '''
        # Create and save an editor
        self.james = Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Create and save a tag
        self.tag = tags(name='Testing')
        self.tag.save_tag()

        self.new_article = Article(title = 'Python James', post ='Python James is Muriuki who wrote Python content for Moringa School', editor=self.james)
        self.new_article.save_article()

        self.new_article.tags.add(self.tag)

    # def tearDown(self):
    #     '''
    #     Method to delete instances of models after each test
    #     '''
    #     Editor.objects.all().delete()
    #     tags.objects.all().delete()
    #     Article.objects.all().delete()

    def test_instance(self):
        '''
        Test case to check if self.new_article in an instance of Article class
        '''
        self.assertTrue( isinstance(self.new_article, Article) )

    def test_save_article(self):
        '''
        Test case to check is an Article is saved in the database
        '''
        self.james.save_editor()
        self.new_article.save_article()
        artilces = Article.objects.all()
        self.assertTrue( len(artilces) > 0 )

    def test_delete_article(self):
        '''
        Test case to check if an article is deleted from the database
        '''
        self.new_article.save_article()
        artilces = Article.objects.all()
        self.new_article.delete_article()
        self.assertTrue( len(artilces) == 0 )

    def test_get_articles(self):
        '''
        Test case to check if all articles are gotten from the database
        '''
        self.new_article.save_article()
        gotten_articles = Article.get_articles()
        artilces = Article.objects.all()
        self.assertTrue( len(gotten_articles) == len(artilces))

    def test_get_news_today(self):
        '''
        Test case to check if today's news is gotten from the database
        '''
        self.new_article.save_article()
        today_news = Article.todays_news()
        self.assertTrue( len(today_news) > 0)

    def test_get_news_by_date(self):
        '''
        Test case to check if news is from a given date is gotten from a given day
        '''
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue( len(news_by_date) == 0)





