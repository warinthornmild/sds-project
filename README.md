# sds-project  Kubetenes cluster with RaspberryPi

## Topology

| hostname  |  IP address | port |  
| --- | --- | --- |
| router | 192.168.99.1 |  - |  
| LB1-control | 192.168.99.200 | 6443, 80, 30002, 30003, 30004 |  
| master01 | 192.168.99.201 | 6443 |
| master02 | 192.168.99.202 | 6443 |
| node1 | 192.168.99.101 | - |
| node2 | 192.168.99.102 | - |
| node3 | 192.168.99.103 | - |
| node4 | 192.168.99.104 | - |
| front-end | - | 30001 |
| product | - | 30002 | 
| user | - | 30003 |
| order | - | 30004 | 

# Setup cluster guide
[SETUP.md](https://github.com/warinthornmild/sds-project/blob/master/vagrant/SETUP.md)