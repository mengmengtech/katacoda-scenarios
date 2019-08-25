#!/bin/bash
cd /opt/
git clone https://github.com/mengmengtech/katacoda-scenarios.git
git clone https://github.com/jakevdp/PythonDataScienceHandbook.git
git clone https://github.com/jakevdp/sklearn_tutorial.git
pip3 install matplotlib
pip3 install sklearn
mkdir /opt/ai
# mkdir /root/ai/ml1-1
# mkdir /root/ai/ml1-1/c1
# mkdir /root/ai/ml1-1/c2
# mkdir /root/ai/ml1-1/c3

# touch hello-world

docker pull jupyter/datascience-notebook
docker run -itd -p 80:8888 -v /opt/ai:/opt/ai --name="mmjupyter" jupyter/datascience-notebook bash
docker exec -it mmjupyter bash
cd /opt/ai/
jupyter notebook &
