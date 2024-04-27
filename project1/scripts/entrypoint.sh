#!/bin/sh
iptables-restore < /etc/iptables/iptables
conntrackd -d
sh
