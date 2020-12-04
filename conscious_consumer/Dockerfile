# Pull the Base Layer for Python
FROM python:3
# set environment variables
ENV PYTHONUNBUFFERED=1
WORKDIR /code
# install requirements
COPY ./requirements.txt /code/
RUN pip install -r ./requirements.txt
# copy the Django project
COPY . /code/
# change file permissions on the entrypoint
RUN chmod +x ./entrypoint
# run the commands on entrypoint.sh
CMD ["./entrypoint"]
