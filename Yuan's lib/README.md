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