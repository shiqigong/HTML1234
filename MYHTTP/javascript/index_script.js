//获取第二个img元素对象
var changeImage = document.querySelector('.image_');
// console.log(changeImage);
function sayHello() {
    // 获取当前时间
    var new_time = new Date();
    // 获取当前时间小时
    var new_hours = new_time.getHours();
    // console.log(new_hours);
    if (new_hours < 12) {
        // 如果时间小于十二点则显示早上好图片
        changeImage.src = "../jpg/morning.jpeg";
    } else if (new_hours < 18) {
        // 如果时间小于十八小时则显示下午好图片
        changeImage.src = "../jpg/afternoon.jpeg";
    } else {
        // 其余时间则为晚上好
        changeImage.src = "../jpg/good_night.jpeg";
    }
    
}
sayHello();



