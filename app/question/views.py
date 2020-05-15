from rest_framework import viewsets
from question import serializers
from core.models import Question


class QuestionViewSet(viewsets.ModelViewSet):
    """View questions in the db"""
    serializer_class = serializers.QuestionSerializer
    queryset = Question.objects.all().order_by('-id')

    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(created_by=self.request.user)
