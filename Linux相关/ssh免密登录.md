在登陆ssh时，每次都要输入密码，特别是vs code打开新窗口，十分麻烦。使用验证密匙即可实现ssh远程登陆
在自己的windows电脑（ssh客户端）中，打开cmd执行：
```bash
ssh-keygen
```
一直按回车，所有都为默认设置
然后在cmd中进入用户目录下的`.ssh`文件夹，里面有`id_rsa.pub`文件
把这个文件上传到需要登陆的Linux服务器：
```bash
scp id_rsa.pub  Linux用户名@Linux的IP地址:/home/xxx(上传到哪个文件目录)
```
查看Linux用户目录中是否有文件夹`.ssh`，若没有则创建：
```bash
mkdir .ssh
```
进入`.ssh`，将刚刚上传的`id_rsa.pub`文件追加到`authorized_keys`即可。
```bash
cat id_rsa.pub >> authorized_keys 
```
>若没有文件，将会自动创建