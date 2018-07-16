import tornado
import tornado.web
import json
import time
import os
import base64
import cv2

class hollow(tornado.web.RequestHandler):
    def set_default_headers(self):
        # print("setting headers!!!")
        self.set_header("Access-Control-Allow-Origin", "*")  # 这个地方可以写域名
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def get(self):
        # print(233)
        filename = self.get_argument("stl")

        print(filename)
        with open(filename, "r")as f:
            x = f.read()
        print("文件大小",len(x))
        self.write(x)

    def post(self):
        print("post")
        # 时间戳
        t = time.time()
        nowTime = lambda: int(round(t * 1000))
        # 接收数据 转化为img 打时间戳 保存
        bd = self.request.body
        jsons = json.loads(bd)
        img = jsons["base64"]
        img = img[img.find(",") + 1:]
        imgdata = base64.b64decode(img)
        filent = str(nowTime())
        filename = "data/" + "img" + filent + ".png"
        f = open("./hollow/" + filename, "wb")
        f.write(imgdata)
        f.close()
        img=cv2.imread("./hollow/"+filename)
        cv2.imwrite("./hollow/"+filename,img)
        # 读取配置文件
        with open("./hollow/config.json")as f:
            config = f.read()
            print(config)
        config = json.loads(config)
        outputfilename = "data/" + "stl" + str(nowTime()) + ".stl"
        cmdstr=r".\\hollow\\" + config["exename"] + " " + "./hollow/" + filename + " ./hollow/" + outputfilename
        print(cmdstr)
        r = os.popen(r".\\hollow\\" + config["exename"] + " " + "./hollow/" + filename + " ./hollow/" + outputfilename)
        r = r.read()
        print(r)
        # with open("./hollow/"+outputfilename,"w")as f:
        # f.write("33299999")
        stl = "http://" + str(config["serveip"]) + ":" + str(
            config["serveport"]) + "/hollow?stl=./hollow/data/stl" + str(nowTime()) + ".stl"
        j = {"model": stl}
        self.write(json.dumps(j))


if __name__ == "__main__":
    pass
    # r = os.popen("test 233 333")
    # print(r.read())
    # img="xxxx,aaaa"
    # img=img[img.find(",")+1:]
    # print(img)
