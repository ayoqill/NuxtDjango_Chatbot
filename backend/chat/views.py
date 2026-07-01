from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def chat_api(request):
    message = request.data.get("message", "")

    return Response({
        "reply": f"You said: {message}"
    })