import json

from flask import Flask, render_template, request

import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# @app.route('/hello')
# def hello_world2():
#     data = "Hello, Data"
#     return render_template("hello.html", data = data)

@app.route('/user/<username>', methods=["GET", "POST"])
def get_user(username):
    return "hello %s" % username


# @app.route("/data", methods=["POST", "GET"])
# def test_data():
#     # print(request.args)
#     # print(request.args.get("a"), request.args.get("b "))
#     # print(request.data)
#     # import json
#     # print(json.loads(request.data))
#     print(request.form)
#     print(request.form.get("username"), request.form.get("password"))
#     return'success'

@app.route("/use_template")
def use_template():
    datas = [(1, "name1"), (2, "name2"), (3, "name3")]
    title = "学生信息"
    return render_template("use_template.html", datas=datas, title=title)


def read_car_inventory():
    # read file
    data = []
    with open("./data/car_inventory.txt") as fin:
        for line in fin:
            line = line[:-1]
            Make, Model, Color, Mileage, Price, Cost = line.split(" ")
            data.append((Make, Model, Color, Mileage, Price, Cost))
    return data


@app.route("/car_inventory")
def car_inventory():
    # read file
    data = read_car_inventory()

    # return html
    return render_template("car_inventory.html", data=data)


@app.route("/get_json")
def get_json():
    # read file
    data = read_car_inventory()

    # return html
    return json.dumps(data)

# 提交网页表单数据到mysql
@app.route("/show_add_user")
def show_add_user():
    # 用render来为了实现未来的网页动态数据展示
    return render_template("show_add_user.html")

# 提交数据的处理
@app.route("/do_add_user", methods=['POST'])
def do_add_user():
    print(request.form)
    name = request.form.get('name')
    sex = request.form.get('sex')
    age = request.form.get('age')
    email = request.form.get('email')
    sql = f"""
        insert into user(name,sex,age,email)
        values ('{name}','{sex}',{age},'{email}')
    """
    print(sql)
    db.insert_or_update_data(sql)
    return 'success'


if __name__ == '__main__':
    app.run()
