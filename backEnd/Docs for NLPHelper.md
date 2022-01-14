### Docs for NLPHelper

**以下给出 NLPHelper 类型的方法声明和用法示例：**

#### 构造方法

```python
def __init__(self, filename='text.txt'):
```

构造方法，需要传入一个参数 filename, 即需要处理的文件路径名。默认值为当前文件夹下的 text.txt

example:

```python
helper_no_args = NLPHelper()
helper_with_args = NLPHelper('case.txt')
```

#### 处理方法

```python
def process(self):
```

无需传入参数，调用该方法之后会处理初始化 NLPHelper 时指定（或默认）的文本文件，完成相应信息的抽取，结果保存在 NLPHelper 对象的成员变量 info （一个字典）中。

example:

```python
helper = NLPHelper()
helper.process()
```

#### 结果的获取

调用处理方法 process 之后结果保存在 NLPHelper 对象的成员变量 info 中（一个字典），通过对应的 key 来获得对应的 value (一个 set)

example:

```python
... # 前面已经完成处理
name = helper.info['name']
ethnicity = helper.info['ethnicity']
gender = helper.info['gender']
birthplace = helper.info['birthplace']
courts = helper.info['courts']
causes = helper.info['causes']
```

#### 在控制台展示处理结果 （测试时使用）

```python
def print_out(self):
```

调用该方法在控制台打印出处理结果

example:

```python
... # 前面已经完成处理
helper.print_out()
```

