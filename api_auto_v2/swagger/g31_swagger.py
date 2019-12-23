#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/10/11
# @Author  : Edrain
import json

import requests
from flask import Flask
from flask_restplus import Api, Resource

from test_cases.supply_g31.g31_work_flow.test_supply_chain_funding import TestSupplyChainFunding
from test_cases.supply_g31.g31_work_flow.test_supply_chain_work_flow_31g_user import TestSupplyChainWorkFlow31gUser

app = Flask(__name__)
api_app = Api(app=app, version='1.0', title='SupplyChain', description='Main APIs')
ns = api_app.namespace(name='supplychain', description='这是swagger，发送接口请求')


@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        """这是一个get请求"""
        return {'status': 'you get a request.'}

    def post(self):
        return {'status': 'you post a request.'}


@ns.route('/get')
class HelloGet(Resource):
    def get(self):
        """访问httpbin的get请求"""
        url = "http://www.httpbin.org/get"
        response = requests.get(url)
        data = json.loads(response.text)
        return data


@ns.route('/registered')
class Registered(Resource):
    def get(self):
        """新用户注册"""
        TestSupplyChainWorkFlow31gUser().test_work_flow_02()
        return {'status': '注册成功'}


@ns.route("/funding/<string:loan_number>")
@ns.param('loan_number', '请传入需要放款的loan_number')
class Funding(Resource):
    def get(self, loan_number):
        """开始-银联放款"""
        TestSupplyChainFunding().test_funding_chinapay_batchPay(loan_number)
        return {'status': '放款成功'}


@ns.route('/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todo_id}


if __name__ == "__main__":
    app.run(debug=True)
