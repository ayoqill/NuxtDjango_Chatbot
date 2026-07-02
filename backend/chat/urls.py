from django.urls import path
from .views import chat_api, faq_list_api

urlpatterns = [
    path("chat/", chat_api),
    path("faqs/", faq_list_api),
]

# means now we have 2 endpoints:
# 1. /api/chat/ - for handling chat messages reply
# 2. /api/faqs/ - for retrieving the list of FAQs