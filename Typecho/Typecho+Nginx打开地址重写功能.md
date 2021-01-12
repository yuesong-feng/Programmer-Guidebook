在Typecho服务器启用地址重写时，启用失败。
原因是Nginx服务器默认没有开启地址重写功能
解决方法：
在Nginx的配置文件的server中，加入：

```
if (!-e $request_filename) {
    rewrite ^(.*)$ /index.php$1 last;
}
```

保存即可。

> 如果使用宝塔面板，则直接在网站设置--伪静态中复制上面的代码保存。
