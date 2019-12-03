# How to set up Kubernetes Cluster
## Prerequisites
1. [Virtualbox](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](https://www.vagrantup.com/downloads.html)

## Infrastructure setup on each machine
1. cd to each directory [load-balancer, master1, master2]
2. Run `vagrant up` to start VM (you config VM in Vagrantfile)
3. In first time, vagrant will run provision script(to install all packages) automatically. If not run `vagrant reload --provision`
4. SSH to vm via `vagrant ssh`

## Loadbalancer setup
1. Verify HAproxy
2. Copy [haproxy.cfg](https://github.com/warinthornmild/sds-project/blob/master/service-loadbalancing/haproxy.cfg) to `/etc/haproxy`
3. Reload HAproxy by running `sudo systemctl restart haproxy`
4. you can verfify the HAproxy by running `nc -v IP_LOADBALANCER:PORT`

## Master1 Setup
We use stacked control pane and etcd nodes
1. Verify `kubeadm, kubectl, kubelet` and `docker`
2. Initilize kubernetes cluster by following command
```
sudo kubeadm init --control-plane-endpoint "192.168.99.200:6443" --upload-certs --pod-network-cidr=10.224.0.0/16 -apiserver-advertise-address=192.168.99.201
```
3. save joining commands.

## Master2 Setup
1. Verify `kubeadm, kubectl, kubelet` and `docker`
2. Join master2 to cluster by joining command from master1. for example 
```
    kubeadm join 192.168.99.200:6443 --token <tokenn> \
    --discovery-token-ca-cert-hash <sha256-token-hash> \
    --control-plane --certificate-key <certificate-key >
```
3. verify node by running `kubectl get nodes`

## Install network cni plugin 
After all nodes have already joined the cluster. we will install the `flannel` as network cni plugin 
```
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```

### Troubleshooting 
Don't forget to run this command on all nodes
```
sudo sysctl net.bridge.bridge-nf-call-iptables=1
```
In case of /run/flannel/subnet.env in missing. put these code on it
```
FLANNEL_NETWORK=10.244.0.0/16
FLANNEL_SUBNET=10.244.0.1/24
FLANNEL_MTU=1450
FLANNEL_IPMASQ=true
```