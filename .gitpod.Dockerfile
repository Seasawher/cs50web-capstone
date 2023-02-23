FROM gitpod/workspace-full

RUN pip install -r requirements.txt

USER gitpod
