from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQResponse


@api_view(["POST"])
def chat_api(request):
    user_message = request.data.get("message", "").lower().strip()

    faq = FAQResponse.objects.filter(
        question__iexact=user_message
    ).first()

    if faq:
        return Response({
            "reply": faq.answer
        })

    return Response({
        "reply": "Sorry, I don't know the answer yet."
    })