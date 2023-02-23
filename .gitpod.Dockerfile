FROM gitpod/workspace-full

# add your tools here
USER gitpod

RUN sudo apt-get update \
 && sudo apt-get install -y \
    chromium-chromedriver\
 && sudo apt-get install -y \
    firefox-geckodriver\
 && sudo rm -rf /var/lib/apt/lists/*
