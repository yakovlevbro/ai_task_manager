from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# from .models import ChatMessage
from .services.ai_handler import get_ai_response


class AddProjectView(View):
    def get(self, request):
        return render(request, 'add_project.html')


        # Компиляция ответов в единый текст для отправки в OpenAI
        user_message = (f"Плачу 20 долларов чаевых"
                        f"Напиши полный и подробный RoadMap проекта основываясь на ответах на следующие вопросы:\n"
                        f"Вопрос 1: Какие именно функции должны быть реализованы на проекте? Какие возможности будут предоставлены пользователям? {question1}\n"
                        f"Вопрос 2: Как будем отслеживать количество зарегистрированных пользователей? Каков будет план маркетинговых мероприятий для достижения этой цели?  {question2}\n"
                        f"Вопрос 3: Какие ресурсы нам потребуются для разработки и запуска базовой версии платформы? Реально ли это сделать за указанный срок? {question3}\n"
                        f"Вопрос 4: Какие конкретные категории навыков и знаний будут доступны на платформе? Как это соответствует потребностям целевой аудитории?  {question4}\n"
                        f"Вопрос 5: Какие этапы разработки платформы должны быть завершены к определенным датам? Какой график работы у нашей команды разработчиков?  {question5}\n"
                        f"Вопрос 6*: Опишите команду, которая будет вести работу над этим проектом(роли, область работы, имена)?  {question6}"
                        )

        # Получение ответа от OpenAI
        chat_response = get_ai_response(user_message)

        # Возвращаем ответ в виде HTML
        return HttpResponse(chat_response)


    def post(self, request):
        # Обработка POST-запроса
        question1 = request.POST.get('question1')
        question2 = request.POST.get('question2')
        question3 = request.POST.get('question3')
        question4 = request.POST.get('question4')
        question5 = request.POST.get('question5')
        question6 = request.POST.get('question6')

        user_message = (f"Плачу 20 долларов чаевых"
                        f"Напиши полный и подробный RoadMap проекта основываясь на ответах на следующие вопросы:\n"
                        f"Вопрос 1: Какие именно функции должны быть реализованы на проекте? Какие возможности будут предоставлены пользователям? {question1}\n"
                        f"Вопрос 2: Как будем отслеживать количество зарегистрированных пользователей? Каков будет план маркетинговых мероприятий для достижения этой цели?  {question2}\n"
                        f"Вопрос 3: Какие ресурсы нам потребуются для разработки и запуска базовой версии платформы? Реально ли это сделать за указанный срок? {question3}\n"
                        f"Вопрос 4: Какие конкретные категории навыков и знаний будут доступны на платформе? Как это соответствует потребностям целевой аудитории?  {question4}\n"
                        f"Вопрос 5: Какие этапы разработки платформы должны быть завершены к определенным датам? Какой график работы у нашей команды разработчиков?  {question5}\n"
                        f"Вопрос 6*: Опишите команду, которая будет вести работу над этим проектом(роли, область работы, имена)?  {question6}"
                        )

        # Получение ответа от OpenAI
        chat_response = get_ai_response(user_message)

        # Возвращаем ответ в виде HTML
        return HttpResponse(chat_response)


# class ChatHistoryView(View):
#     def get(self, request, user_id):
#         # Получение истории диалога для конкретного пользователя
#         chat_history = ChatMessage.objects.filter(user_id=user_id).order_by('created_at')
#         return render(request, 'chat_history.html', {'chat_history': chat_history})
#
#     def post(self, request, user_id):
#         # Здесь вы можете добавить логику обработки данных из HTML-страницы
#         pass
