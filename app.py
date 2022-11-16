import os
from typing import Optional, Dict, Any

from flask import Flask, jsonify, request
from flask_restx import Api, Resource

from functions import file_data, filter_lines, map_lines, unique_lines, sort_lines, limit_lines, regex

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

api = Api(app)
perform_ns = api.namespace("")

commands = {
    'filter': filter_lines,
    'map': map_lines,
    'unique': unique_lines,
    'sort': sort_lines,
    'limit': limit_lines,
    'regex': regex
}


@perform_ns.route("/perform_query")
class PerformView(Resource):
    def post(self) -> object:
        req_json = request.json
        filename = req_json.get('file_name')
        cmd1 = req_json.get('cmd1')
        value1 = req_json.get('value1')
        cmd2 = req_json.get('cmd2')
        value2 = req_json.get('value2')

        try:
            data = file_data(filename)
        except FileNotFoundError:
            return "Файл не найден"

        try:
            command1 = commands[cmd1]
            command2 = commands[cmd2]
        except KeyError:
            return "Команда не найдена"

        data = command1(data, value1)
        data = command2(data, value2)

        data = list(data)

        return jsonify({'result': data})
