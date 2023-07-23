> docker build -t pycodebr-db .

> docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=Pycodebr  
> -e MYSQL_USER=MainUse -e MYSQL_PASSWORD=MainPassword pycodebr-db
