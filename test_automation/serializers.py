from test_automation.models import TestSuite, TestCase, TestJob
from rest_framework import serializers


class TestSuiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSuite
        fields = ('id', 'name')

class TestCaseSerializer(serializers.ModelSerializer):
    test_suite = TestSuiteSerializer(many=False)
    class Meta:
        model = TestCase
        fields = ('id', 'name', 'script', 'script_type', 'test_suite')

class TestJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestJob
        fields = '__all__'