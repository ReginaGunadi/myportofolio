from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Award

class ExperienceTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="TED Translator",
            description="Menambahkan dan mereview subtitle Bahasa Indonesia dari video TED",
            category="part-time",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "TED Translator")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Ongoing")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "There are no experiences yet.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Finished")
        self.assertNotContains(response, "Ongoing")


class AwardsTest(TestCase):
    def setUp(self):
        self.award = Award.objects.create(
            title="ABRSM Grade 6",
            description="Main piano intinya mah",
            category="music",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.award.title)
        self.assertContains(response, f'href="{reverse("main:show_award")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_award_model(self):
        self.assertEqual(str(self.award), "ABRSM Grade 6")
        self.assertEqual(self.award.category, "music")

    def test_award_page(self):
        response = self.client.get(reverse("main:show_award"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "award.html")
        self.assertContains(response, self.award.title)
        self.assertContains(response, self.award.description)
        self.assertContains(response, "Music")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_award_page(self):
        Award.objects.all().delete()
        response = self.client.get(reverse("main:show_award"))
        self.assertContains(response, "There are no awards found yet.")