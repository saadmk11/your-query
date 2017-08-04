from questions.models import SendNotification


def notification_count(request):
    if request.user.is_authenticated:
        user = request.user
        not_viewed = SendNotification.objects.filter(user=user, viewed=False).count()
        return {'not_viewed': not_viewed}
    return {}
