{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "server.py",
      "provenance": [],
      "authorship_tag": "ABX9TyNqk1O4HEE9JPEjRqboUDcT",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/DrVenkataRajeshKumar/EVA4-Capstone-Project/blob/main/server_py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "ZnVz4PhiSGlz"
      },
      "source": [
        "# from werkzeug import secure_filename\r\n",
        "from flask import Flask, render_template, request\r\n",
        "import time\r\n",
        "app = Flask(__name__)\r\n",
        "\r\n",
        "@app.route('/')\r\n",
        "def index():\r\n",
        "   return render_template('index.html')\r\n",
        "\r\n",
        "\r\n",
        "@app.route('/Imgclassification/')\r\n",
        "def imgclassification():\r\n",
        "    return render_template('Imgclassification.html')\r\n",
        "\r\n",
        "@app.route('/upload/')\r\n",
        "def uploadFiles():\r\n",
        "   return render_template('upload.html')\r\n",
        "# @app.route('/upload')\r\n",
        "# def upload_file():\r\n",
        "#    return render_template('upload.html')\r\n",
        "\t\r\n",
        "@app.route('/uploader/', methods = ['GET', 'POST'])\r\n",
        "def upload_file():\r\n",
        "   print('fff')\r\n",
        "   if request.method == 'POST':\r\n",
        "      f = request.files['file']\r\n",
        "      f.save(secure_filename(f.filename))\r\n",
        "      return 'File uploaded successfully'\r\n",
        "\r\n",
        "@app.route('/my-link/', methods = ['GET', 'POST'])\r\n",
        "def hello_python():\r\n",
        "   print(\"hello\")\r\n",
        "   if(request.method == 'POST'):\r\n",
        "      print(\"hello post completed\")\r\n",
        "      uploaded_files = request.files.getlist(\"fileupload1\")\r\n",
        "      save(secure_filename(f.filename))\r\n",
        "      print(uploaded_files)\r\n",
        "\r\n",
        "   return \"Completed\"\r\n",
        "\r\n",
        "if __name__ == '__main__':\r\n",
        "   app.run(debug = True)\r\n"
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
