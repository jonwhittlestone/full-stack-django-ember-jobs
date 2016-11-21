from django.test import TestCase, RequestFactory

class IndexViewTestCase(TestCase):

    # Todo. Test using APIRequestFactory

    def setUp(self):
        self.factory = RequestFactory()