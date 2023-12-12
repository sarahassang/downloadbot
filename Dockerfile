FROM python:latest


RUN git clone https://github.com/Rip69x/downloadbot.git /downloadbot
WORKDIR /downloadbot
RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r downloadbot/requirements.txt
CMD python3 bot.py
