import os
import getpass
import aws
import accessories

i = 3
while i>0:
	password = getpass.getpass("Enter the password : ")
	passwd = "arth"

	if passwd == password:
		os.system("clear")		
		break
	else:
		print("The provided password is incorrect")	  
		i-=1
		if i == 0:
			print("Too many incorrect attempts")
			exit()
		else:
			print("Try again, {} chances left".format(i))

def linux():
    #cmd = input("Enter the command you want to run :- ")
    #cmd_out = os.system(" {} ".format(cmd))
    #return cmd_out
    while True:
        os.system("clear")
        accessories.figlet("Linux","Poison",4)
        os.system("tput bold")
        os.system("tput setaf 2")
        print("""
        Select from the options below\n
        [1] : Know system date and time
        [2] : See calender
        [3] : Know current directory
        [4] : Create an empty file
        [5] : Create a directory
        [6] : See the content of a file 
        [7] : Write some data in a file
        [8] : Copy a file/directory
        [9] : Move a file
        [10] : Move a directory
        [11] : Check OS details
        [12] : Know the IP of this System
        [13] : See how much RAM is free
        [14] : see the CPU details
        [15] : See all the partitions and disks attached to this system
        [16] : See the details of all the Filesystems
        [17] : Return to main menu
        [18] : Exit
        """)
        os.system("tput sgr o")
        cmd = input("Enter your choice :- ")
        if int(cmd) == 1:
            os.system("date")
            accessories.wait()
        elif int(cmd) == 2:
            os.system("cal")
            accessories.wait()
        elif int(cmd) == 3:
            os.system("pwd")
            accessories.wait()
        elif int(cmd) == 4:
            file_name = input("Enter the path with file name where the file has to be created :- ")
            #file_path = input("Enter the path to the directory where you want to create the file :- ")
            os.system("touch {}".format(file_name))
            accessories.wait()
        elif int(cmd) == 5:
            dir_name = input("Enter the directory name :- ")
            os.system("mkdir -p {}".format(dir_name))
            accessories.wait()
        elif int(cmd) == 6:
            file_path = input("Enter the path with the file name :- ")
            os.system("cat {}".format(file_path))
            accessories.wait()
        elif int(cmd) == 7:
            print("""
            [1] : To overwrite the data
            [2] : To append the data
            [3] : Back
            """)
            ch_7 = int(input("Enter your choice :- "))
            if ch_7 == 1:
                file_name = input("Enter the file name :- ")
                print(repr("Note : To give newline in the text use \n between the text and for tab use \t"))
                data = input("Enter the text :- ")
                os.system("printf '{1}' > {0}".format(file_name,data))
                accessories.wait()
            elif ch_7 == 2:
                file_name = input("Enter the file name :- ")
                print(repr("Note : To give newline in the text use \n between the text and for tab use \t"))
                data = input("Enter the text :- ")
                os.system("printf '{1}' >> {0}".format(file_name,data))
                accessories.wait()
            elif ch_7 == 3:
                continue
        elif int(cmd) == 8:
            src = input("Enter the path of the file/directory which you want to copy :- ")
            dest = input("Enter the destination Path :- ")
            os.system("cp -rf {0} {1}".format(src,dest))
            accessories.wait()
        elif int(cmd) == 9:
            src = input("Enter the path of the file which you want to move :- ")
            dest = input("Enter the destination Path :- ")
            os.system("mv -f {0} {1}".format(src,dest))
            accessories.wait()
        elif int(cmd) == 10:
            src = input("Enter the path of the directory which you want to move :- ")
            dest = input("Enter the destination Path:- ")
            os.system("mv -rf {0} {1}".format(src,dest))
            accessories.wait()
        elif int(cmd) == 11:
            print(os.system("cat /etc/os-release"))
            accessories.wait()
        elif int(cmd) == 12:
            os.system("""
            if ifconfig | grep enp0s3 > /dev/null
            then ifconfig enp0s3 | grep inet* | head -n +1 | cut -c 14-26
            else 
            if ifconfig | grep eth0 > /dev/null
            then ifconfig eth0 | grep inet* | head -n +1 | cut -c 14-26
            else echo "Unknown Network Card (NIC)"
            fi
            fi""")
            accessories.wait()
        elif int(cmd) == 13:
            os.system("free -h")
            accessories.wait()
        elif int(cmd) == 14:
            os.system("lscpu")
            accessories.wait()
        elif int(cmd) == 15:
            os.system("fdisk -lL")
            accessories.wait()
        elif int(cmd) == 16:
            os.system("df -hT")
            accessories.wait()
        elif int(cmd) == 17:
            break
        elif int(cmd) == 18:
            exit()
        else:
            print("Invalid choice!!!")
            accessories.wait()
