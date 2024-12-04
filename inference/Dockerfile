FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY chunker.proto /app/

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. inference.proto

COPY . /app/

EXPOSE 50050

CMD ["python", "server.py"]
