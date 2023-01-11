FROM python:3.11


#LABEL Maintainer="roushan.me17"


# Any working directory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /home

#to COPY the remote file at working directory in container
#COPY ./ ./
# Now the structure looks like this '/usr/app/src/test.py'

RUN git clone https://github.com/archius11/money_calc_tg_bot.git &&  \
    pip install --no-cache-dir -r money_calc_tg_bot/requirements.txt

#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python", "money_calc_tg_bot/main.py"]
