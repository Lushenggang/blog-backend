import os
import sys
import uuid
import time

from qiniu import Auth
from . import api
from flask import g, jsonify, request, send_from_directory, current_app
from .decorators import permission_required
from ..models import Permission
from ..qiniu import get_token

@api.route('/get-file/')
def get_file():
  dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
  dirpath = dirname + '/../files/'
  filename = request.args.get('filename')
  path = request.args.get('path')
  if filename != 'default' and path:
    dirpath += path + '/'
  return send_from_directory(dirpath, filename)

@api.route('/get-qiniu-token/<filename>')
@permission_required(Permission.ADMIN)
def get_qiniu_token(filename):
  token = get_token(filename)
  domain = current_app.config['QI_NIU_LINK_URL']
  return jsonify({ 'token': token, 'domain': domain })

@api.route('/save-image/', methods = ['PUT'])
@permission_required(Permission.ADMIN)
def save_post_image():
  f = request.files['image']
  filename = str(uuid.uuid1()).replace('-', '')
  dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
  upload_path = dirname + '/../files/post/'
  if not os.path.exists(upload_path):
    os.makedirs(upload_path)
  f.save(upload_path + filename)
  return jsonify({ 'message': '上传成功', 'filename': filename, 'path': 'post' })