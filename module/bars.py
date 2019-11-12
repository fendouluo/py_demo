"""
Bars Module
============
这是一个打印不同分割线的示例模块
导入模块
有不同的方式导入模块。我们已经看到过一种了。你甚至可以从模块中导入指定的函数。这样做：
>>> from bars import simplebar, starbar
>>> simplebar(20)
--------------------
你也可以使用 from module import * 导入模块中的所有定义，然而这并不是推荐的做法.使用 import bars
"""

def starbar(num):
    """打印 * 分割线

    :arg num: 线长
    """
    print('*' * num)

def hashbar(num):
    """打印 # 分割线

    :arg num: 线长
    """
    print('#' * num)

def simplebar(num):
    """打印 - 分割线

    :arg num: 线长
    """
    print('-' * num)
