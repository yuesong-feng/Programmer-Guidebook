修改ssh配置文件：

```bash
sudo vim /etc/ssh/sshd_config
```
找到注释掉的`PermitRootLogin`,取消注释并把值设置为yes
然后重启ssh服务即可

```bash
service sshd restart
```
