from os import system as s

# Verifiy Monit monitors and restarts SSH
s(echo "Testing SSH..."; systemctl stop sshd; monit; sleep 5; monit summary | grep SSH; sleep 120; monit summary | grep SSH)

# Verifiy Monit monitors and restarts NFS
s(echo "Testing NFS..."; systemctl stop nfslock nfs; monit; sleep 5; monit summary | grep NFS; sleep 35; monit summary | grep NFS)

# Verifiy Monit monitors and restarts LDAP
s(echo "Testing LDAP..."; systemctl stop slapd; monit; sleep 5; monit summary | grep LDAP; sleep 35; monit summary | grep LDAP)

# Verifiy Monit monitors and restarts RSYSLOG
s(echo "Testing RSYSLOG..."; systemctl stop rsyslog; monit; sleep 5; monit summary | grep RSYSLOG; sleep 35; monit summary | grep RSYSLOG)

# Verifiy Monit monitors Memory usages
s(echo "Testing System CPU Monitoring..."; monit; sleep 5; monit summary | grep Group-2-CIT470-NKU-EDU; stress --vm  1 --vm-bytes 3500M --timeout 45s; monit summary | grep Group-2-CIT470-NKU-EDU)

# Verifiy Monit monitors CPU usages
s(echo "Testing System CPU Monitoring..."; monit; monit summary | grep Group-2-CIT470-NKU-EDU; stress --vm-bytes 256M --cpu 100 --timeout 40s; monit summary | grep Group-2-CIT470-NKU-EDU)

# Verifiy Monit monitors Disk Space usages
s(echo "Testing Monit Disk Monitoring..."; monit summary | grep -e HOME -e ROOT -e VAR; echo "Filling /HOME..."; dd if=/dev/zero of=/home/zero bs=51200 count=1000000; echo "Filling /VAR..."; dd if=/dev/zero of=/var/zero bs=51200 count=1000000; echo "Filling /..."; dd if=/dev/zero of=/zero bs=51200 count=1000000; echo "Waiting for Monit Cycles"; sleep 90; monit summary | grep -e HOME -e ROOT -e VAR;  echo "Cleaning up disk test..."; rm -f /home/zero; rm -f /var/zero; rm -f /zero)
