首先确认你的Mac已经安装了命令行工具：Command Line Tools (CLT) for Xcode。打开终端，输入`git --version`，命令，如果没有安装，macOS会跳出安装框，点击安装即可。如果已经安装则会出现git版本信息，如：`git version 2.24.3 (Apple Git-128)`

接下来更换homebrew的源，首先确认您使用的是zsh还是bash终端，macOS自带的终端是zsh终端。

如果使用的是zsh，则查看用户的根目录下是否有`.zprofile`文件，如果没有则用以下命令新建一个：

`touch ~/.zprofile` 

然后在这个文件里写入如下内容：

```bash
export HOMEBREW_BREW_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git"
export HOMEBREW_CORE_GIT_REMOTE="https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git"
export HOMEBREW_BOTTLE_DOMAIN="https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles"
```

保存后用`source ~/.zprofile`命令使之生效，然后输入`export`，如果配置正确，应该会看到三个环境变量：`HOMEBREW_BREW_GIT_REMOTE`，`HOMEBREW_CORE_GIT_REMOTE`，`HOMEBREW_BOTTLE_DOMAIN`，地址为刚刚保存在`.zprofile`文件中的地址。

然后在终端输入下面的命令安装homebrew：
```bash
git clone --depth=1 https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/install.git brew-install
/bin/bash -c "$(
    cat brew-install/install.sh |
    sed -E 's|^(\s*HOMEBREW_BREW_GIT_REMOTE=)(.*)$|\1"${HOMEBREW_BREW_GIT_REMOTE:-\2}"|g' |
    sed -E 's|^(\s*HOMEBREW_CORE_GIT_REMOTE=)(.*)$|\1"${HOMEBREW_CORE_GIT_REMOTE:-\2}"|g'
)"
rm -rf brew-install
```

对基于 Apple Silicon CPU 设备上的 macOS 系统,安装成功后需将 brew 程序的相关路径加入到环境变量中(Intel芯片的设备可忽略)：
```bash
grep -qF '/opt/homebrew/bin' /etc/paths || sudo sed -i "" '1i \
/opt/homebrew/bin
' /etc/paths
grep -qF '/opt/homebrew/share/man' /etc/manpaths || sudo sed -i "" '1i \
/opt/homebrew/share/man
' /etc/manpaths
```

然后使用以下命令替换现有仓库上游：
```bash
git -C "$(brew --repo)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git
git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git
git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask.git
git -C "$(brew --repo homebrew/cask-fonts)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-fonts.git
git -C "$(brew --repo homebrew/cask-drivers)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-drivers.git
git -C "$(brew --repo homebrew/cask-versions)" remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-cask-versions.git
```

更换上游后需重新设置 git 仓库 HEAD：
```bash
brew update-reset
```

至此，homebrew安装完成，并且更换到了清华源。