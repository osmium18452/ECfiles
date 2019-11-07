<h3 align='center'> Information Generator </h3>

## 文件说明

### gentabfile.py

生成 `accounts.tab` 和 `teams.tab` 

> 将这两个文件分别导入 domjudge 的账号和队伍，即可完成队伍信息的录入

`accounts.tab` 结构：

| Field | Type | Null | Comments |
|-|-|-|-|
| role | str | NO | 账号规则（team、admin等）|
| name | str | YES | 没什么卵用的字段，一般留空 |
| username | str | NO | 登陆用户名，用户名中 **最后出现** 的 **一串数字** 应当是其相应的 **队伍的id** |
|password | str | YES | 登陆密码，可以先留空，最后在domjudge的账号管理处批量生成 |


`teams.tab` 结构：

| Field | Type | Null | Comments |
|-|-|-|-|
| teamid | int | NO | 队伍的id |
| externalid | int | YES | 队伍的扩展id，一般与teamid相等 |
| categoryid | int | NO | 队伍类别的id，如 system，jury，star，girl等 |
| team name | str | NO | 队伍名 |
| affiliation name | str | YES | |
| abbr. affiliation name | str | YES | affiliation name 的简写 |
| country | str | YES | affiliation 的所属国家，三个字母表示 |

**Requirement**
- [info.json](../../set/README.md#infojson)
- [SchoolInfo.json](../../set/README.md#schoolinfojson)
    
---

### mkAffili.py

生成 `team_Affiliation` 表需要的信息，表结构：

| Field | Type | Null | Key | Default | Extra |
|-|-|-|-|-|-|
| affilid | int(4) unsigned | NO | PRI | NULL | auto_increment |
| externalid | varchar(255) | YES | UNI | NULL | |
|shortname | varchar(32) | NO | | NULL | |
| name | varchar(255) | NO | | NULL | |
| country | char(3) | YES | | NULL | |
| comments | longtext | YES | | NULL | |

**Requirement**
- [JoinedSchool](../../set/README.md#joinedschool)
- [SchoolInfo.json](../../set/README.md#schoolinfojson)
- [SchoolNameCH_EN.json](../../set/README.md#schoolnamech_enjson)
    
---

### insertAffili.py, insertRoom.py

生成 `sql` 插入队伍的 `Affiliation` 和 `room`

> domjudge 队伍信息的导入不支持 Affiliation(学校信息), room(座位号) 等信息

**Requirement**
- [info.json](../../set/README.md#infojson)
- [sname2id.json](../../set/README.md#sname2idjson)
    > 学校的 id 在使用 mkAffli.py 生成的 sql 插入数据库后可从数据库读取。
    
---

### procPic.py

将小的校徽图片处理成 `1920x1080` 的大图片，用作桌面壁纸

~~没什么卵用，不如用 PS~~
    
---
    
### getpath.py

获取相对于脚本的相对路径的绝对路径

~~一个没什么卵用的 python 模块，但是不能删:)~~
    
---

### AllSchoolInfo 
·
[从 `icpc` 官网获取所有学校信息的爬虫](./AllSchoolInfo)
