# -*- coding: utf-8 -*-
"""
鑫科新能源光伏EPC报价单系统
部署到 Railway：python server.py
"""
from flask import Flask, send_from_directory
app = Flask(__name__)

BASE = "/app"  # Railway 容器内路径

@app.route("/")
def index():
    return send_from_directory(BASE, "xkne_pv_quotation_builder.html")

@app.route("/<path:path>")
def static_files(path):
    return send_from_directory(BASE, path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)