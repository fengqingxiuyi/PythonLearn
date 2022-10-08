# PythonLearn

## FAQ

### PEP 8: W292 no newline at end of file

PyCharm要求你在末尾新起一行，否则就会警告。更多信息：<https://pep8.readthedocs.io/en/latest/intro.html>

### UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc3 in position 0: invalid continuation byte

```python
# 因为25_file.txt文件的编码格式是gbk，而当前文件的编码格式是utf-8，所以会报错。
# file = open('25_file.txt', 'r')
# 解决方案：指定编码格式
file = open('25_file.txt', 'r', encoding='gbk')
```

## 参考教程

1. [Python全栈开发教程](https://www.bilibili.com/video/BV1wD4y1o7AS)
2. [Python3.9官方文档](https://docs.python.org/3.9/index.html)
