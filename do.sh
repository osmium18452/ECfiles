#!/usr/bin/env bash 
dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )
cd $dir

while (true); do

    cat << EOF



*****************************************************
*                                                   *
*                                                   *
*            1. 创建用户                            *
*            2. 更改 hostname 并且设置桌面          *
*            3. 添加 oj 链接                        *
*            4. 发送 oj 帐号密码(0)                 *
*            5. 禁止 usb                            *
*            6. 删除用户                            *
*            7. 修正时间                            *
*            8. 点亮屏幕                            *
*            9. 自动获取ip                          *
*            q. 退出                                *
*            *. 重新输入                            *
*                                                   *
*                                                   *
*****************************************************

in: 
EOF
    read chc
    clear
    case $chc in
        1) ./scr/pssh_solution/createUser.sh ;;
        2) ./scr/pssh_solution/desktop_hostname.py ;;
        3) ./scr/pssh_solution/mkLink2oj.sh ;;
        4) ./scr/pssh_solution/sendFile2login.py ;;
        5) ./scr/pssh_solution/bindUSB.sh ;;
        6) ./scr/pssh_solution/deluser.sh ;;
        7) ./scr/pssh_solution/fixtime.sh ;;
        8) ./scr/pssh_solution/lightscreen.sh ;;
        9)
            pscp -h iplist -t 1 './scr/pssh_solution/autogetip.sh' '/root/xx.sh'
            pssh -h iplist -t 1 'nohup /root/xx.sh &' > /dev/null
            ;;
        q)
            echo "quit"
            break
            ;;
        *) echo "重新输入" ;;
    esac
done

