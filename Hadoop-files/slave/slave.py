import os
nn_ip = input("Enter the Hadoop NameNode IP :- ")
dn_dir = input("Enter the directory name for the slave :-  ")
os.system("mkdir -p /{}".format(dn_dir))
fin = open("/root/slave/hdfs-site.xml", "rt")
fout = open("/etc/hadoop/hdfs-site.xml", "wt")
for line in fin:
    fout.write(line.replace('path', '{}'.format(dn_dir)))
fin.close()
fout.close()
fin = open("/root/slave/core-site.xml", "rt")
fout = open("/etc/hadoop/core-site.xml", "wt")
for line in fin:
    fout.write(line.replace('ip', '{}'.format(nn_ip)))
fin.close()
fout.close()
os.system("hadoop-daemon.sh start datanode")
print("Datanode Configured Successfuly")
