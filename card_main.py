import card_tools


while True:
    card_tools.start_output()
    op = input("请选择操作功能:")
    if op in ["1", "2", "3"]:
        if op == '1':
            card_tools.add()
        elif op == '2':
            card_tools.list()
        elif op == '3':
            card_tools.search()
    elif op == '0':
        break
    else:
        print("请输入正确的操作！！：")
    pass
