from bottle import route, run, template,request,post, static_file,redirect,response,hook,HTTPResponse
import html_codes
from datetime import datetime
import time
import logging
import json

logging.basicConfig()
jobs = {}
job_defaults = {
    'coalesce': False,
    'max_instances': 2
}

heroes_json = ""

with open('heroes.json') as data_file:
    heroes_json = json.load(data_file)

@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/api/heroes')
def index():
    json_response = json.dumps(heroes_json)
    return json_response


run(host='localhost', port=8080)