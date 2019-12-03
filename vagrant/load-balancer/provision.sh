sudo apt show haproxy
sudo add-apt-repository -y ppa:vbernat/haproxy-1.7
sudo apt update
sudo apt install -y haproxy
haproxy -v