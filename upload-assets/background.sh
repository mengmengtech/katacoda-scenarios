#!/bin/bash
mkdir /root/ai
mkdir /root/ai/ml1-1

mkdir /root/ai/ml1-1/c1
mkdir /root/ai/ml1-1/c2
mkdir /root/ai/ml1-1/c3
sudo grep -i "done" /opt/katacoda-background-finished &> /dev/null
if [[ "$?" -eq 0 ]]; then
exit
fi

while true; do sudo grep -i "done" /opt/katacoda-finished > /dev/null && break || sleep 2; done

echo "Everything ready... Finalise the deployment"

/opt/deploy.sh

echo "done" | sudo tee /root/katacoda-background-finished