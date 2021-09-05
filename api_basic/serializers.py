from rest_framework import serializers
from .models import Grade

class GradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grade
        fields = ['id', 'term', 'subject', 'catalogNbr', 'courseDescription',
                  'instructorLast', 'instructorFirst', 'aCount', 'bCount',
                  'cCount', 'dCount', 'fCount', 'satisfactory', 'dropCount',
                  'percentA']

