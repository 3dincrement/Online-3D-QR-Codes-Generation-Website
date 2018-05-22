import tornado
import os
import json
import hollow.hollow
import tornado.web



if __name__=="__main__":
    with open("config.json")as f:
        configs=f.read()
    configs=json.loads(configs)
    print(configs["serveport"])
    app = tornado.web.Application([
        (r"/hollow", hollow.hollow.hollow)

    ])
    app.listen(configs["serveport"])
    tornado.ioloop.IOLoop.current().start()
1