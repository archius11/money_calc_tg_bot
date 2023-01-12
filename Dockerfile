FROM python:3.11

WORKDIR /home/moneybot

#to COPY the remote file at working directory in container
COPY requirements.txt ./
# Now the structure looks like this '/usr/app/src/test.py'

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py"]
