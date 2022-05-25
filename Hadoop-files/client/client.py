import os
nn_ip = input("Enter the Hadoop NameNode IP :- ")
fin = open("/root/client/core-site.xml", "rt")
fout = open("/etc/hadoop/core-site.xml", "wt")
for line in fin:
    fout.write(line.replace('ip', '{}'.format(nn_ip)))
fin.close()
fout.close()
os.system("hadoop-daemon.sh start datanode")
print("Hadoop Client Configured Successfuly")
