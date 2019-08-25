#!/bin/bash
/home/jovyan
cd /opt/
mkdir /opt/ai
cd /opt/ai
git clone https://github.com/mengmengtech/katacoda-scenarios.git
git clone https://github.com/jakevdp/PythonDataScienceHandbook.git
git clone https://github.com/jakevdp/sklearn_tutorial.git
pip3 install matplotlib
pip3 install sklearn

docker pull jupyter/datascience-notebook
docker run -itd -p 80:8888 -v /home/jovyan/work:/opt/ai --name="mmjupyter" jupyter/datascience-notebook bash
docker exec -it mmjupyter bash
jupyter notebook &
