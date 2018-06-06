# -*- coding: utf-8 -*-
import os

basedir=os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
SECRET_KEY = '1werw3@#$@#%$^%&^%&^*&(*(()3he6'

UPLOAD_FOLDER = basedir+'/uploadFile'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024