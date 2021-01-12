在index.php和archive.php文件找到代码
>`<?php $this->content('阅读剩余部分...'); ?>`

将其替换为
>`<?php $this->excerpt(); ?>`
如果要按制摘要的输出字数，可以修改代码为
>`<?php $this->excerpt(200, '...'); ?>`

如果使用handsome主题，直接在主题设置里设置即可