# How to Deploy Flask Web Application with MySQL
## Create VM/Instance & Connect using SSH
1. Launch AWS EC2 Instance(Specification) <br>
    **1.1 Instance Type**: t2.micro <br>
    **1.2 Key Pair Name**: mujahed <br>
    **1.3 Security Group**: sgDefault and sgAllTraffic <br>
2. Connect using SSH Command
    ``` bash
    ssh -i key.pem username@public_ip
    ```
## Clone Web App on Server
1. Install Git Command line tool()
    ``` sh
    sudo su
    sudo apt update
    sudo apt install git -y
    git --version
    ```
2. Clone Git Repository
    
    ``` git
    git clone https://github.com/NubeEra-MCO/PyFlaskMySQL-DockerfileCompose.git
    ```
 3. Prepare 2 Containers and Deploy Application using Dockerfile technique
    ``` sh
    cd PyFlaskMySQL-DockerfileCompose/01.WithDockerfile    
    chmod +x docker-Commands.sh
    ./docker-Commands.sh
    ```
4. Prepare 2 Containers and Deploy Application using Docker Compose(YAML) technique
    ``` sh
    cd PyFlaskMySQL-DockerfileCompose/02.Compose
    chmod +x docker-Commands.sh
    ./docker-Commands.sh
    ```