def hadoop():
    while True:
        os.system("clear")
        accessories.figlet("Hadoop Menu","Train",5)
        os.system("tput bold")
        os.system("tput setaf 2")
        print("""
        [1] : Install Hadoop
        [2] : To setup hadoop master
        [3] : To setup hadoop DataNodes(Slaves)
        [4] : Configure hadoop client
        [5] : See Hadoop Cluster details
        [6] : Upload data to hadoop cluster
        [7] : Read data from hadoop cluster
        [8] : Delete data from hadoop cluster
        [9] : Limit the size of Datanode storage
        [10] : Start/Stop Hadoop master
        [11] : Start/Stop Hadoop DataNode
        [12] : Return to main menu
        [13] : Exit
        """)
        os.system("tput sgr 0")
        opt_2 = input("Enter your choice :- ")
        if int(opt_2) == 1:
            #os.system("git clone --quiet https://github.com/Ajaypathak372/arth-team-task1.git > /dev/null")
            os.system("bash ./hadoop")
            accessories.wait()
        elif int(opt_2) == 2:
            hadoop_master()
        elif int(opt_2) == 3:
            hadoop_slave()
        elif int(opt_2) == 4:
            client_ip = input("Enter the IP of the system which you want to cofigure as Hadoop Client :- ")
            #os.system("git clone --quiet https://github.com/Ajaypathak372/arth-team-task1.git > /dev/null")
            os.system("scp -r ./Hadoop-files/client {}:/root > /dev/null".format(client_ip))
            os.system("ssh {0} python3 ~/client/client.py".format(client_ip))
        elif int(opt_2) == 5:
            opt_2_4 = input("Enter the NameNode IP or any DataNode IP associated with Hadoop Cluster :- ")
            print("Hadoop Cluster details are ......")
            os.system("ssh {} hadoop dfsadmin -report".format(opt_2_4))
            accessories.wait()
        elif int(opt_2) == 6:
            client_ip = input("Enter Client IP :- ")
            file_name = input("Enter the file name (with path) you want to upload :- ")
            os.system("ssh {0} hadoop fs -put {1} /".format(client_ip,file_name))
            print("File Successfully uploaded")
            accessories.wait()
        elif int(opt_2) == 7:
            client_ip = input("Enter Client IP :- ")
            file_name = input("Enter the file name whose data you want to read :- ")
            os.system("ssh {0} hadoop fs -cat /{1}".format(client_ip,file_name))
            accessories.wait()
        elif int(opt_2) == 8:
            client_ip = input("Enter Client IP :- ")
            file_name = input("Enter the file name you want to delete :- ")
            os.system("ssh {0} hadoop fs -rm /{1}".format(client_ip,file_name))
            print("File Successfully deleted")
            accessories.wait()
        elif int(opt_2) == 9:
            print("""
            [1] : Extend the Storage
            [2] : Reduce the Storage
            [3] : Back
            """)
            limit = input("Enter your choice :- ")
            if limit == 1:
                ip = input("Enter the DataNode storage IP :- ")
                os.system('ssh {} df -hT'.format(ip))
                ex = input("How much you want to extend? : ")
                vg = input("Enter Your Volume Group Name : ")
                lv = input("Enter Your Logical Volume Name : ")
                os.system('ssh {} lvextend --size {} /dev/{}/{}'.format(ip , ex , vg , lv))
                print("Data Node Storage Sucessfully Extended")
                os.system('ssh {} resize2fs  /dev/{}/{}'.format(ip , vg ,lv))
                os.system('ssh {} df -hT'.format(ip))
                accessories.wait()
            elif limit == 2:
                accessories.wait()
            elif limit == 3:
                continue
        elif int(opt_2) == 10:
            print("""
            [1] : Start
            [2] : Stop
            [3] : Back
            """)
            opt_2_10 = int(input("Enter your choice :- "))
            if opt_2_10 == 1:
                nn_ip = input("Enter the NameNode IP :- ")
                os.system("ssh {} hadoop-daemon.sh start namenode".format(nn_ip))
                print("NameNode Started Successfully")
                accessories.wait()
            elif opt_2_10 == 2:
                nn_ip = input("Enter the NameNode IP :- ")
                os.system("ssh {} hadoop-daemon.sh stop namenode".format(nn_ip))
                print("NameNode Stopped Successfully")
                accessories.wait()
            elif opt_2_10 == 3:
                continue
        elif int(opt_2) == 11:
            print("""
            [1] : Start
            [2] : Stop
            [3] : Back
            """)
            opt_2_11 = int(input("Enter your choice :- "))
            if opt_2_11 == 1:
                nn_ip = input("Enter the DataNode IP :- ")
                os.system("ssh {} hadoop-daemon.sh start datanode".format(nn_ip))
                print("DataNode Started Successfully")
                accessories.wait()
            elif opt_2_11 == 2:
                nn_ip = input("Enter the DataNode IP :- ")
                os.system("ssh {} hadoop-daemon.sh stop datanode".format(nn_ip))
                print("DataNode Stopped Successfully")
                accessories.wait()
            elif opt_2_11 == 3:
                continue
        elif int(opt_2) == 12:
            break
        elif int(opt_2) == 13:
            exit()
        else:
            print("Invalid Choice!!!")
            accessories.wait()

