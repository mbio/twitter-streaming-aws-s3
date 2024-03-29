#!/bin/bash

echo '===================================='
echo 'System update and upgrade'
echo '===================================='

sudo apt-get update
sudo apt-get -y upgrade

echo '===================================='
echo 'Installing Python3...'
echo '===================================='

sudo apt-get -y install python3 python3-pip
pip3 install --no-cache-dir -r /vagrant/requirements.txt

ALIAS=$(cat <<EOF
alias python=python3
alias pip=pip3
EOF
)
echo "${ALIAS}" >> ~/.bashrc
source ~/.bashrc

echo '===================================='
echo 'Setup complete!'
echo '===================================='
