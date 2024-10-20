// دالة لتحديث الوقت
function updateTime() {
    var now = new Date();  // جلب الوقت الحالي
    var currentTime = now.getFullYear() + '-' +
        ('0' + (now.getMonth() + 1)).slice(-2) + '-' + 
        ('0' + now.getDate()).slice(-2) + ' ' + 
        ('0' + now.getHours()).slice(-2) + ':' + 
        ('0' + now.getMinutes()).slice(-2) + ':' + 
        ('0' + now.getSeconds()).slice(-2);
    
    document.getElementById("currentTime").innerHTML = currentTime;  // تحديث DOM
}

// استدعاء الدالة كل ثانية
setInterval(updateTime, 1000);