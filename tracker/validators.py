from rest_framework.serializers import ValidationError


def validate_habit(data):
    if data.get("reward") and data.get("related_habit"):
        raise ValidationError("Нельзя одновременно reward и related_habit")

    if data.get("duration", 0) > 120:
        raise ValidationError("Время выполнения > 120 секунд")

    if data.get("is_pleasant"):
        if data.get("reward") or data.get("related_habit"):
            raise ValidationError("У приятной привычки не может быть награды")
