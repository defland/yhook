# Yhook
   
   基于Flask的webhook自动部署脚本
   在写项目时候，发现github的webhook功能很强大，可以做到本地开发好的代码，gitpush到仓库，然后直接同步到服务器中，相当于push master分支等于直接部署到服务器中。但网上比较多webhook工具都比较重量级，干脆自己搞一个脚本。

# Keyword
  
  Yhook：
  CentOS环境 + Flask（接受webhook POST消息）+ gunicorn（部署flask） + Nginx(反向代理)

# 实现需求

- 生成Payload URL，接受github推送的JSON消息
- 收到webhook JSON消息后，执行本地脚本（更新代码，重启web服务）