def hadoop_master():
    nn_ip = input("Enter the IP of the system which you want to cofigure as Hadoop Master :- ")
    #nn_username = input("Enter the username :- ")
    #os.system("ssh {0} ".format(nn_ip)) 
    #os.system("git clone --quiet https://github.com/Ajaypathak372/arth-team-task1.git > /dev/null")
    #os.system("ssh {0} python3 -u- < ~/master/master.py".format(nn_ip)")
    os.system("scp -r ./Hadoop-files/master {}:/root > /dev/null".format(nn_ip))
    os.system("ssh {0} python3 ~/master/master.py".format(nn_ip))
    os.system("rm -rf ~/master")
    accessories.wait()
    
def hadoop_slave():
    dn_ip = []
    dn = int(input("How many DataNodes(Slaves) you want to configure :-  "))
    for i in range(0,dn):
        ip = input("Enter the IP Address of the DataNode(Slave) {} :- ".format(i+1))
        dn_ip.append(ip)
        #dn_username = input("Enter the username :- ")
    for j in dn_ip:
        #os.system("git clone --quiet https://github.com/Ajaypathak372/arth-team-task1.git > /dev/null")
        os.system("scp -r ./Hadoop-files/slave {}:/root > /dev/null".format(j))
        print("Configuring Datanode {} ".format(j))
        os.system("ssh {0} python3 ~/slave/slave.py".format(j))
        os.system("rm -rf ~/slave")
    accessories.wait()

