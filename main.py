#
# import sshtunnel
# import argparse
# import datetime
# def getArgs():
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-s' , '--sip' , dest = 'source_ip' , nargs='+',  help="add source ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")
#     parser.add_argument('-sp' , '--sport' , dest = 'source_port' , nargs='+' , help='add source port you want allow on ufw like this 3306 3389 22')

#     parser.add_argument('-d' , '--dip' , dest = 'destination_ip' , nargs='+' , help="add destination ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")

#     parser.add_argument('-dp' , '--dport' , dest = 'destination_port' , nargs='+' , help='add destination port you want allow on ufw like this 3306 3389 22')
#     return parser.parse_args()
#
# class InitArgs:
#     def __init__(self):
#         pass
#
#     def getArgs(self):
#         parser = argparse.ArgumentParser()
#         parser.add_argument('-s', '--sip', dest='source_ip', nargs='+',
#                             help="add source ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")
#         parser.add_argument('-sp', '--sport', dest='source_port', nargs='+',
#                             help='add source port you want allow on ufw like this 3306 3389 22')
#         parser.add_argument('-d', '--dip', dest='destination_ip', nargs='+',
#                             help="add destination ip address you want allow on ufw like this 192.168.1.1 192.168.2.2 192.168.3.3 and you can add 0.0.0.0 for any")
#         parser.add_argument('-dp', '--dport', dest='destination_port', nargs='+',
#                             help='add destination port you want allow on ufw like this 3306 3389 22')
#         return parser.parse_args()
#
# # ssh -N -L 0.0.0.0:3306:192.168.43.6:3306 root@homsa-db-pr
# a = datetime.datetime.now()
# print(int(a.timestamp()))
#
# p1 = InitArgs()
# farhad = p1.getArgs()

# print(farhad.source_ip)
import argparse
import sys

import paramiko
def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o' , '--oc' , dest = 'optimize_clear' , action="store_true",  help="php artisan optimize:clear")
    parser.add_argument('-r' , '--rr' , dest = 'rooms_reindex' , action="store_true" , help='php artisan rooms:reindex')
    parser.add_argument('-s' , '--sra' , dest = 'supervisor_restart' , action="store_true" , help='supervisorctl restart all')
    parser.add_argument('-m' , '--mode' , dest = 'mode' , nargs="?" , required=True, choices = ["dev","prod"], help="choose which server you want to run command")
    parser.add_argument('-t' , '--table' , dest = 'table' , action="store_true" , help='which server you want to run dump')
    parser.add_argument('-f' , '--full' , dest = 'full' , action="store_true" , help='full dump from database base on your choose dev/prod')
    parser.add_argument('-e' , '--env' , dest = 'env' , action="store_true" , help='show env base on your choose dev/prod')
    return parser.parse_args()

args = getArgs()
prod_base_path = "/var/www/homsa/"
dev_base_path = "/var/www/homsa-new/homsa/"
dev_base_user = "root"
prod_base_user = "webapp"


def create_connection(mode):
    if mode == "dev":
        print(mode)
        ssh = paramiko.SSHClient()
        private_key = paramiko.RSAKey.from_private_key_file("/home/f.salehi/.ssh/id_rsa")
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="homsa-dev" , username="root" , pkey=private_key)
    else:
        ssh = paramiko.SSHClient()
        private_key = paramiko.RSAKey.from_private_key_file("/home/f.salehi/.ssh/id_rsa")
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname="homsa-pr" , username="root" , pkey=private_key)
    return ssh
# ssh_stdin , ssh_stdout , ssh_stderr = (ssh.exec_command(f"php {dev_base_path}artisan o:c"))
# print(ssh_stdout.read().decode())
# try:
#     print(ssh_stdin.read().decode())
# except:
#     pass
# err = ssh_stderr.read().decode()
# if err:
#
#     print("mamad")

def run_command(mode , oc , rr):
    ssh = create_connection(mode)
    if mode == "dev":
        if oc:
            _, ssh_stdout, ssh_stderr = (ssh.exec_command(f"php {dev_base_path}artisan o:c"))
            if ssh_stdout:
                print(ssh_stdout.read().decode())
            else:
                print(ssh_stderr.read().decode())
        if rr:
            _, ssh_stdout, ssh_stderr = (ssh.exec_command(f"php {dev_base_path}artisan rooms:reindex"))
            if ssh_stdout:
                print(ssh_stdout.read().decode())
            else:
                print(ssh_stderr.read().decode())

    elif mode == "prod":
        if oc:
            _, ssh_stdout, ssh_stderr = (ssh.exec_command(f"php {prod_base_path}artisan o:c"))
            if ssh_stdout:
                print(ssh_stdout.read().decode())
            else:
                print(ssh_stderr.read().decode())
        if rr:
            _, ssh_stdout, ssh_stderr = (ssh.exec_command(f"php {prod_base_path}artisan rooms:reindex"))
            if ssh_stdout:
                print(ssh_stdout.read().decode())
            else:
                print(ssh_stderr.read().decode())
    else:
        sys.exit("please run wiht -h flag and read help")
        # sys.exit("0")
        # _, ssh_stdout, ssh_stderr = (ssh.exec_command(f"php {prod_base_path}artisan o:c"))
        # if ssh_stdout:
        #     print(ssh_stdout.read().decode())
        # else:
        #     print(ssh_stderr.read().decode())

run_command(args.mode , args.optimize_clear , args.rooms_reindex)


# def execute_command(args):
#     pass
# def get_command(args):
#     if args.mode == "dev":
#         def dev():
#             pass
#         dev()
#     else:
#         def prod():
#             print (args.mode)
#         prod()
#
# get_command(args)
