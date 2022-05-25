import os
nn_ip = input("Enter the IP of the Hadoop master :- ")
os.system("bash ~/arth-team-task1/hadoop")
nn_dir = input("Enter the directory name for hadoop master :-  ")
os.system("mkdir -p /{}".format(nn_dir))
fin = open("/root/master/hdfs-site.xml", "rt")
fout = open("/etc/hadoop/hdfs-site.xml", "wt")
for line in fin:
    fout.write(line.replace('path', '{}'.format(nn_dir)))
fin.close()
fout.close()
fin = open("/root/master/core-site.xml", "rt")
fout = open("/etc/hadoop/core-site.xml", "wt")
for line in fin:
    fout.write(line.replace('ip', '{}'.format(nn_ip)))
fin.close()
fout.close()
print("Formatting the directory of the name node......")
os.system("hadoop namenode -format")
print("Starting the NameNode.....")
os.system("hadoop-daemon.sh start namenode")
os.system("""
if jps | grep NameNode
then echo "Hadoop master(NameNode) Setup Successfully"
else "Not able to setup NameNode !!!"
fi
""")
