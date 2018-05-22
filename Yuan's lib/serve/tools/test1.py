import requests
import json

if __name__=="__main__":
    # with open("data/233.txt")as f:
    #     t=f.read()
    #     print(t)
    sess=requests.session()
    datas={
        "base64":"2333aaaa"
    }
    # r=sess.get("http://localhost:2000/hollow")
    r=sess.post("http://localhost:2000/hollow",data=json.dumps(datas))
    print(r.text)