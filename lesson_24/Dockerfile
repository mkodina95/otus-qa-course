FROM python:3.7
LABEL author=mkodina

# clone repository
RUN git clone https://github.com/mkodina95/otus-qa-course.git

# install packets
RUN pip3 install -r otus-qa-course/requirements.txt

# install chrome
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
RUN echo "deb [arch=amd64]  http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update
RUN apt-get -y install google-chrome-stable

# install webdriver
RUN /bin/bash -c "wget -qP /tmp/ https://chromedriver.storage.googleapis.com/$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip"
RUN unzip -o /tmp/chromedriver_linux64.zip -d /usr/bin
RUN chmod +x /usr/bin/chromedriver
RUN rm /tmp/chromedriver_linux64.zip