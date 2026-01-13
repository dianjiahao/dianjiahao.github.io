# 1. 初始化 Git 仓库（让 Git 开始管理这个文件夹）
git init

# 2. 确保分支名叫 main
git branch -m main

# 3. 关联你的 GitHub 远程仓库
git remote add origin https://github.com/dianjiahao/dianjiahao.github.io.git

# 4. 添加所有文件（这一步是你之前失败的）
git add .

# 5. 提交更改
git commit -m "Update website and photos"

# 6. 强制推送到 GitHub（这一步会把电脑上的版本强制覆盖到网上）
git push -f origin main