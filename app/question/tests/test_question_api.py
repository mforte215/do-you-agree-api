from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Question
from question.serializers import QuestionSerializer
import datetime
from django.contrib.auth import get_user_model


QUESTION_LIST_URL = reverse('question:question-list')


def question_detail_url(question_id):
    """Get question detail URL"""
    return reverse('question:question-detail', args=[question_id])


def staged_question(user):
    """Create a sample question"""
    return Question.objects.create(
        created_by=user,
        created_on=datetime.datetime.now(),
        title='are you hungry?',
        text='title is the question'
        )


class PublicQuestionApiTests(TestCase):
    """Test unauthenticated question API access"""

    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
            'email@test.com',
            'testpassword'
        )
        self.client.force_authenticate(self.user)

    def test_get_question_list(self):
        """Test to get question list, no auth"""

        response = self.client.get(QUESTION_LIST_URL)
        questions = Question.objects.all().order_by('-id')
        serializer = QuestionSerializer(questions, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_single_question(self):
        """Test to view single question"""
        question = staged_question(user=self.user)
        url = question_detail_url(question.id)
        response = self.client.get(url)
        serializer = QuestionSerializer(question)
        self.assertEqual(response.data, serializer.data)
