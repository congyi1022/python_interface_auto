#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/8/6
# @Author  : Edrain
import requests


class BaseApi(object):

    method = "GET"
    url = ""
    params = None
    data = None
    headers = None
    cookies = None
    files = None
    auth = None
    timeout = None
    allow_redirects = True
    proxies = None
    hooks = None
    stream = None
    verify = None
    cert = None
    json = None

    def __init__(self):
        self.response = None

    def set_params(self, **params):
        self.params = params
        return self

    def set_header(self, key, value):
        self.headers = self.headers or {}
        self.headers.update({key: value})
        return self

    def set_headers(self, **kwargs):
        self.headers = self.headers or {}
        self.headers.update(kwargs)
        return self

    def set_cookie(self, key, value):
        self.cookies = self.cookies or {}
        self.cookies.update({key: value})
        return self

    def set_cookies(self, **kwargs):
        self.cookies = self.cookies or {}
        self.cookies.update(kwargs)
        return self

    def set_json(self, json_data):
        self.json = json_data
        return self

    def set_data(self, data):
        self.data = data
        return self

    def set_file(self, files):
        self.files = files
        return self

    def run(self, session=None):
        session = session or requests.sessions.Session()
        self.response = session.request(
            self.method,
            self.url,
            params=self.params,
            data=self.data,
            headers=self.headers,
            cookies=self.cookies,
            files=self.files,
            auth=self.auth,
            timeout=self.timeout,
            allow_redirects=self.allow_redirects,
            proxies=self.proxies,
            hooks=self.hooks,
            stream=self.stream,
            verify=self.verify,
            cert=self.cert,
            json=self.json
        )
        return self

    def extract(self, field):
        value = self.response
        for _key in field.split("."):
            if isinstance(value, requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value, _key)
            elif isinstance(value, (requests.structures.CaseInsensitiveDict, dict)):
                value = value[_key]
        return value

    def validate(self, key, expected_value):
        actual_value = self.extract(key)
        assert actual_value == expected_value
        return self

    def get_response(self):
        return self.response



