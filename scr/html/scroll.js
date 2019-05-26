var wait_time = 3000;
var down_speed = 4;
var up_speed = down_speed * 50;
var down_cnt = wait_time / 30;
var up_cnt = wait_time / 30;
var c_bottom = 0;
var c_top = 0;

setInterval(function () {
    if (window.scrollY === undefined || window.scrollX === undefined) window.scrollTo(window.scrollX, 0);
    if (window.pageYOffset + window.innerHeight >= document.body.offsetHeight) c_bottom++;
    if (c_bottom === down_cnt) {
        setTimeout(function scroll_back() {
            window.scrollTo(window.scrollX, window.scrollY - up_speed);
            if (window.scrollY <= 0) {
                location.reload();
                return;
            }
            setTimeout(scroll_back, 30);
        }, 30);
        c_bottom = 0;
        c_top = 0;
        return;
    }
    if (c_top >= up_cnt) window.scrollTo(window.scrollX, window.scrollY + down_speed);
    c_top++;
}, 30);
