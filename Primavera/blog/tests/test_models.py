
from django.test import TestCase
from .models import Post


class PostModelTestCase(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(title='Test post', description='Test description')
        self.assertEqual(post.title, 'Test post')
        self.assertEqual(post.description, 'Test description')


    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 100)

    def test_date_default_value(self):
        post = Post.objects.get(id=1)
        date = post.date
        self.assertEqual(date, '2022-03-25')
