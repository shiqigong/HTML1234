function showTime(clock) {
    // 获取当前时间
    var now = new Date();
    // 获取当前时间的当前年
    var year = now.getFullYear();
    // 获取当前时间的当前月-1月，因为是从0开始的
    var month = now.getMonth();
    // 获取当前时间当前月份的第几天
    var day = now.getDate();
    // 获取当前时间的当前小时
    var hour = now.getHours();
    // 获取当前时间的当前分钟
    var minu = now.getMinutes();
    // 获取当前时间的当前秒
    var second = now.getSeconds();

    month = month + 1;
    // 创建一个数组，下面用索引来获取周几
    var arr_work = new Array("星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六");
    // 获取周几
    var week = arr_work[now.getDay()];
    var time = year + "年" + month + "月" + day + "日 " + week + " " + hour + ":" + minu + ":" + second;
    // 设置标签内容
    clock.innerHTML = time;
}
// 网页加载完成后立刻执行后面的函数
window.onload = function () {
    // 获取标签对象
    var clock = document.getElementById("clock");
    // 每1s调用一次showTime(clock)函数
    window.setInterval("showTime(clock)", 1000);
}