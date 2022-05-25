import os
import accessories

def ec2():
        while True:
            os.system("clear")
            print("""
            [1] : Create New EC2 Instance
            [2] : Start Specific Instance
            [3] : Stop Instance
            [4] : Terminate Instance
            [5] : Show all instances
            [6] : Security Groups
            [7] : Back
            """)
            ec2_ch = input("Enter your choice :- ")
            if int(ec2_ch) == 1:
                ami = input("Enter AMI id to Launch Instance: ")
                instance_type = input("Enter Instance type: ")
                count = input("Enter Number of Instances to launch: ")
                subnet_id = input("Enter Subnet id: ")
                sg_id1 = input("Enter Security Group Id to attach to the Instance: ")
                key = input("Enter Key to attach to ec2 Instance: ")
                print("Launching New EC2 Instance.....")
                os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id {} --security-group-ids {} --key-name {}'.format(ami , instance_type , count ,subnet_id, sg_id1 , key))
                print("Instance launched Successfully......")
                accessories.wait()
            elif int(ec2_ch) == 3:
                id = input("Enter Instance id to stop Ec2 instances: ")
                print("Stopping Instance.......")
                os.system("aws ec2 stop-instances --instance-ids {}".format(id))
                print("Insatnce stopped Successfully....")
                accessories.wait()
            elif int(ec2_ch) == 2:
                id = input("Enter Instance id to start Ec2 instances: ")
                print("Starting Instance.....")
                os.system("aws ec2 start-instances --instance-ids {}".format(id))
                print("Instance Started successfully......")
                accessories.wait()
            elif int(ec2_ch) == 4:
                id = input("Enter Instance id to terminate Ec2 instances: ")
                print("Terminating instance...")
                os.system("aws ec2 terminate-instances --instance-ids {}".format(id))
                print("Instance terminated successfully.....")
                accessories.wait()
            elif int(ec2_ch) == 5:
                print("Showing Instances....")
                os.system("aws ec2 describe-instances")
                accessories.wait()
            elif int(ec2_ch) == 6:
                print("""
                [1] : Create new security group
                [2] : Delete Security group
                [3] : Add Ingress Rules
                [4] : Show Security Groups
                [5] : Back
                """)
                sg_ch1 = input("Enter your choice: ")
                if int(sg_ch1) == 1:
                    sg_name = input("Enter Security group Name: ")
                    sg_des = input("Enter Security group description: ")
                    print("Creating New Security group....")
                    os.system("aws ec2 create-security-group --group-name {0} --description {1}".format(sg_name,sg_des))
                    print("Successfully created security group....")
                    accessories.wait()
                elif int(sg_ch1) == 2:
                    sg_id=input("Enter Security group id you want to delete:  ")
                    print("Deleting Security group...")
                    os.system("aws ec2 delete-security-group --group-id {}".format(sg_id))
                    print("Successfully deleted Security group....")
                    accessories.wait()
                elif int(sg_ch1) == 3:
                    sg_id = input("Enter Security Group ID : ")
                    ip_protocol = input("Enter IP Protocol: ")
                    port_no = input("Enter Port No: ")
                    cidr=input("Input Ip Ranges : ")
                    print("Authorizing Security group....")
                    os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(sg_id , ip_protocol , port_no , cidr))
                    print("Sucessfully authorize security group...")
                    accessories.wait()
                elif int(sg_ch1) == 4:
                    sg_id2 = input("Enter group id : ")
                    sg_name1 = input("Enter name of Security Group: ")
                    os.system("aws ec2 describe-security-groups --group-ids {} --group-names {}".format(sg_id2,sg_name1))
                    accessories.wait()
                elif int(sg_ch1) == 5:
                    continue
            elif int(ec2_ch) == 7:
                break

