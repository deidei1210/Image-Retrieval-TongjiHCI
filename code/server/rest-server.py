import os
import shutil

import numpy as np
from flask import Flask, Response, jsonify, request, redirect
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from tensorflow.python.platform import gfile
from werkzeug.utils import secure_filename

from search import recommend

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__, static_url_path="")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
auth = HTTPBasicAuth()

CORS(app, resources=r'/*')

# Loading the extracted feature vectors for image retrieval
extracted_features = np.zeros((2955, 2048), dtype=np.float32)
with open('saved_features_recom.txt') as f:
    for i, line in enumerate(f):
        extracted_features[i, :] = line.split()
print("loaded extracted_features")

# tags
tag_type = ['animals', 'baby', 'bird', 'car', 'clouds', 'dog', 'female',
            'flower', 'food', 'indoor', 'lake', 'male', 'night', 'people',
            'plant_life', 'portrait', 'river', 'sea', 'structures', 'sunset',
            'transport', 'tree', 'water']


def image_tags():
    type_dict = dict()
    for i in tag_type:
        type_dict[i] = []
        # 读取对应的文件
        with open('database/tags/' + i + '.txt', 'r') as fp:
            li = fp.readlines()
            for j in li:
                type_dict[i].append(j.strip())
    return type_dict


# 预加载
type_dict = image_tags()


# 通过id查找图片
@app.route('/image', methods=['GET'])
def get_img():
    imageId = request.values.get('id')

    with open('database/dataset/im' + imageId + '.jpg', mode='rb') as f:
        byte_data = f.read()

    return Response(byte_data, mimetype='image/jpeg')


# 获取收藏图片
@app.route('/collect/all', methods=['GET'])
def get_all_collect():
    res = []

    filename = 'database/favorites.txt'

    if not os.path.isfile(filename):
        with open(filename, 'w') as f:
            pass

    with open(filename, mode='r') as f:
        for i in f.readlines():
            res.append(i.strip())

    return jsonify(res)


# 改变收藏状态
@app.route('/collect', methods=['POST'])
def change_img_collect():
    # 获取json中的数据
    data: dict = request.get_json()
    data = {k: v for k, v in data.items() if v is not None and v != ''}

    print(data)
    imageId = data['id']
    imageId = str(imageId)

    filename = 'database/favorites.txt'

    if not os.path.isfile(filename):
        with open(filename, 'w'):
            pass

    # 获取全部收藏图片
    with open('database/favorites.txt', mode='r') as f:
        s = f.readlines()

    p = []
    isCollected = False
    for i in s:
        if i.strip() == imageId:
            isCollected = True
        else:
            p.append(i.strip())

    if not isCollected:
        p.append(imageId)

    # 写回
    n = len(p)
    with open('database/favorites.txt', mode='w') as f:
        for index, item in enumerate(p):
            if index != n - 1:
                f.write(item + '\n')
            else:
                f.write(item)

    return jsonify({
        'success': True,
    })


@app.route("/tags", methods=['GET'])
def get_tags():
    res = []
    for i in type_dict.keys():
        res.append({
            'label': i,
            'size': len(type_dict[i]),
        })
    res.sort(key=lambda x: x['size'], reverse=True)

    return jsonify(res)


@app.route('/info', methods=['GET'])
def get_img_info():
    imageId = request.values.get('id')

    filename = 'database/favorites.txt'

    if not os.path.isfile(filename):
        with open(filename, 'w'):
            pass

    # 查看favorites文件夹
    with open(filename, mode='r') as f:
        isCollected = False
        for i in f.readlines():
            if i.strip() == imageId:
                isCollected = True
                break

    # 获取图片类型
    tags = []
    for i in type_dict.keys():
        if imageId in type_dict[i]:
            tags.append(i)

    return jsonify({
        'isCollected': isCollected,
        'tags': tags,
    })


@app.route('/upload_img', methods=['GET', 'POST'])
def upload_img():
    print("image upload")
    result = 'static/result'
    if not gfile.Exists(result):
        os.mkdir(result)
    shutil.rmtree(result)

    if request.method == 'POST' or request.method == 'GET':
        print("files")
        print(request.files)
        print("form")
        print(request.form)

        # 检查request中是否存在文件数据
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        print(file.filename)
        # 没有选择图片的情况下提交空文件
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            input_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            recommend(input_location, extracted_features)
            os.remove(input_location)
            image_list = [file[2:-4] for file in os.listdir(result) if not file.startswith('.')]
            print(image_list)
            return jsonify(image_list)


app.run(debug=True, port=3367, host='0.0.0.0')
