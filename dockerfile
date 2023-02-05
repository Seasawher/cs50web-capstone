FROM python:3

# Nodejs
RUN curl -sL https://deb.nodesource.com/setup_lts.x | bash - && \
    apt install -y nodejs && \
    npm install npm@latest -g
WORKDIR /usr/src/frontend
COPY /frontend/package*.json ./
RUN npm install

# Django
WORKDIR /usr/src/django
COPY /django/requirements.txt ./
RUN pip install -r requirements.txt
