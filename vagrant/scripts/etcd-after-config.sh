    sudo systemctl stop etcd
    sudo systemctl disable etcd
    sudo systemctl daemon-reload
    sudo systemctl enable etcd
    sudo systemctl start etcd
    sudo systemctl status etcd