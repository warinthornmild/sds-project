# sds-project  Kubetenes cluster with RaspberryPi

## Topology

| hostname  |  IP address | port |  
| --- | --- | --- |
| router | 192.168.99.1 |  - |  
| LB1-control | 192.168.99.200 | 6443 |  
| master01 | 192.168.99.201 | 6443 |
| master02 | 192.168.99.202 | 6443 |
| node1 | 192.168.99.101 | - |
| node2 | 192.168.99.102 | - |
| node3 | 192.168.99.103 | - |
| node4 | 192.168.99.104 | - |
| LB2-gateway | 192.168.99.10 | * |
| front-end | - | 30001 |
| product | - | 30002 | 
| order | - | 30002 | 
| user | - | 30004 |
