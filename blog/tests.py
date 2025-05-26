from django.test import TestCase
from django.urls import reverse
from .models import Author, Tag, Post

class ModelsTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name='Test', last_name='User', email='test@example.com')
        self.tag = Tag.objects.create(tag='testtag')
        self.post = Post.objects.create(
            title='Títol', excerpt='Excerpt', image_name='img.jpg',
            date='2024-01-01', slug='titoli', content='Contingut', author=self.author
        )
        self.post.tags.add(self.tag)

    def test_author_str(self):
        self.assertEqual(str(self.author), 'Test User')

    def test_tag_unique(self):
        with self.assertRaises(Exception):
            Tag.objects.create(tag='testtag')

    def test_post_relation(self):
        self.assertIn(self.post, self.author.posts.all())
        self.assertIn(self.post, self.tag.posts.all())

class ViewsTest(TestCase):
    def setUp(self):
        a = Author.objects.create(first_name='A', last_name='B', email='a@b.com')
        t = Tag.objects.create(tag='t1')
        p = Post.objects.create(title='P', excerpt='E', image_name='i.jpg', date='2024-01-01', slug='p', content='C', author=a)
        p.tags.add(t)

    def test_index(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_post_detail_404(self):
        resp = self.client.get('/posts/no-existeix/')
        self.assertEqual(resp.status_code, 404)
