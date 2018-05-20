document.write("<script src=\"qrcodealg.js\"></script>");
/*
* Use:生成二维码图片
*  二维码一个点 10像素 对于最大的二维码可能需要准备接近2k x 2k的大小的画布
* @param {string} strings 二维码包含的文字信息
* @param {string} canvasid 一个画布id 画布用于盛放二维码预览
* @return {string} 返回二维码所对应的base64字符串 用于传回后台处理
* */
function createqr(strings,canvasid) {
    var qrObj=new QRCodeAlg(strings,3);
    let arrs=qrObj.modules;
    show(arrs,canvasid);
    let base64_str=CanvasToImage(canvasid);
    return base64_str;
}
/*
* Use: 将画布内容转为jpeg base64编码
* @param {string} canvasid 画布的id
* @return {string} 画布内容的jpeg base64编码
 */
function CanvasToImage(canvasid) {
    //新Image对象，可以理解为DOM
    var canvas=document.getElementById(canvasid);
    var image = new Image();
    // canvas.toDataURL 返回的是一串Base64编码的URL，当然,浏览器自己肯定支持
    image.src = canvas.toDataURL("image/jpeg");
    return image.src;
}

/*
*  Use:将二维码显示在画布上
*  1为黑色 2~9为 1~8对应的数字
*  @param {Array[][]} arr 二维码的二维矩阵 1黑0白 (0,0)为第一个模块
*  @param {string} canvasid 要显示的画布的id
* */
function show(arr,canvasid) {
    // alert("show1");
    var c=document.getElementById(canvasid);
    var cxt=c.getContext("2d");
    let cxt2=c.getContext("2d");
    cxt.fillStyle="#000000";
    // alert("show2");
    var wid=10;

    for(let i=0;i<=arr.length-1;i++){
        for(let j=0;j<=arr[0].length-1;j++){

            switch (arr[i][j]){
                case 2:{  cxt.fillStyle="#ff0721";break;}
                case 3:{  cxt.fillStyle="#ffa812";break;}
                case 4:{  cxt.fillStyle="#f7ff0c";break;}
                case 5:{  cxt.fillStyle="#11ff02";break;}
                case 6:{  cxt.fillStyle="#07fff0";break;}
                case 7:{  cxt.fillStyle="#0aa9ff";break;}
                case 8:{  cxt.fillStyle="#0227ff";break;}
                case 9:{  cxt.fillStyle="#ff0af3";break;}
            }
            if(arr[i][j]==1){
                // alert("231");

                cxt.fillStyle="#000000";
            }
            if(arr[i][j]==1){
                cxt.fillRect(j*wid+1,i*wid+1,wid,wid);}
            else if(arr[i][j]!=0){
                cxt2.font="9px Arial";
                cxt2.strokeText(""+(arr[i][j]-1),j*wid+3,i*wid+10);

            }
        }
    }
}