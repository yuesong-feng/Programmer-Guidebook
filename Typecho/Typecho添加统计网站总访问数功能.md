>适用于handsome主题

在服务器端打开文件：`sudo nano /var/www/html/usr/themes/handsome/component/sidebar.php`
把第一行
		`<?php if (!defined('__TYPECHO_ROOT_DIR__')) exit ?>`
替换为
```php
 <?php if (!defined('__TYPECHO_ROOT_DIR__')) exit;
    //总访问量
    function theAllViews()
        {
            $db = Typecho_Db::get();
            $row = $db->fetchAll('SELECT SUM(VIEWS) FROM `typecho_contents`');
                echo number_format($row[0]['SUM(VIEWS)']);
        }
 ?>
```
> 第六行中,`typecho_contents`中的`typecho_`是您的数据库前缀，如果您安装typecho时修改过，则换成您自己的前缀

在下文中找到博客信息，可以看到有一些`<li>`标签，在其中加入访客总数标签：
```html
<li class="list-group-item"> <i class="glyphicon glyphicon-user text-muted"></i> <span class="badge
pull-right"><?php echo theAllViews();?></span><?php _me("访客总数") ?></li>

```
然后保存文件即可。
>其他主题单独调用：`<?php echo theAllViews();?></span><?php _me("访客总数") ?>`