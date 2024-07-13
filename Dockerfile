FROM apache/airflow:2.7.1-python3.9

COPY requirements.txt /opt/airflow/ 
# copy the requirement files to airflow folder

USER root 
# switch to root user

# update libraries and install python
RUN apt-get update && apt-get install -y gcc python3-dev


# switch to airflow user
USER airflow


# install all the requirements
RUN pip install --no-cache-dir -r /opt/airflow/requirements.txt
