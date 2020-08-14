data = [{
    'name': "name1",
    'password': 'password1',
}, {

    'name': "name2",
    'password': 'password2',
}]


def start_output():
    """开始界面 
    """
    print("*"*30)
    print("欢迎使用")
    print()
    print("1 添加名片")
    print("2 显示全部名片")
    print("3 查询名片")
    print()
    print("0 退出")
    print("*"*30)
    pass


def add():
    name = input("请输入用户姓名：")
    password = input("请输入用户密码：")
    data.append({
        'name': name,
        'password': password
    })
    pass


def list():
    print("姓名\t\t密码\t\t")
    for a in data:
        print_user(a)
        pass
    pass


def search():
    a = input("请输入要搜索的姓名")
    for u in data:
        if u['name'] == a:
            print("姓名\t\t密码\t\t")
            print_user(u)
            caozuo2(u)
            break
        else:
            print("没有该用户")


def print_user(user):
    for a in user.values():
        print(a, end="\t\t")
    print()


def caozuo2(u):
    o = input("修改（1）删除（2） 退出（0）:")
    if o == '1':
        xiugai(u)
    elif o == '2':
        data.remove(u)
    else:
        pass


def xiugai(u):
    name = input("请输入要修改的姓名（回车不修改）：")
    password = input("请输入要修改的密码（回车不修改）：")
    if len(name) > 0:
        u[name] = name
    if len(password) > 0:
        u[password] = password
