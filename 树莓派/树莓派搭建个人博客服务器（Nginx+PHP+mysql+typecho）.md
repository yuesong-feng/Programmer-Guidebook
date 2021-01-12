>建议在安装之前先安装Pi Dashboard（我的博客里有详细安装教程）,通过炫酷的 WebUI 来监控树莓派的状态！
>如果已经按照教程完成了Pi Dashboard的安装，即可跳过第一步（安装Nginx和PHP）

## 一、安装Nginx和PHP ##
 在 Pi 的终端运行以下命令。
```
    sudo apt-get update
    sudo apt-get install nginx php7.3-fpm php7.3-cli php7.3-curl php7.3-gd php7.3-cgi
    sudo service nginx start
    sudo service php7.3-fpm restart
```
如果安装成功，可通过 http://树莓派IP/ 访问到 Nginx 的默认页。Nginx 的根目录在 /var/www/html。

#### 接下来要让Nginx能处理PHP

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

## 二、安装mysql
`sudo apt-get install mariadb-server`

修改密码：`sudo mysqladmin -u root -p password`
初始密码随便输入，然后输入您的密码，即可设置root用户的密码。

进入数据库：`sudo mysql -u root -p`，然后输入您设置的密码。

使用Typecho需要创建一个名为`typecho`的数据库：
`CREATE DATABASE typecho;`

把数据可权限交给root用户：
`GRANT ALL PRIVILEGES ON typecho.* TO 'root'@'localhost' IDENTIFIED BY '您设置的密码';`
`FLUSH PRIVILEGES;`
然后按 Ctrl+D 退出 MariaDB 提示符。

## 三、安装Typecho
在[Typecho官网][1]下载Typecho，解压后上传到服务器的指定目录（树莓派默认为`/var/www/html`）
上传完毕，访问 http://树莓派IP/ 即可看到Typecho的安装程序，根据引导完成安装。
>官网安装文档：http://docs.typecho.org/install
>
进入Typecho后、无法登录后台，点击前台链接或者后台登录时出现"404, not found"

这是nginx的设置时没有注意支持pathinfo导致的，具体关于php pathinfo的信息可以在网上搜索到。

#### 解决方法
打开Nginx的配置文件`sudo nano /etc/nginx/sites-available/default`,一般的出现这种情况时,location设置都是类似这样
`   location ~ .*\.php$`
要支持pathinfo，要改成
`    location ~ .*\.php(\/.*)*$`
然后在location里加上
（注意是加上不是替换！）

```
            set $path_info "";
            set $real_script_name $fastcgi_script_name;
            if ($fastcgi_script_name ~ "^(.+?\.php)(/.+)$") {
                    set $real_script_name $1;
                    set $path_info $2;
            }
            fastcgi_param SCRIPT_FILENAME $document_root$real_script_name;
            fastcgi_param SCRIPT_NAME $real_script_name;
            fastcgi_param PATH_INFO $path_info;
```
>其他问题可参考官网文档 http://docs.typecho.org/servers



  [1]: http://typecho.org/