def ebs():
    while True:
        os.system("clear")
        print("""
        [1] : Create new Volume
        [2] : Attach Volume to Specific Instance
        [3] : Dettach Volume
        [4] : Delete Volume
        [5] : Show Volumes
        [6] : Mount and Partition
        [7] : Back
        """)
        vol_ch = input("Enter your Choice: ")
        if int(vol_ch) == 1:
            az = input("Enter Availablity Zone to Create EBS Volume: ")
            ebs_size = input("Enter Size to create EBS Volume: ")
            print("Creating New Volume ....")
            os.system('aws ec2 create-volume --availability-zone {} --size {}'.format(az , ebs_size))
            print("New Volume Created Successfully....")
            accessories.wait()
        elif int(vol_ch) == 2:
                ebs_vid = input("Enter EBS Volume ID to Attach to EC2 Instance: ")
                ec2_id = input("Enter EC2 Instance ID to attach EBS Volume: ")
                print("Attaching Volume to instance.....")
                os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdg'.format(ebs_vid , ec2_id))
                print("Successfully Volume attached to the instance.......")
                accessories.wait() 
        elif int(vol_ch) == 3:
                v_id = input("Enter volume id: ")
                print("Detaching Volume.......")
                os.system("aws ec2 detach-volume --volume-id {}".format(v_id))
                print("Volume Dettached Successfully.....")
                accessories.wait()
        elif int(vol_ch) == 4:
                 v_id = input("Enter volume id: ")
                 print("Deleting Volume....")
                 os.system("aws ec2 delete-volume --volume-id {}".format(v_id))
                 print("Successfully deleted Volume...")
                 accessories.wait()
        elif int(vol_ch) == 5:
                os.system("aws ec2  describe-volumes")
                accessories.wait()
        elif int(vol_ch) == 6:
               ip = input("Enter Public IP of EC2: ")
               ky = input("Enter Private Key Name For Login Into EC2 : ")
               os.system('ssh -l ec2-user {} -i {}.pem sudo fdisk -l'.format(ip , ky))
               na = input("\nEnter Partition Name: ")
               nb = input("Enter directory name: ") 
               os.system("ssh -l ec2-user {} -i {}.pem sudo mkdir {}".format(ip,ky,nb))
               os.system('ssh -l ec2-user {} -i {}.pem sudo mkfs.ext4 {}'.format(ip , ky , na))
               os.system('ssh -l ec2-user {} -i {}.pem sudo mount {}  {}'.format(ip , ky , na,nb))
               os.system('ssh -l ec2-user {} -i {}.pem sudo df -hT'.format(ip , ky))
               accessories.wait()
        elif int(vol_ch) == 7:
                break

def s3():
    while True:
            os.system("clear")
            print("""
            [1] : Create New S3 Bucket
            [2] : Delete S3 bucket
            [3] : Upload object in S3 bucket
            [4] : Delete object in S3 bucket
            [5] : Delete S3 bucket
            [6] : Back
            """)
            bucket_ch = input("Enter your Choice :- ")
            if int(bucket_ch) == 1:
                s3_name = input("Enter S3 bucket name that must be unique: ")
                #region = input("Enter name of region: ")
                print("Creating S3 Bucket.....")
                os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))
                print("S3 bucket created successfully....")
                accessories.wait()
            elif int(bucket_ch) == 2:
                s3_name = input("Enter S3 Bucket name: ")
                print("Deleting S3 bucket...")
                os.system("aws s3api delete-bucket --bucket {} --region ap-south-1".format(s3_name))
                print("Successfully deleted S3 bucket.....")
                accessories.wait()
            elif int(bucket_ch) == 3:
                object_name = input("Enter Object name (with full path) to put inside S3 bucket: ")
                s3_name = input("Enter S3 Bucket name: ")
                print("Uploading object....")
                os.system('aws s3 cp {0} s3://{1} --acl public-read'.format(object_name , s3_name))
                print("Successfully uploaded object in S3 bucket...")
                accessories.wait()
            elif int(bucket_ch) == 4:
                s3_name = input("Enter S3 bucket name: ")
                object_name = input("Enter object name: ")
                print("Deleting object....")
                os.system('aws s3 rm s3://{}/{}'.format(s3_name , object_name))
                print("Successfully deleted object...")
                accessories.wait()
            elif int(bucket_ch) == 5:
                s3_name = input("Enter name of bucket: ")
                region = input("Enter region name: ")
                print("Deleting S3 Bucket....")
                os.system("aws s3api delete-bucket --bucket {} --region {}".format(s3_name,region))
                print("Successfully S3 bucket successfully....")
                accessories.wait()
            elif int(bucket_ch) == 6:
                break
