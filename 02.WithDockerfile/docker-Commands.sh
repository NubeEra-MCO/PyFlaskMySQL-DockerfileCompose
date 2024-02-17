docker build -t flask-app -f FlaskDockerfile .
docker build -t mysql-container -f MySQLDockerfile .

docker run -d --name mysql-db mysql-container

docker run --name mysql-container -e DB_HOST=localhost -e DB_USER=root -e DB_NAME=dev1 -e TABLE_NAME=users -e DB_PASSWORD=123 -d mysql
docker exec -it mysql-container mysql -uroot -p



docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mysql-db
docker run -d -p 5000:5000 --name flask-app -e DB_HOST=<MySQL_Container_IP> -e DB_USER=db_user -e DB_PASSWORD=db_password -e DB_NAME=dev1 -e TABLE_NAME=users flask-app


curl http://localhost:5000