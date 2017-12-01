# coding:utf-8
from flask import Flask,request
app = Flask(__name__)

import commands,os

# 全局变量

# learoom项目系统路径
PROJECT_A_PATH = '/home/yg/www/learoom_dev/'
PROJECT_A_DEV_PATH = '/Users/yg/Documents/code/Project/learoom_dev/'

PROJECT_B_PATH = '/home/yg/server/Yhook'
PROJECT_B_DEV_PATH = '/Users/yg/Documents/code/Project/Yhook'

PROJECT_DEV_PATH = '/home/yg/www/learoom_stable/'
PROJECT_STABLE_PATH = '/home/yg/www/learoom_stable/'

SYSTEMD_PROJECT_A = 'learoom_dev.service' # web网站项目的自启动服务名称
SYSTEMD_PROJECT_B = 'yhook.service' # yhook的自启动服务名
SYSTEMD_PROJECT_STABLE = 'learoom_stable.service' # 稳定业务服务

# 负责项目A的消息接受,webhook的路径 域名:端口/learoom
@app.route('/',methods=['POST','GET'],strict_slashes=False)
@app.route('/index',methods=['POST','GET'],strict_slashes=False)
@app.route('/learoom_dev',methods=['POST','GET'],strict_slashes=False)
def learoom():

    if request.method == "GET":
        return "pelase use POST"

    # x = request.form
    # print x
    # x = str(x)
    
    print "pull code ing ...."
    # 拉取代码和重启web服务
    comm = 'cd %s && ls -l && git status && git reset --hard && git pull' % PROJECT_A_PATH
    pull_code(comm)
    print "pull code done!"

    print "restart serve  ing ...."
    comm2 = 'sudo systemctl restart %s && sudo systemctl status %s'  % (SYSTEMD_PROJECT_A,SYSTEMD_PROJECT_A)
    restart_server(comm2)
    print "restart serve done!"

    return '< Project: learoom_dev >: Pull code and restart app done!' 

# 负责项目B的消息接受
@app.route('/yhook',methods=['POST','GET'],strict_slashes=False)
def yhook():

    if request.method == "GET":
        return "pelase use POST"

    # x = request.form
    # print x
    # x = str(x)
    
    # 拉取代码和重启web服务
    comm = 'cd %s && ls -l && git status && git reset --hard && git pull' % PROJECT_B_PATH # 同步项目代码
    pull_code(comm)
    
    comm2 = 'sudo systemctl restart %s && sudo systemctl status %s'  % (SYSTEMD_PROJECT_B,SYSTEMD_PROJECT_B) #  重启服务
    restart_server(comm2)

    return '< Project: yhook >: Pull code and restart app done!' 


# # 负责learoom项目正式服务的更新、重启
# @app.route('/ctl/<comm>',methods=['POST','GET'],strict_slashes=False)
# def ctl(comm):
#     # comm: git_updata,cp_update,restart,update_db,get_db,
#     if request.method == "GET":
#         return "Pelase use POST,<br> comm: git_updata,cp_update,restart,update_db,get_db"


# 正式服务器
# @app.route('/stable',methods=['POST','GET'],strict_slashes=False)
# def learoom_stable():

#     if request.method == "GET":
#         return "pelase use POST"

#     # x = request.form
#     # print x
#     # x = str(x)
    
#     print "pull code ing ...."
#     # 拉取代码和重启web服务
#     comm = 'cd %s && ls -l && git status && git reset --hard && git pull' % PROJECT_STABLE_PATH
#     pull_code(comm)
#     print "pull code done!"

#     print "restart serve  ing ...."
#     comm2 = 'sudo systemctl restart %s && sudo systemctl status %s'  % (SYSTEMD_PROJECT_STABLE,SYSTEMD_PROJECT_STABLE)
#     restart_server(comm2)
#     print "restart serve done!"

#     return '< Project: learoom_stable >: Pull code and restart app done!' 




# 拉取gitpull
def pull_code(comm=''):

    # 执行
    # cd /home/yg/www/leanroom/
    # git reset --hard
    # git pull

    print comm
    (status, output) = commands.getstatusoutput(comm)
    print status, output


# 重启服务器
def restart_server(comm=''):


    print comm
    (status, output) = commands.getstatusoutput(comm)
    print status, output


if __name__ == '__main__':
   
    app.run(DEBUG = True)

