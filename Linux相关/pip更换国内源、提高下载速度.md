## 临时使用
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```
## 永久使用
1. 更新pip
```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```
2. 换源
```bash
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```