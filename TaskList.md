## For Team Workstations

- 删除旧用户
- (建议)创建系统服务, 使其每分钟自动获取一次 IP 地址 (执行 `netplan apply`)
- 禁用 usb
- 创建用户, 并添加
  - OJ 链接
  - OJ 用户名和密码
  - codeblocks 的配置文件
- 更改 hostname 并设置左面为学校校徽
- 修正时间

## For Jury Workstations

- 修改 hostname (用以 Domjudge 识别)
- 修改凭据文件 (~~位置忘了...~~)

## For Web Server

- 导入队伍信息
- 导入账号信息
- 导入学校信息
- 向数据库添加队伍的详细信息
  - 队伍所属学校
  - 队伍的座位号
- 向数据库添加学校的详细信息(~~具体忘了...~~)
- 添加用于 judgehost 的账户

- 可能需要清除缓存, 重新部署数据库
