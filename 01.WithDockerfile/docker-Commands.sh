#!/bin/bash
docker stop $(docker ps -a -q) && docker rm $(docker ps -a -q)
docker rmi $(docker images -q)

docker build -t flask-app -f FlaskDockerfile .
docker build -t mysql-container -f MySQLDockerfile .

docker run -d --name mysql-db mysql-container
# docker run --name mysql-container -e DB_HOST=localhost -e DB_USER=root -e DB_NAME=dev1 -e TABLE_NAME=users -e DB_PASSWORD=123 -d mysql
# docker exec -it mysql-container mysql -uroot -p

# Wait to create proper mysql-container
sleep 30
ip=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql-db)

dbName=dev1
tableName=users
dbUserName=db_user
dbPwd=123

docker run -d -p 5000:5000 --name flask-app -e DB_HOST=$ip -e DB_USER=dbUserName -e DB_PASSWORD=$dbPwd -e DB_NAME=$dbName -e TABLE_NAME=$tableName flask-app


# docker exec -it mysql-container mysql -uroot -p123
# docker exec -it flask-app bash
#     bash# apt update && apt install curl -y
#     bash# curl http://localhost:5000/insert
#     bash# curl http://localhost:5000/select
# docker logs flask-app
