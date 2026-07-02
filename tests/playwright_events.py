from playwright.sync_api import sync_playwright, Request, Response


# Логирование запросов
def log_request(request: Request):
    print(f"Request: {request.url}")


# Логирование ответов
def log_response(response: Response):
    print(f"Response: {response.url}")


with sync_playwright() as playwright:
    # Открываем браузер и создаём новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Добавляем обработчики событий
    page.on("request", log_request)  # Запрос отправлен
    page.on("response", log_response)  # Ответ получен

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    # Задержка для завершения всех запросов
    page.wait_for_timeout(3000)


# Отслеживание запросов
# with page.expect_request("**/*logo*.png") as first:
#     page.goto("https://wikipedia.org")
# print(first.value.url)

# Отслеживание всплывающих окон
# with page.expect_popup() as popup:
#     page.get_by_text("open the popup").click()
# popup.value.goto("https://wikipedia.org")

# Добавление обработчиков событий
# page.on("request", callback_function)  # Обработчик события отправки запроса
# page.on("response", callback_function)  # Обработчик события получения ответа

# Обработчики событий
# listener = lambda request: print(f"Request: {request.url}")
#
# page.on("request", listener)  # Добавляем обработчик
# page.remove_listener("request", listener)  # Убираем обработчик

# Фильтрация событий
# def log_specific_requests(request):
#     if "googleapis.com" in request.url:
#         print(f"Filtered request: {request.url}")
#
# page.on("request", log_specific_requests)

# Работа с ответами
# def log_response_body(response):
#     if response.ok:
#         print(f"Response body: {response.body()}")  # Тело ответа
#
# page.on("response", log_response_body)
