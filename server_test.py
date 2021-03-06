from os import system as s

# Verifiy Monit monitors and restarts SSH
s('echo ""; echo "Testing SSH..."; systemctl stop sshd; monit; sleep 5; monit summary | grep SSH; sleep 120; monit summary | grep SSH')

# Verifiy Monit monitors and restarts NFS
s('echo ""; echo "Testing NFS..."; systemctl stop nfslock nfs; monit; sleep 5; monit summary | grep NFS; sleep 35; monit summary | grep NFS')

# Verifiy Monit monitors and restarts LDAP
s('echo ""; echo "Testing LDAP..."; systemctl stop slapd; monit; sleep 5; monit summary | grep LDAP; sleep 35; monit summary | grep LDAP')

# Verifiy Monit monitors and restarts RSYSLOG
s('echo ""; echo "Testing RSYSLOG..."; systemctl stop rsyslog; monit; sleep 5; monit summary | grep RSYSLOG; sleep 35; monit summary | grep RSYSLOG')

# Verifiy Monit monitors and restarts RSYSLOG
s('echo ""; echo "Testing SENDMAIL..."; systemctl stop sendmail; monit; sleep 5; monit summary | grep SENDMAIL; sleep 35; monit summary | grep SENDMAIL')

# Verifiy Monit monitors Memory usages
s('echo ""; echo "Testing System Memory Monitoring..."; monit; sleep 5; monit summary | grep Group-2-CIT470-NKU-EDU; stress --vm  1 --vm-bytes 3500M --timeout 45s; monit summary | grep Group-2-CIT470-NKU-EDU')

# Verifiy Monit monitors CPU usages
s('echo ""; echo "Testing System CPU Monitoring..."; monit; sleep 5; monit summary | grep Group-2-CIT470-NKU-EDU; stress --vm-bytes 512M --cpu 100 --timeout 90s; monit summary | grep Group-2-CIT470-NKU-EDU')

# Verifiy Monit monitors Disk Space usages
s('echo ""; echo "Testing Monit Disk Monitoring..."; monit summary | grep -e HOME -e ROOT -e VAR; echo ""; echo "Filling /HOME..."; dd if=/dev/zero of=/home/zero bs=51200 count=1000000; echo ""; echo "Filling /VAR..."; dd if=/dev/zero of=/var/zero bs=51200 count=1000000; echo ""; echo "Filling /..."; dd if=/dev/zero of=/zero bs=51200 count=1000000; echo ""; echo "Waiting for Monit Cycles"; sleep 90; monit summary | grep -e HOME -e ROOT -e VAR;  echo ""; echo "Cleaning up disk test..."; rm -f /home/zero; rm -f /var/zero; rm -f /zero')

