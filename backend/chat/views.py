from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import FAQResponse
from .serializers import FAQResponseSerializer


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

@api_view(["GET"])
def faq_list_api(request):
    faqs = FAQResponse.objects.all()    # Gets all FAQ records from PostgreSQL
    serializer = FAQResponseSerializer(faqs, many=True)     # Converts many database rows into JSON
    return Response(serializer.data)
