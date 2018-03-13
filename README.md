# Yhook
   
   基于Flask的webhook自动部署脚本
   在写项目时候，发现github的webhook功能很强大，可以做到本地开发好的代码，gitpush到仓库，然后直接同步到服务器中，相当于push master分支等于直接部署到服务器中。但网上比较多webhook工具都比较重量级，干脆自己搞一个脚本。

# 流程

[![9fLDaQ.md.png](https://s1.ax1x.com/2018/03/13/9fLDaQ.md.png)](https://imgchr.com/i/9fLDaQ)

# 原理和步骤
  Yhook：
  CentOS + Flask+ gunicorn + Nginx
  
  基本流程（本地开发->github仓库->外网服务器）：
  
1. 本地开发完成，推送Master分支
2. github触发webhook消息，推送一条request(POST)推送到某个URL(用Yhook就是为了生成这条接收URL)上，告知有代码更新
3. Yhook服务接收到消息，执行本地shell脚本（git pull、重启web服务等操作）
4. 从而实现推送即部署。

# 实现需求

v1 (100%)
- 生成Payload URL，接受github推送的JSON消息。
- 收到webhook JSON消息后，执行本地脚本（更新代码，重启web服务）。



