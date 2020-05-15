from rest_framework import serializers
from core.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """Serialize a question for list"""

    class Meta:
        model = Question
        fields = (
            'id', 'title', 'active', 'created_by', 'created_on', 'upvotes', 'downvotes',
        )
        read_only_fields = ('id', 'created_by', 'created_on')
