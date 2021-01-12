项目原网站：https://make.quwj.com/project/10

Pi Dashboard (Pi 仪表盘) 是一个开源的 IoT 设备监控工具，目前主要针对树莓派平台，也尽可能兼容其他类树莓派硬件产品。你只需要在树莓派上安装好 PHP 服务器环境，即可方便的部署一个 Pi 仪表盘，通过炫酷的 WebUI 来监控树莓派的状态！

目前已加入的监测项目有：

- CPU 基本信息、状态和使用率等实时数据
- 内存、缓存、SWAP分区使用的实时数据
- SD卡（磁盘）的占用情况
- 实时负载数据
- 实施进程数据
- 网络接口的实时数据
- 树莓派IP、运行时间、操作系统、HOST 等基础信息
## 一、安装Nginx和PHP ##

 在 Pi 的终端运行以下命令。
```
    sudo apt-get update
    sudo apt-get install nginx php7.3-fpm php7.3-cli php7.3-curl php7.3-gd php7.3-cgi
    sudo service nginx start
    sudo service php7.3-fpm restart
```
如果安装成功，可通过 http://树莓派IP/ 访问到 Nginx 的默认页。Nginx 的根目录在 /var/www/html。

接下来要让Nginx能处理PHP

`sudo nano /etc/nginx/sites-available/default`
将其中的如下内容

```
location / {
                # First attempt to serve request as file, then
                # as directory, then fall back to displaying a 404.
                try_files $uri $uri/ =404;
        }
```
替换为
```
location / {
    index  index.html index.htm index.php default.html default.htm default.php;
}
 
location ~\.php$ {
    fastcgi_pass unix:/run/php/php7.3-fpm.sock;
    #fastcgi_pass 127.0.0.1:9000;
    fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    include fastcgi_params;
}
```
Ctrl + O 保回车存再 Ctrl + X 退出。
最后重启Nginx
`sudo service nginx restart`
## 二、上传Pi-Dashboard到树莓派服务器

>首先在树莓派安装git并配置好github的用户名、邮箱，树莓派默认自带git
    ```
    cd /var/www/html
    ```
    ```
    sudo git clone https://github.com/spoonysonny/pi-dashboard.git
    ```
即可通过`http://树莓派IP/pi-dashboard`访问部署好了的 Pi Dashboard。

如果页面无法显示，可以尝试在树莓派终端给源码添加运行权限，例如你上传之后的路径是是`/var/www/html/pi-dashboard`，则运行
    cd /var/www/html
    sudo chown -R www-data pi-dashboard
>也可[直接在github下载项目源代码][1]，然后上传到树莓派的`/var/www/html`目录


  [1]: https://github.com/spoonysonny/pi-dashboard