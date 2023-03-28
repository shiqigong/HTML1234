# git项目

## git init 初始化项目

## git status 初始化仓库后默认工作在master分支，当前工作区与仓库去不一致会有提示
## git add [files...] 将工作内容记录到暂存区
## git rm --cached[file] 取消文件暂存记录
## git commit [file] -m [message] 将文件同步到本地仓库  -m 表明添加一些同步信息，表达同步内容
## git log 查看commit 日志记录
## git log --pretty=oneline  查看日志记录第一行
## git diff [file] 比较工作区文件和仓库文件差异
## git checkout [commit] -- [file] 将暂存区或者某个commit点文件恢复到工作区
## git mv [file] [path]    git rm [files]  移动或者删除文件  注意：这两个操作会修改工作区内容，同时将操作记录提交到暂存
## git reset --hard HEAD^ 退回到上一个commit节点  一个^表示退回一个版本，以此类推
## git reset --hard [commit_id] 退回到指定的commit_id节点
## git reflog 查看所有操作记录，最上面的为最新记录，可以利用commit_id去往任何操作位置
## git tag [tag_name] [commit_id] -m [message] 创建标签，commit_id不写默认标签表示最新的commit_id位置，message也可以不写
## git tag 查看标签列表 
## git show [tag_name] 查看标签详细信息
## git reset --hard [tag] 去往某个标签节点
## git tag -d [tag]  删除标签
## git stash save [message] 保存工作区内容，将工作区未提交的修改封存，让工作区回到修改前的状态
## git stash list 查看工作区列表，最新保存的工作区在最上面
## git shash apply [stash@{n}] 应用某个工作区
## git stash drop [stash@{n}] 删除某一个工作区
## git stash clear 删除所有保存的工作区