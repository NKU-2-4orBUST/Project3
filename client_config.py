from os import system as s
import re, argparse
#Creates Command line Argument Parsers
parser=argparse.ArgumentParser(usage='Quickly install or reinstall servers',description='Used to install Monit monitoring server on newly imaged clients  |  Format:  0.0.0.0-->255.255.255.255',add_help=True,allow_abbrev=True)
parser.add_argument('-s','--server', required=True, help='Sets variable for Server IP')
parser.add_argument('-c','--client', required=True, help='Sets variable for Server IP')
args = parser.parse_args()

IP = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def validation():
  if(re.search(IP, args.client) and re.search(IP, args.server)):
        print("IP address validated")
        config()
  else:
        print("Invalid Ip address, Please use the -h to see proper formatting")
      
def config():      
  # Install and Download monit and dependencies as well as configs
  s('yum install -y sendmail epel-release; yum install -y monit; wget https://github.com/NKU-2-4orBUST/Project3/raw/main/monitrc_client https://github.com/NKU-2-4orBUST/Project3/raw/main/rsyslog.conf')
  # Configures Monit and rsyslog
  s('echo "Configuring rsyslog and Monit"; sed "s/IP_SERVER.*/'+args.server+'/g" monitrc_client > monitrc1; sed "s/IP_CLIENT.*/'+args.client+'/g" monitrc_test > /etc/monitrc; sed "s/IP_SERVER.*/'+args.server+':514/g" rsyslog.conf > /etc/rsyslog.conf; systemctl enable monit rsyslog; systemctl start monit rsyslog')
  # Configure Firewall for Monit and rsyslog
  s('echo "Configuring Firewall for rsyslog monitoring"; firewall-cmd --zone=public --add-port=514/tcp -–permanent; firewall-cmd --zone=public --add-port=514/udp -–permanent; firewall-cmd --reload')
  # Removes downloaded files
  s('echo "Cleaning up files"; rm -f monitrc_client monitrc1 rsyslog.conf')
  
validation()
