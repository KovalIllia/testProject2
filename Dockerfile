## Використовуємо офіційний Python образ
#FROM python:3.9-slim
#
## Встановлюємо робочу директорію
#WORKDIR /app
#
## Копіюємо файл залежностей
#COPY requirements.txt .
#
## Встановлюємо залежності
#RUN pip install --no-cache-dir -r requirements.txt
#
## Копіюємо код додатку
#COPY . .
#
## Відкриваємо порт
#EXPOSE 8000
#
## Команда для запуску
#CMD ["python", "app.py"]

FROM python:3.9-slim
WORKDIR /app
COPY ./app.py /app/
COPY ./requirements.txt .
ENV PYTHONPATH=/testproject2
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest allure-python-commons pytest-html pytest-xdist
RUN mkdir -p /app/test_result
#CMD ["python", "/app/app.py"]
#CMD python -m pytest -s --alluredir=test_result/ /testproject2/tests/
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
CMD ["python", "-m", "pytest", "-s", "--alluredir=/app/test_result/", "/testproject2/tests/"]

#correct comand for starting test -- docker run -v "$(pwd):/testproject2" -v "$(pwd)/test_result:/app/test_result" -v "$(pwd)/logs:/app/logs" testproject2:latestTest change
Test change
