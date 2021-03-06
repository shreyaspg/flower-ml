FROM python:3.8
RUN apt-get update && apt-get install -y \
     python3

ENV HOME /home/app
RUN pip install --upgrade pip

RUN pip install flwr==0.16.0
RUN pip install scikit-learn==0.24.2
RUN pip install openml==0.12.2
RUN pip install pandas


WORKDIR $HOME
COPY . $HOME

ENTRYPOINT ["python3"]
