import json
from pathlib import Path

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def chat_api(request):
    user_message = request.data.get("message", "").lower().strip()

    file_path = Path(__file__).resolve().parent / "data" / "responses.json"

    with open(file_path, "r") as file:
        responses = json.load(file)

    for item in responses:
        question = item["question"].lower().strip()

        if user_message == question:
            return Response({
                "reply": item["answer"]
            })

    return Response({
        "reply": "Sorry, I don't know the answer yet."
    })