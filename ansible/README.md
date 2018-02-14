# Ansible roles

## Docker ansible role

This role make sure that docker is installed on linux Ubuntu server and configure logging into syslog

Running this role on you local host run this command:
```bash
ansible-playbook -i "localhost," -c local docker.yml -K
```


## Rsyslog ansible role

This role make sure that rsyslog is installed and configured for these scenario:
- default configuration and loging
- custom loging to custom files
- sending logs to remote rsyslog server

When you run this default command:
```bash
ansible$ ansible-playbook -i "localhost," -c local rsyslog.yml -K
```
Ansible will configure default loging in /var/log/*


By default custom logs and sending logs to remote rsyslog servers are disabled.
To enable this function you need to define these variables in command line when you running ansible-playbook as you can see below.
```bash
ansible-playbook -i "localhost," -c local rsyslog.yml -K -e "custom_logs=true"
```
or
```bash
ansible-playbook -i "localhost," -c local rsyslog.yml -K -e "remote_logs=true"
```
or for both to be enabled
```bash
ansible-playbook -i "localhost," -c local rsyslog.yml -K -e "custom_logs=true" -e "remote_logs=true"
```


### configure custom logs
When you want to configure custom logs you need to edit rsyslog/vars/main.yml and define these variables:
```yaml
rsyslog_custom_files:
  "path+name_of_log_file":
    facility: ""
    priority: ""
  "path+name_of_log_file2":
    facility: ""
    priority: ""
  .
  .
  .
```
example of correct defined custom logs variables
```yaml
rsyslog_custom_files:
  "/var/log/custom.log":
    facility: "local7"
    priority: "*"
  "/var/log/custom2.log":
    facility: "mail"
    priority: "*"
```

### configure sending logs to remote rsyslog server
When you want to configure sending logs to remote servers you need to edit rsyslog/vars/main.yml and define these variables:
```yaml
rsyslog_remote_facilitie: ""
rsyslog_remote_priorities: ""
rsyslog_remote_server: ""
rsyslog_remote_server_port: ""
```
example
```yaml
rsyslog_remote_facilitie: "*"
rsyslog_remote_priorities: "*"
rsyslog_remote_server: "10.10.10.10"
rsyslog_remote_server_port: "513"
```
