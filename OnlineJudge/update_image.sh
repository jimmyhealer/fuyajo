imageid=$(docker inspect -f {{".Id"}} registry.cn-hangzhou.aliyuncs.com/onlinejudge/oj_backend)
docker build -t registry.cn-hangzhou.aliyuncs.com/onlinejudge/oj_backend:latest .
cd ../OnlineJudgeDeploy
sudo docker-compose up -d
cd -
docker image rm ${imageid:7:12}
