FROM python:3.7

LABEL MAINTANER="marcio.lima@santander.com.br"
LABEL NAME="MARCIO DE LIMA"

ENV APP_HOME="/opt/code"
USER root

WORKDIR $APP_HOME

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade -r $APP_HOME/requirements.txt
RUN pip install --no-cache-dir --upgrade scikit-learn==0.21.3

COPY ./app $APP_HOME/app
COPY ./modelo $APP_HOME/modelo
COPY ./start.sh $APP_HOME

ENV LC_ALL=en_US.utf8 \
    LANG=en_US.utf8 \
    APP_HOME=${APP_HOME}

RUN chmod 777 $APP_HOME

EXPOSE 8000:8000

ENTRYPOINT ["/bin/sh", "start.sh"]
