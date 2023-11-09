FROM python:3.10
LABEL authors="egor"
RUN pip install --upgrade pip && pip install fastapi && pip install uvicorn[standart]

# docker run --rm -p 5000:5000 -v "$(pwd)"/src:/src mp_kasud_im
WORKDIR /src
#RUN mkdir -p /var/www/var/media
#VOLUME /var/www/var/media
COPY ./src /src
#COPY start.sh /src

RUN chmod +x ./start.sh
CMD ["./start.sh"]
#CMD ["python", "http_api.py"]