def docker():
    while True:
        os.system("clear")
        accessories.figlet("Docker","Blocks",6)
        os.system("tput bold")
        os.system("tput setaf 2")
        print("""
        [1] : Install Docker
        [2] : Start/Stop Docker Services Temporialy
        [3] : Start/Stop Docker Services Permanently
        [4] : Launch Containers
        [5] : Start/Stop a container
        [6] : List all running containers
        [7] : List all stopped containers
        [8] : List all Saved Docker Images
        [9] : Remove all stopped containers
        [10] : Remove all running containers
        [11] : Remove images
        [12] : To see the details of an container 
        [13] : Return to main menu
        [14] : Exit
        """)
        os.system("tput sgr 0")
        opt_3 = int(input("Enter your choice :- "))
        if opt_3 == 1:
            os.system("""
            if rpm -q docker-ce | grep docker
then echo "Docker Package is already installed"
else 
echo "Docker Package is not installed"
echo "Installing Docker......"
echo "Configuring yum for Docker"
cat <<EOF > /etc/yum.repos.d/docker.repo
[docker-repo]
name=Docker Configuration Repository
baseurl=https://download.docker.com/linux/centos/7/x86_64/stable/
gpgcheck=0
EOF
yum install -y docker-ce --nobest > /dev/null
fi
            """)
            accessories.wait()
        elif opt_3 == 2:
            print("""
            [1] : Start
            [2] : Stop
            [3] : Back
            """)
            opt_3_2 = int(input("Enter your choice :- "))
            if opt_3_2 == 1:
                os.system("systemctl start docker --now")
                print("Docker services started successfully")
                accessories.wait()
            elif opt_3_2 == 2:
                os.system("systemctl stop docker")
                print("Docker services stopped successfully")
                accessories.wait()
            elif opt_3_2 == 3:
                continue
        elif opt_3 == 3:
            print("""
            [1] : Start
            [2] : Stop
            [3] : Back
            """)
            opt_3_3 = int(input("Enter your choice :- "))
            if opt_3_3 == 1:
                os.system("systemctl enable docker")
                print("Docker services started permanently means docker services will automatically start when system boots")
                accessories.wait()
            elif opt_3_3 == 2:
                os.system("systemctl stop docker")
                print("Docker services are disabled and will not start on boot and have to start everytime when system boots")
                accessories.wait()
            elif opt_3_3 == 3:
                continue
        elif opt_3 == 4:
            print("""
            [1] : Launch container in background
            [2] : Launch container with mapped port and attached volume
            [3] : Get the terminal of a running container
            [4] : Run commands inside the docker container
            [5] : Back
            """)
            opt_3_4 = int(input("Enter your choice :- "))
            if opt_3_4 == 1:
                cont_name = input("Enter the name for the container :- ")
                image = input("Enter the name of the docker image with tag (or for latest just give image name):- ")
                os.system("docker run -dit --name {0} {1}".format(cont_name,image))
                print("container is running in background")
                accessories.wait()
            elif opt_3_4 == 2:
                cont_name = input("Enter the name for the container :- ")
                image = input("Enter the name of the docker image with tag (or for latest just give image name):- ")
                cont_port = input("Enter the port number of the container to be mapped :- ")
                port = input("Enter the free port number used to access the container :- ")
                vol = input("Enter the directory name with path to be mounted with the container :- ")
                cont_vol = input("Enter the directory name with path in the container which is to be mounted :- ")
                os.system("docker run -dit -p {2}:{3} -v {4}:{5} --name {0} {1}".format(cont_name,image,port,cont_port,vol,cont_vol))
                print("container is running in background")
                accessories.wait()
            elif opt_3_4 == 3:
                cont_name = input("Enter the container's name or id :- ")
                os.system("docker exec -it {} /bin/bash".format(cont_name))
            elif opt_3_4 == 4:
                cont_name = input("Enter the container's name or id :- ")
                cmd = input("Enter the command :- ")
                os.system("docker exec -it {0} /bin/bash -c {1}".format(cont_name,cmd))
            elif opt_3_4 == 5:
                continue
            else:
                print("Invalid choice!!!")
                accessories.wait()
        elif opt_3 == 5:
            print("""
            [1] : Start
            [2] : Stop
            [3] : Back
            """)
            opt_3_5 = int(input("Enter your choice :- "))
            if opt_3_5 == 1:
                cont_name = input("Enter the container's name or id :- ")
                os.system("docker start {}".format(cont_name))
                accessories.wait()
            elif opt_3_5 == 2:
                cont_name = input("Enter the container's name or id :- ")
                os.system("docker stop {}".format(cont_name))
                accessories.wait()
            elif opt_3_5 == 3:
                continue
        elif opt_3 == 6:
            os.system("docker ps")
            accessories.wait()
        elif opt_3 == 7:
            os.system("docker ps -a")
            accessories.wait()
        elif opt_3 == 8:
            os.system("docker images -a")
            accessories.wait()
        elif opt_3 == 9:
            os.system("docker rm -f $(docker ps -aq)")
            print("All Stopped containers has been removed")
            accessories.wait()
        elif opt_3 == 10:
            os.system("docker rm -f $(docker ps -q)")
            print("All Running containers has been removed")
            accessories.wait()
        elif opt_3 == 11:
            print("""
            [1] : Remove an image
            [2] : Remove all images
            [3] : Back
            """)
            opt_3_11 = int(input("Enter your choice :- "))
            if opt_3_11 == 1:
                image_name = input("Enter the image name or id :- ")
                os.system("docker rmi -f {}".format(image_name))
                accessories.wait()
            elif opt_3_11 == 1:
                os.system("docker rmi $(docker images -aq)")
                accessories.wait()
            elif opt_3_11 == 3:
                continue
        elif opt_3 == 12:
            cont_name = input("Enter the container's name or id :- ")
            os.system("docker inspect {}".format(cont_name))
            accessories.wait()
        elif int(opt_3) == 13:
            break
        elif int(opt_3) == 14:
            exit()
        else:
            print("Invalid choice!!!")
            accessories.wait()

