# 如何推送到 GitHub

## ✅ 已完成的准备工作

- ✅ Git 仓库已初始化
- ✅ 所有文件已添加并提交
- ✅ 远程仓库已配置: `https://github.com/AchengBusiness/happycapy-office-ui.git`
- ✅ 分支已重命名为 `main`

## 📋 推送步骤

### 方法 1: 使用 GitHub CLI（推荐）

如果你已经安装了 GitHub CLI:

```bash
# 1. 登录 GitHub
gh auth login

# 2. 推送代码
git push -u origin main
```

### 方法 2: 使用 Personal Access Token

1. **创建 GitHub 仓库**（如果还没有的话）
   - 访问 https://github.com/new
   - 仓库名：`happycapy-office-ui`
   - 可见性：**Public**（公开）
   - 不要勾选 "Initialize with README"

2. **创建 Personal Access Token**
   - 访问 https://github.com/settings/tokens/new
   - Note: `happycapy-office-ui-push`
   - Expiration: 选择有效期
   - Scopes: 勾选 `repo`（全部权限）
   - 点击 "Generate token"
   - **复制生成的 token（只显示一次！）**

3. **推送到 GitHub**

```bash
# 使用 token 推送（将 YOUR_TOKEN 替换为你的 token）
git push https://YOUR_TOKEN@github.com/AchengBusiness/happycapy-office-ui.git main

# 或者设置 remote URL（推荐，只需设置一次）
git remote set-url origin https://YOUR_TOKEN@github.com/AchengBusiness/happycapy-office-ui.git
git push -u origin main
```

### 方法 3: 使用 SSH（如果已配置 SSH 密钥）

```bash
# 更改 remote URL 为 SSH
git remote set-url origin git@github.com:AchengBusiness/happycapy-office-ui.git

# 推送
git push -u origin main
```

## 📦 提交信息

当前提交包含：
- 17 个文件
- 1585 行代码
- 完整的项目文档
- 全身水豚角色精灵图
- 等距豪华办公室背景
- Flask 后端服务
- Phaser 游戏引擎前端

## 🔐 安全提示

- ⚠️ 不要将 Personal Access Token 提交到代码中
- ⚠️ Token 应该保密，不要分享给他人
- ✅ 推送成功后，你的 token 会被 Git 记住（存储在 .git/config 中）

## 📝 推送后验证

推送成功后，访问你的仓库：
https://github.com/AchengBusiness/happycapy-office-ui

你应该能看到：
- README.md（项目首页）
- 所有源代码文件
- 精灵图和背景图
- 文档文件

## 🌐 设置为公开仓库

如果仓库默认是私有的，需要设置为公开：

1. 访问仓库设置: https://github.com/AchengBusiness/happycapy-office-ui/settings
2. 滚动到 "Danger Zone"
3. 点击 "Change visibility"
4. 选择 "Public"
5. 确认操作

---

**需要帮助？** 如果遇到问题，请检查：
- GitHub 仓库是否已创建
- Token 权限是否正确（需要 repo 权限）
- 网络连接是否正常
