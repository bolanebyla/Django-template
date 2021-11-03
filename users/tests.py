from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(username='normal_user', password='foo')
        self.assertEqual(user.username, 'normal_user')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        self.assertIsNotNone(authenticate(username='normal_user', password='foo'))

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(ValueError):
            User.objects.create_user(username='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(username='super_user', password='foo')
        self.assertEqual(admin_user.username, 'super_user')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        self.assertIsNotNone(authenticate(username='super_user', password='foo'))

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='super_user', password='foo', is_superuser=False)
