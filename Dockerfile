FROM python:3.11
ADD src/app /app
WORKDIR /app
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
COPY templates ./templates/
COPY static ./static/
ENV FLASK_APP=/app
ENV TZ="America/Denver"
CMD ["flask","run","--host=0.0.0.0","--port=5000"]