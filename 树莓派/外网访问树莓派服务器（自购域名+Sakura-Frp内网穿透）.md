 - 首先在域名代理商（如腾讯云）购买一个喜欢的域名。
 - 注册Sakura Frp账号，进入管理面板后，创建隧道，服务器选择可建站类型的，隧道类型为HTTP，本地地址为树莓派IP地址，本地端口为80，绑定域名输入自己购买的域名。
>若选择国内的服务器，需要网站备案才可以建站，十分麻烦


>若不是网站，根据需要选择相应类型和端口。
 - 根据操作系统下载客户端，树莓派选择arm版。将客户端上传到树莓派，赋予可执行权限`chmod +x frpc_linux_arm`,然后在相同目录创建一个`frpc.ini`文件，打开隧道列表，查看刚刚建立的隧道的配置文件，把文本框中的配置代码复制到`frpc.ini`中。
- 接下来运行文件，`./frpc_linux_arm`，即可登录成功。会显示：
```
隧道启动成功
连接方式: sg-na-cn2.sakurafrp.comyuesong-feng.com
前面就是你创建隧道时选择的服务器，后面是你绑定的域名
```

 - 访问域名的控制台（如腾讯云），添加域名解析，把域名的CNAME记录更改为： `您创建隧道时选择的服务器，如：sg-na-cn2.sakurafrp.com`

- 稍等片刻，访问您的域名，即可外网访问树莓派服务器！
