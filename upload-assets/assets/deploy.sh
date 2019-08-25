#!/bin/bash
cd /root/
git clone https://github.com/mengmengtech/katacoda-scenarios.git
pip3 install matplotlib
pip3 install sklearn
mkdir /root/ai
# mkdir /root/ai/ml1-1
# mkdir /root/ai/ml1-1/c1
# mkdir /root/ai/ml1-1/c2
# mkdir /root/ai/ml1-1/c3

# touch hello-world

docker pull jupyter/datascience-notebook
docker run -itd -p 80:8888 -v /root/ai:/root/ai --name="mmjupyter" jupyter/datascience-notebook bash
docker exec -it mmjupyter bash
jupyter notebook &
