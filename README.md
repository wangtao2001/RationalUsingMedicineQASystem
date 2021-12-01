## 1.运行前配置

1.1 配置 ./web/static/js/neovis-config.js 中 第4、5行 server_user 与 server_password，填写neo4j数据库账号密码

1.2 配置 ./system/QASystem/views.py 中 第6、7行 user 与 password，填写neo4j数据库账号密码

## 2.问答接口

在 ./system/QASystem/views.py 中，第 22 行的 question 表示前端页面传入的问题，第25-29行为需要返回的数据

answer 填写问答系统回答问题返回的答案

- 当只有中心结点时，将answer_node_names设为空数组，answer_node_type设为空字符串，此时只会显示中心结点的全部关系
- 存在答案结点时，在answer_node_names传入所有答案结点的名称，answer_node_type传入答案结点的类型，此时不仅显示中心结点的全部关系，且会将答案结点变大

源文件中填写了示例数据

## 3.项目本地运行

3.1 启动neo4j数据库

3.2 进入 ./system 目录下，使用命令行输入 python ./manage.py runserver , 此时会在本地8000端口启动后端服务（需要 python 版本3.6以上和 包django和py2neo）

3.3 使用 HBuliderX 打开 ./web目录（可能需要首先安装 npm）, 使用编辑器上方 运行、运行到浏览器，待编译完成后，会在本地打开8080和8081端口。在浏览器中输入http://127.0.0.1:8080/ 或 http://localhost:8080/ 即可访问页面主页
