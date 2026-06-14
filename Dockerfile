FROM python:3.13-slim

WORKDIR /app

# 安装 Flask
RUN pip install --no-cache-dir flask

# 复制静态文件
COPY xkne_pv_quotation_builder.html /app/
COPY Server.py /app/

EXPOSE 8080

CMD ["python", "Server.py"]