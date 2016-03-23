#!/usr/bin/expect -f
 set timeout 20
 set host [lindex $argv 0]
 set username "localadmin"
 set password "p@ssw0rd"

set dir ~/logs

log_file -a $dir/session_$host.log

send_log "### /Start-ssh/ Host: $host @ [exec date] ###\r"
spawn ssh -o "StrictHostKeyChecking no" $username@$host

expect "*assword: "
send "$password\r"

expect "*#"

send "edit\r"
expect "*(working)#"

send "system hostname $host.rave.apple.com\r"

expect "*(working)#"
send "activate\r"
expect "*#"
send "exit\r"

send_log "### End rename Host: $host @ [exec date] ###\r"
exit
