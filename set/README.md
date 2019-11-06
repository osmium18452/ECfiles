<h1 align='center'> 比赛信息设置 </h1>

## 文件说明

### accounts.tab

队伍的账号信息，用以导入 Domjudge

### teams.tab

队伍信息，用以导入 Domjudge

### info.json

队伍的详细信息，格式：

```json
[
    {
        "externalid": "exid",
        "id": "id",
        "team": "account name",
        "password": [
            "password for warm-up match",
            "password for official match"
        ],
        "photoName": "photo name (签到时拍的)",
        "name": [
            "team name (zh_cn)",
            "team name (en_us)"
        ],
        "location": "location",
        "schoolName": [
            "school name (zh_cn)",
            "school name (en_us)"
        ],
        "mark": "team mark (e.g. star)",
        "ip": "ip addr for team work station",
        "members": [
            "member 1",
            "member 2",
            "member 3"
        ]
    }
]
```

---

### home

gnome 的某种认证文件（我也不知道这是啥，但是没有的话，桌面图标就无法使用）

### icon2oj.png

指向 Domjudge 的桌面快捷方式的图标

### link2oj.desktop

指向 Domjudge 的桌面快捷方式

### username

脚本创建用户时使用的用户名

### passwd

脚本创建用户时使用的密码

### codeblocks

code::blocks 配置文件（默认配置，但是关闭了****补全，以防止闪退）
 
### ipmac.json

选手机 ip 和 mac 的对应关系（静态 ip 需要），格式：
```json
{
    "mac": "ip"
}
```

---

### pic.tar.gz

参赛学校的校徽（学校中文名.jpg（png？））<br> 使用时要解压。。。

### JoinedSchool

所有参加的学校（中文名）<br> ~~我也不知道当时为啥弄个这个~~


### SchoolInfo.json

学校信息的 json，格式：

```json
{
    "school name(en_us)": [
        "abbr school name",
        "abbr country name"
    ]
}
```

### SchoolNameCH_EN.json

学校中英文名对照表，格式：

```json
{
    "school name(zh_cn)": "school name(en_us)"
}
```

### sname2id.json

学校英文名和学校 id 的对照表，格式：

```json
{
    "school name(en_us)": "id"
}
```
