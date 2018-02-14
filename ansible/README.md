# Ansible roles

## Docker ansible role

This role make sure that docker is installed on linux Ubuntu server and configure logging into syslog

Running this role on you local host run this command:
```
ansible-playbook -i "localhost," -c local docker.yml -K
```


## Rsyslog ansible role

This role make sure that rsyslog is installed and configured for these scenario:
- default configuration and loging
- custom loging to custom files
- sending logs to remote rsyslog server
