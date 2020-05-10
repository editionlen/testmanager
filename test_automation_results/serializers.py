from test_automation_results.models import JobReport
from rest_framework import serializers

class JobReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobReport
        fields = '__all__'