FROM python:3

# Nodejs
RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt install -y nodejs && \
    npm install npm@latest -g

# Django
COPY ./django /usr/src/django
WORKDIR /usr/src/django
RUN pip install -r requirements.txt
