# import httpx
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
#
# print(response.status_code)  # 200
# print(response.json())       # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
#
# import httpx
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
#
# print(response.status_code)  # 201 (Created)
# print(response.json())       # Ответ с созданной записью
#
# import httpx
#
# headers = {"Authorization": "Bearer my_secret_token"}
#
# response = httpx.get("https://httpbin.org/get", headers=headers)
#
# print(response.json())  # Заголовки включены в ответ

# import httpx
#
# params = {"userId": 1}
#
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
# print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
# print(response.json()) # Фильтрованный список задач

# import httpx
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
#
# response = httpx.post("https://httpbin.org/post", files=files)
#
# print(response.json())  # Ответ с данными о загруженном файле

# import httpx
#
# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
# print(response1.json())  # Данные первой задачи
# print(response2.json())  # Данные второй задачи

# import httpx
#
# try:
#     response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
#     response.raise_for_status()  # Вызовет исключение при 4xx/5xx
# except httpx.HTTPStatusError as e:
#     print(f"Ошибка запроса: {e}")

# import httpx
#
# try:
#     response = httpx.get("https://httpbin.org/delay/5", timeout=2)
# except httpx.ReadTimeout:
#     print("Запрос превысил лимит времени")


