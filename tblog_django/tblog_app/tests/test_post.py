from django.test import TestCase
from tblog_app.views import PostView
from django.http import HttpRequest
from tblog_app.models import Post, Tag


class PostViewTestCase(TestCase):
    def setUp(self):
        Post.objects.create(id=1, title='test_title', body='test_body', description='test_description')
        p = Post.objects.create(id=2, title='test_title', body='test_body', description='test_description')
        t = Tag.objects.create(name='wonzzang')
        p.tags.add(t)
        self.p = PostView()

    def _request_tag_param(self) -> HttpRequest:
        ret = HttpRequest()
        ret.GET['tag'] = 'wonzzang'
        return ret

    def _request_no_param(self) -> HttpRequest:
        return HttpRequest()

    def test_get_query_set(self):
        tests = [
            {
                'name': 'Normal1',
                'args': {
                    'request': self._request_tag_param()
                },
                'expected': ["<Post: 2>"]
            },
            {
                'name': 'Normal2',
                'args': {
                    'request': self._request_no_param()
                },
                'expected': ["<Post: 2>", "<Post: 1>"]
            },
        ]

        for tt in tests:
            self.assertQuerysetEqual(self.p._get_query_set(tt['args']['request']), tt['expected'])
