# start by pulling the python image
FROM python:3.10.5

# environment variables
ENV PORT=5010

# copy requirements file into the image
COPY ./requirements.txt /app/requirements.txt

# switch working directory
WORKDIR /app

# install the dependencies and packages in the requirements file
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

# copy every content from the local to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT ["python"]

# exposed internal port
EXPOSE 5010

CMD ["app.py"]