from django.urls import path
from .views import chat_api, faq_list_api, register_api

urlpatterns = [
    path("chat/", chat_api),
    path("faqs/", faq_list_api),
    path("signup/", register_api),
]

# means now we have 3 endpoints:
# 1. /api/chat/ - for handling chat messages reply
# 2. /api/faqs/ - for retrieving the list of FAQs
# 3. /api/register/ - for registering new users