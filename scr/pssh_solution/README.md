<h3 align='center'> pssh solution </h3>

#### 文件说明

- `bindUSB.sh`

    移除 linux 内核的 usb 存储器驱动 `/lib/modules/$(uname -r)/kernel/drivers/usb/storage`

- `configCodeblocks.sh`

    为了防止 code::blocks 闪退，应关闭 `symbol complete` (~~应该叫这个~~)

- `createUser.sh`

    从设置里读取用户名和密码，并创建以此为用户名和密码的 linux 普通权限账户

- `deluser.sh`

    从设置里读区用户名，删除此用户

- `desktop_hostname.py`

    设置选手机的桌面为其学校的校徽

    更改选手机的 `hostname` 为其座位号

- `fixtime.sh`

    同步选手机和服务的时间

- `getpath.py`

    一个没有什么用的 python 模块，但是你不能删它:)

- `lightscreen.sh`

    杀死 gdm 进程以达到亮屏的效果

    ~~没啥卵用~~

- `mkLink2oj.sh`

    从设置中读取用户名，在此用户的桌面添加指向 domjudge 的快捷方式

- `screen.sh`

    屏幕分辨率的修正脚本

- `sendFile2login.py`

    给选手机分发登录到 domjudge 的凭据

- `setStudentComputer.sh`

    一个部署静态 ip 并且设置 sshd 和默认桌面壁纸的脚本

    需要一个 mac:ip 的对应表，这个表写在该脚本中

