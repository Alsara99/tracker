from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = [
            "id",
            "place",
            "time",
            "action",
            "periodicity",
            "duration",
            "is_public",
            "reward",
            "related_habit",
            "is_pleasant",
        ]
        read_only_fields = ["id", "user"]

    def validate(self, attrs):
        habit = Habit(**attrs)
        habit.clean()
        return attrs

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
