<h1 align='center'> 从 icpc 官网爬取所有学校信息的爬虫 </h1>

## 文件说明

### main.py

主程序, 运行这个启动爬虫 (它负责获取 `icpc` 官网的auth_key)
    
运行过程中会生成一些临时文件，完成后会被自动删除
    
**NOTE**: 运行前先把文件中的 `username` 和 `password` 填了
    
### robot.sh

爬虫主体, 负责从爬去信息, 最后返回 `main.py` 并由它整理这些爬取的内容
    
### result.json

生成的信息, 格式:
```json
[
    {
        "id": id(int),
        "name": "school name",
        "url": "School official website",
        "country": "abbr country name"
    }
]
```
    
## 运行环境

- x86_64 GNU/Linux

- Python 3.7.4

    - selenium 


