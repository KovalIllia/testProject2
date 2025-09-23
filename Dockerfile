

FROM python:3.9-slim

WORKDIR /app

COPY . /app/

ENV PYTHONPATH=/app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pytest allure-python-commons pytest-html pytest-xdist

RUN mkdir -p /app/test_result

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


CMD ["python", "-m", "pytest", "-s", "--alluredir=/app/test_result/"]

