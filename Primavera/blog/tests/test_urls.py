from django.test import TestCase
from django.urls import reverse, resolve, path
from blog.views import  post_detail, posts, posting
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from blog.models import Post

class BlogTestCase(TestCase):
    
    def setUp(self):
        self.post = Post.objects.create(title='Test Post', description='This is a test post.', 
                                        image='blog/images/test.png', date=timezone.now())

    def test_render_posts_view(self):
        response = self.client.get(reverse('blog:posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts.html')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)

    def test_post_detail_view(self):
        response = self.client.get(reverse('blog:post_detail', args=[self.post.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_detail.html')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.description)

    def test_posting_view(self):
        response = self.client.post(reverse('blog:posting'), {
            'title': 'New Test Post',
            'description': 'This is a new test post.',
            'image': 'blog/images/new_test.png',
            'date': timezone.now()
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.count(), 2)
