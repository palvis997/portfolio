from django.test import TestCase, Client
from django.urls import reverse
from main.models import Project, BlogPost, ContactMessage


class PortfolioViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PAVIS MUGO MURUGA')

    def test_about_page_loads(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Pavis Mugo Muruga')

    def test_what_i_do_page_loads(self):
        response = self.client.get(reverse('what_i_do'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What I Do')

    def test_skills_page_loads(self):
        response = self.client.get(reverse('skills'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Technical Skills')

    def test_experience_page_loads(self):
        response = self.client.get(reverse('experience'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Industrial Experience')

    def test_projects_page_loads(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Projects &amp; Case Studies')

    def test_project_lab_page_loads(self):
        response = self.client.get(reverse('project_lab'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PROJECT LAB')

    def test_playground_page_loads(self):
        response = self.client.get(reverse('playground'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'TECH PLAYGROUND')

    def test_dashboard_page_loads(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'PAVIS DEVELOPER DASHBOARD')

    def test_credentials_page_loads(self):
        response = self.client.get(reverse('credentials'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Credentials &amp; Endorsements')

    def test_resume_and_cv_page_loads(self):
        response = self.client.get(reverse('resume'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pavis Mugo Muruga')
        self.assertContains(response, 'Kirinyaga University')

        response_cv = self.client.get(reverse('cv_view'))
        self.assertEqual(response_cv.status_code, 200)

    def test_accessibility_statement_loads(self):
        response = self.client.get(reverse('accessibility'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Accessibility Statement')

    def test_contact_page_loads(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Contact Information')

    def test_project_detail_view(self):
        project = Project.objects.create(
            title='Test Project',
            slug='test-project',
            short_description='Test description',
            category='django',
            is_active=True
        )
        response = self.client.get(reverse('project_detail', kwargs={'slug': project.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')

    def test_blog_views(self):
        post = BlogPost.objects.create(
            title='Test Post',
            slug='test-post',
            content='Test content for blog post.',
            published=True
        )
        # List view
        response = self.client.get(reverse('blog_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

        # Detail view
        response = self.client.get(reverse('blog_detail', kwargs={'slug': post.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_contact_form_submission(self):
        response = self.client.post(reverse('contact_submit'), {
            'name': 'Test Recruiter',
            'email': 'recruiter@example.com',
            'phone': '1234567890',
            'subject': 'Internship Opportunity',
            'message': 'Hello Pavis, we would love to connect with you regarding an opportunity.'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, 'Test Recruiter')
        self.assertEqual(msg.subject, 'Internship Opportunity')
