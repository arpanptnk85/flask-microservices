FROM python:3.10.16-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY resources resources
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=5 \ 
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT [ "python", "./resources/app.py"]