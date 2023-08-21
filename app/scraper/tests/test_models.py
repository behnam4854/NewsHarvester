
from django.test import TestCase
from scraper.models import Headline, Source, Sentiment

class ModelsTestCase(TestCase):

    def setUp(self):
        self.source = Source.objects.create(
            name='Hacker News', 
            url='https://news.ycombinator.com'
        )

        self.headline = Headline.objects.create(
            title='Example Headline',
            content='Some interesting content',
            url='https://example.com/article',
            published_date='2023-02-28 14:00:00',
            # source=self.source
        )

        self.sentiment = Sentiment.objects.create(
            headline=self.headline,
            sentiment='positive',
            confidence=0.95
        )

    def test_headline_str(self):
        self.assertEqual(str(self.headline), 'Example Headline')

    def test_source_str(self):
        self.assertEqual(str(self.source), 'Hacker News')

    def test_sentiment_str(self):
        self.assertEqual(str(self.sentiment), 'Example Headline - positive')