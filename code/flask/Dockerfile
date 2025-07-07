FROM registry.access.redhat.com/ubi8/python-39

WORKDIR /opt/app-root/src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY templates/ templates/

EXPOSE 8080

CMD ["python", "app.py"]