def webserver():
    while True:
        os.system("clear")
        accessories.figlet("HTTPD   WebServer","Banner3-D",6)
        os.system("tput bold")
        os.system("tput setaf 2")
        print("""
	Select from the options below\n
        [1] : Install HTTPD Webserver
        [2] : Start/Stop HTTPD services
        [3] : Start/Stop HTTPD services permanently
        [4] : Create a webpage
        [5] : Return to main menu
        [6] : Exit
        """)
        os.system("tput sgr 0")
        opt_5 = int(input("Enter your choice :- "))
        if opt_5 == 1:
            os.system("""
            if rpm -q httpd | grep httpd
then echo "HTTPD WebServer Package is already installed"
else 
echo "Installing Apache HTTPD Webserver....."
yum install httpd -y > /dev/null
echo "HTTPD successfully Installed"
fi
            """)
            accessories.wait()
        elif opt_5 == 2:
            print("""
            [1] : Start
            [2] : Stop
            [3] : Back
            """)
            opt_5_2 = int(input("Enter your choice :- "))
            if opt_5_2 == 1:
                os.system("systemctl start httpd")
                print("HTTPD services started successfully")
                accessories.wait()
            elif opt_5_2 == 2:
                os.system("systemctl stop httpd")
                print("HTTPD services stopped successfully")
                accessories.wait()
            elif opt_5_2 == 3:
                continue
        elif opt_5 == 3:
            print("""
            [1] : Start
            [2] : Stop
            [3] : Back
            """)
            opt_5_3 = int(input("Enter your choice :- "))
            if opt_5_3 == 1:
                os.system("systemctl enable httpd")
                print("HTTPD services started permanently and no need to restart on every boot")
                accessories.wait()
            elif opt_5_3 == 2:
                os.system("systemctl disable httpd")
                print("HTTPD services has disabled and need to be restart on every boot")
                accessories.wait()
            elif opt_5_3 == 3:
                continue
        elif opt_5 == 4:
            opt_5_4 = input("Want to copy the webpage or create a new one[y/n] :- ")
            if opt_5_4 == 'y':
                page = input("Enter the webpage name with full path :- ")
                os.system("cp -rf {} /var/www/html".format(page))
                print("WebPage copied successfully")
                accessories.wait()
            elif opt_5_4 == 'n':
                page = input("Enter the webpage name(with .html extension) :- ")
                print(repr("Note : To give newline in the text use \n between the text and for tab use \t"))
                data = input("Enter the text ih HTML :- ")
                os.system("printf '{1}' >> /var/www/html/{0}".format(page,data))
                print("webpage created !!")
                accessories.wait()
        elif opt_5 == 5:
            break
        elif opt_5 == 6:
            exit()
        else:
            print("Invalid choice!!!")
            accessories.wait()

