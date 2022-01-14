# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

    item = 999
    a = item % 10000 // 1000
    b = item % 1000 // 100
    c = item % 100 // 10
    d = item % 10
    print(f"{a},{b},{c},{d}")
# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
