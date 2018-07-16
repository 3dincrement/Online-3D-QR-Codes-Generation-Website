# Yuan's lib
## qrcreate
demo.html里已经基本表明了用法  
首先包含  qrcreater.js (同目录的qrcodealg.js要放在一起)
然后调用
* createqr(strings,canvasid)  
@param {string} strings 二维码包含的文字信息  
@param {string} canvasid 一个画布id 用于盛放二维码预览  
@return {string} 返回二维码所对应的base64字符串    
即可生成并显示二维码
    
## serve
服务后端  
* 配置文件 config.json 决定服务端口
* 启动serve.py即可启动服务器  
###### 依赖 tornado opencv-python python3.6
### hollow
* 功能: 前端传回二维码图片base64  
后端接受 调用cpp 生成镂空stl 并将stl的url传回前端
* httppost传入: json  
* 格式:{"base64":x}   
x为二维码图片的base64编码  
* 返回:  json: {"model":x}  
x为输出stl 文件的url
* 用法:httppost ip + 端口 + hollow  
例"http://localhost:2000/hollow"
* cpp部分接口:  
传入参数1: 空 系统默认  
传入参数2: png图片的相对路径 例如: ./data/img1526983538974.png
传入参数3: stl图片应该输出的路径及文件名   
例如: ./data/stl1526983538974.stl  
* cpp可执行文件放置:
位于Yuan's lib\serve\hollow下 请自行在配置文件中填入exe名称(默认为test)
* 配置文件config.json: "exename":x (str)  
x为打包好的可执行文件的名称  
"serveip": 服务器ip (str)  
"serveport":服务器端口 (int)