def partitions():
    while True:
        os.system("clear")
        accessories.figlet("LVM","Roman",4)
        os.system("tput bold")
        os.system("tput setaf 2")
        print("""
        Select from the options below\n
        [1] : Create Physical Volume
        [2] : Create Volume Group
        [3] : Create Logical Partition
        [4] : Format partitions
        [5] : Extend Partition Size
        [6] : Reduce Partition Size
        [7] : Extend Volume Group Size
        [8] : Return to main menu
        [9] : Exit
        """)
        os.system("tput sgr 0")
        opt_6 = int(input("Enter your choice :- "))
        if opt_6 == 1:
            n = input("Enter the number which you want to create Physical Volume: ")
            for i in range(int(n)):
                n1 = input("Enter {} disk name: ".format(i))
                os.system("pvcreate {}".format(n1))
                os.system("pvdisplay {}".format(n1))
        elif opt_6 == 2:
            c = input("Enter the name of Volume group: ")
            os.system("vgcreate {0} {1}".format(c,n1))
            os.system("vgdisplay {0}".format(c))
        elif opt_6 == 3:
            s = input("Enter the size of LV: ")
            n2 = input("Enter the name of LV: ")
            vg = input("Enter name of volume group: ")
            os.system("lvcreate --size {0}G --name {1} {2}".format(s,n2,vg))
            os.system("lvdisplay {0}".format(n2))
        elif opt_6 == 4:
            print("""
            Select format type
            [1] : mkfs.ext4
            [2] : resize2fs
            [3] : Back
            """)
            fmt_ch = input("Enter your choice: ")
            if int(fmt_ch) == 1:
                vg = input("Enter name of volume group: ")
                lv = input("Enter name of logical VOlume: ")
                os.system("mkfs.ext4 /dev/{0}/{1}".format(vg,lv))
            elif int(fmt_ch) == 2:
                vg1 = input("Enter name of volume group: ")
                lv1 = input("Enter name of logical VOlume: ")
                os.system("resize2fs /dev/{0}/{1}".format(vg1,lv1))
                os.system("df -H")
            elif int(fmt_ch) == 3:
                continue
        elif opt_6 == 5:
            e=input("Please enter the Volume Group Name :- ")
            g=input("Please enter your Paraition Name (for example sdd2) :- ")
            l=int(input("Enter how much size you want to increase: "))
            os.system("lvextend --size +{}G /dev/{}/{}".format(l,e,g))
            os.system("resize2fs /dev/{}/{}".format(e,g))
            accessories.wait()
        elif opt_6 == 6:
            e=input("Please enter the Volume Group Name :- ")
            g=input("Please enter your Paraition Name(for example sdd2): ")
            l=int(input("Enter how much size you want to reduce: "))
            os.system("lvreduce -r -L --size +{}G /dev/{}/{}".format(l,e,g))
            accessories.wait()
        elif opt_6 == 7:
            y=input("Enter the Partition Name you want to increase: ")
            os.system("vgextend {} /dev/{}".format(e,y))
            accessories.wait()
        elif opt_6 == 8:
            break
        elif opt_6 == 9:
            exit() 
        else:
            print("Invalid choice!!!")

def aws_menu():
    while True:
        os.system("clear")
        accessories.figlet("AWS Menu","starwars",3)
        os.system("tput bold")
        os.system("tput setaf 2")
        print("""
        Which service you want to use ?\n
        [1] : Install AWS CLI 
        [2] : Configure AWS CLI with your AWS account
        [3] : EC2
        [4] : EBS
        [5] : S3
        [6] : Return to Main Menu
        [7] : Exit
        """)
        os.system("tput sgr 0")
        opt_4 = int(input("Enter your choice : "))
        if opt_4 == 1:
            os.system("""
            if ls /usr/local | grep aws-cli > /dev/null
            then echo 'AWS CLI is already installed'
            else
            echo 'Installing AWS CLI......'
            curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" > /dev/null
            unzip awscliv2.zip > /dev/null
            sudo ./aws/install > /dev/null
            if aws --version | grep aws
            then echo 'AWS CLI is successfully installed'
            else echo 'Could not able to install AWS CLI'
            fi 
            fi
            """)
            accessories.wait()
        elif opt_4 == 2:
            print("Note : To configure AWS CLI you need to have an IAM user created in your AWS account")
            opt_4_1 = input("Enter your IAM user profile name :- ")
            print("Enter your IAM user credentials and details below")
            os.system("aws configure")
            print("AWS CLI configured to use for {} user".format(opt_4_1))
            accessories.wait()
        elif opt_4 == 3:
            aws.ec2()
        elif opt_4 == 4:
            aws.ebs()
        elif opt_4 == 5:
            aws.s3()
        elif opt_4 == 6:
            break
        elif opt_4 == 7:
            exit()
        else:
            print("Invalid choice!!!")
            accessories.wait()            

while True:

    os.system("clear")
    accessories.figlet("Multi  Menu  Program","3d",3)
    os.system("tput setaf 2")
    os.system("tput bold")

    print("""
    select from the options below\n
    Press 1 : To Run Some Basic linux commands (RHEL 8)
    Press 2 : To setup Hadoop Cluster
    Press 3 : For using Docker
    Press 4 : To use some AWS services
    Press 5 : To configure WebServer
    Press 6 : Create Partitions 
    Press 7 : Exit
	""")

    ch = input("\tEnter your choice :-  ")
    os.system("tput sgr 0")
    if int(ch) == 1:
        linux()
    elif int(ch) == 2:
        hadoop()
    elif int(ch) == 3:
        docker()
    elif int(ch) == 4:
        aws_menu()
    elif int(ch) == 5:
        webserver()
    elif int(ch) == 6:
        partitions()
    elif int(ch) == 7:
        exit()
    else:
        print("Invalid Choice !!!")
        accessories.wait()
