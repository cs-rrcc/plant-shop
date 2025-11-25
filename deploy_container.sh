#!/bin/bash

echo "Building Unbeleafable Image"
docker build -t plantshop .

echo "Sowing the container seeds hold on!"
sleep 3

echo "Running CTF Container"
docker run -i --name plantshop --publish 5000:5000 --rm plantshop