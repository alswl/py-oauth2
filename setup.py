#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name = 'py-oauth2',
    version = '0.0.1',
    keywords = ('Python', 'OAuth2', 'Douban', 'GitHub', 'Weibo'),
    description = 'Python OAuth2',
    long_description = 'Python OAuth2',
    license = 'MIT License',

    url = 'https://github.com/liluo/py-oauth2',
    author = 'liluo',
    author_email = 'i@liluo.org',

    packages = find_packages(),
    platforms = 'any',
    install_requires = ['httplib2'],

)
