## list(可变)

`list.insert(index, obj)` 在index处插入对象

`list.index(obj, start, end)` 找出与obj第一个匹配项的索引位置，start和end可选。

`list.remove(obj)` 移除列表中某个对象的第一个匹配项

`list.append(ob j)` 列表末尾添加新的对象

`list.pop(index=-1) -> obj` 移除一个元素并返回，index默认为-1（最后一个元素）

`list.count(obj) -> int` 统计对象在list中出现的次数

`list.reverse()` 列表反转

list用作栈：`list.append()	list.pop()`

list用作队列：`list.append()	list.pop(0)`

`set(list)` 列表直接转化为集合，去掉相同元素

`list.sort(key=None, reverse=False)` 列表排序。
- reverse = True 降序， reverse = False 升序（默认）。
- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。

- - `random = [(2, 2), (3, 4), (4, 1), (1, 3)]`

- - `random.sort(key=takeSecond)`



***
## str(不可变)

`str(list)` 返回list的真实字符串，如: str(['1', '2', '3', '4', '5']) -> '['1', '2', '3', '4', '5']' 想返回'12345'，应该用`''.join(list)`，此时list中的元素应为str，如果为int，要先转化为str才行

`str.count(sub, start=0, end=len(str)) -> int` 统计字串sub在str中出现的次数，start默认为0，end默认为len(str)

`str.lower() -> str` 全部字母变小写

`str.upper() -> str` 全部字母变大写

***
## collections库：

`collections.Counter(list) -> dict` 计数字典

***
## random库：
`random.random()` 生成 [0, 1) 之间的浮点数

`random.randomint(start, end)` 生成 [start, end] 之间的整数（包括start和end） 