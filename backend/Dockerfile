FROM python:3.8-slim-buster
WORKDIR /myapp
COPY . /myapp
ENV FLASK_APP=main.py
RUN pip3 install -r requirements.txt
VOLUME /myapp
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0","app:app"]
