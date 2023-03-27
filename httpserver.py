'''
htttpserver v2.0
env python3.11
io多路复用 和 http 训练
'''

from socket import *
from select import *


# 具体功能实现
class HTTPServer:
    # 服务器文件类型字典
    dic = {'.css': 'text/css', '.js':'application/x-javascript', '.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/jpeg'}

    def __init__(self, host='127.0.0.1', port='8888', dir='./'):
        self.host = host
        self.port = port
        self.dir = dir
        self.address = (host, port)
        # 实例化对象时直接创建套接字
        self.create_socket()
        self.bind()
        # 多路复用列表
        self.rlist = []
        self.wlist = []
        self.xlist = []


    # 创建套接字
    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # 绑定套接字
    def bind(self):
        self.sockfd.bind(self.address)

    # 启动服务
    def server_forever(self):
        self.sockfd.listen(100)
        # print('listen the port %d'%self.port)
        # IO多路复用接受客户端请求
        self.rlist.append(self.sockfd)
        while True:
            rs, wx, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print('Connect from', addr)
                    self.rlist.append(c)
                else:
                    # 处理请求
                    self.handle(r)

    def handle(self, connfd):
        # 接受HTTP请求
        request = connfd.recv(4096)
        # 客户端断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 提取请求内容 （字节串按行分割）
        request_line = request.splitlines()[0]
        info = request_line.decode().split(' ')[1]
        print(connfd.getpeername(), ':', info)

        # 根据请求内容进行数据整理
        # 分为两类 1. 请求网页  2. 其他
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)

    # 返回网页
    def get_html(self, connfd, info):
        if info == '/':
            # 请求主页
            filename = self.dir + '/index.html'
        else:
            filename = self.dir + info
        try:
            fd = open(filename, 'r', encoding='utf-8')
        except Exception:
            # 网页不存在
            response = 'HTTP/1.1 404 Not Found\r\n'
            response += 'Content-Typy:text/html\r\n'
            response += '\r\n'
            response += '<h1>Sorry...<h1>'
        else:
            # 网页存在
            response = 'HTTP/1.1 200 OK\r\n'
            response += 'Content-Typy:text/html\r\n'
            response += '\r\n'
            response += fd.read()
        finally:
            connfd.send(response.encode())

    # 返回数据
    def get_data(self, connfd, info):
        pass
        # 未完待续
    #     if info[-4:].lower() == '.css':
    #         self.sendatajs(connfd, '.css', info)
    #     if info[-3].lower() == '.js':
    #         self.sendatajs(connfd, '.js', info)
    #     if info[-4].lower() == '.png':
    #         self.sendataimg(connfd, '.png', info)
    #     if info[-4].lower() == '.jpg':
    #         self.sendataimg(connfd, '.jpg', info)
    #     if info[-5].lower() == '.jpeg':
    #         self.sendataimg(connfd, '.jpeg', info)
    #     if info[-5].lower() == '.webp':
    #         self.sendataimg(connfd,'.webp',info)
    #
    # # 处理js文件
    # def sendatajs(self,connfd, str, info):
    #     filename = self.dir + info
    #     try:
    #         fd = open(filename, 'r', encoding='utf-8')
    #     except Exception:
    #         # 网页不存在
    #         response = 'HTTP/1.1 404 Not Found\r\n'
    #         response += 'Content-Typy:%s\r\n'%self.dic[str]
    #         response += '\r\n'
    #         response += '<h1>Sorry...<h1>'
    #     else:
    #         # 网页存在
    #         response = 'HTTP/1.1 200 OK\r\n'
    #         response += 'Content-Typy:%s\r\n'%self.dic[str]
    #         response += '\r\n'
    #         response += fd.read()
    #     finally:
    #         connfd.send(response.encode())
    #
    # # 处理图片文件
    # def sendataimg(self,connfd,str,info):
    #     filename = self.dir + info
    #     try:
    #         fd = open(filename, 'br')
    #     except Exception:
    #         # 网页不存在
    #         response = 'HTTP/1.1 404 Not Found\r\n'
    #         response += 'Content-Typy:%s\r\n' % self.dic[str]
    #         response += '\r\n'
    #         response += '<h1>Sorry...<h1>'
    #     else:
    #         # 网页存在
    #         response = 'HTTP/1.1 200 OK\r\n'
    #         response += 'Content-Typy:%s\r\n' % self.dic[str]
    #         response += '\r\n'
    #         response = response.encode() + fd.read()
    #     finally:
    #         connfd.send(response)


# 用户使用HTTPserver
if __name__ == "__main__":
    '''
    通过HTTPServer类快速搭建服务，展示自己的网页
    '''
    # 用户决定的参数
    HOST = '127.0.0.1'
    POST = 8888
    DIR = './MYHTTP/html'  # 网页存储位置
    httpd = HTTPServer(HOST, POST, DIR)  # 实例化类对象
    httpd.server_forever()  # 启动服务
