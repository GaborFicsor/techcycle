from django.db import models


class FAQ(models.Model):
    """
    A model for the frequently asked questions
    This was made for better rendering the faq
    seciton on the landing page
    """
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
