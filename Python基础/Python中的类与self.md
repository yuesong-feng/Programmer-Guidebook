在使用Python3刷LeetCode时，我们可以看到，每一个解都是包含在一个Solution类中的，并且函数的第一个参数都是self。那么Python中self究竟是什么呢？
>推荐大家自己动手写写代码，将会极大地帮助理解

Python中规定，一个类的函数的第一个参数是实例对象本身,相当于Java或C++里面的this指针。为了方便，我们一般命名为`self`表示“自己”的意思。（事实上命名成什么并没有影响）

也就是说，所有Python中的函数，只要函数在一个类里面，第一个参数都应该为self。如果不是self。如果不是self，那么表示的也是实例对象本身。

这样可以实现面向对象的思想，可以很方便地调用类自己的属性和方法。下面开始举例：

```python
class Solution:
    def __init__(self):
        self.val = 100
a = Solution()
print(a.val)
```
在这个例子中，`__init__`是类的初始方法，可以理解为在初始化一个Solution类的实例a时，同时创建了一个`self`指针，`self`就指向这个实例a。`self.val`表示：Solution类有一个属性，属性名为`val`。用`__init__`函数初始化实例时，将类的`val`属性设置为100。所以对于实例a，有一个属性`val`的值是100，程序应该输出100。

接下来为这个类添加一个`method`方法：

```python
class Solution:
    def __init__(self):
        self.val = 100
    def method(self, nums):
        print(nums)
a = Solution()
a.method()
```
这段程序执行会报错，原因是在调用Solution的method方法时，除了第一个参数self之外，还有一个参数nums，这是必须的，如果不传参数就会报错。应该改为：
```python
class Solution:
    def __init__(self):
        self.val = 100
    def method(self, nums):
        print(nums)
array = [1, 2, 3]
a = Solution()
a.method(array)
```
也可以把定义`method`的一行改为：
```python
def method(self, nums = [1, 2, 3]):
```
这样就可以不传参数，不传参数的时候nums设置为默认值[1, 2, 3]，传递参数的时候nums覆盖这个默认值。

注意，类中定义的方法`method`有两个参数`self`和`nums`，在函数被使用的时候，第一个参数是被忽略了的，从第二个参数开始传递。也就是说，函数中传递的`array`是对应的类方法的定义中的`nums`，而`self`是规定好的、指向类的实例a的指针。

如果类中有两个方法，self指针可以很方便地调用同类中的方法。例如：
```python
class Solution:
    def __init__(self):
        self.val = 100
    def method1(self, nums):
        self.method2(nums)
    def method2(self, nums):
        print(nums)
array = [1, 2, 3]
a = Solution()
a.method1(array)
```
`method2`方法是输出传递进的参数`nums`，那么`method1`方法呢？

`method1`方法负责接收参数`nums`，并把`nums`传递给`method2`。由于`method1`、`method2`都在类`Solution`中，要在`method1`中调用`method2`，则需要用`self.method2`说明，`method2`也是类中的方法而不是全局方法。