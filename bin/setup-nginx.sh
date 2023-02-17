#!/usr/bin/env bash

sudo service nginx stop
sudo rm /etc/nginx/sites-enabled/default
sudo rm /etc/nginx/sites-available/default
sudo rm /etc/nginx/sites-available/pizza
sudo rm /etc/nginx/sites-enabled/pizza
sudo cp /root/challenge/pizza/conf/nginx.conf /etc/nginx/sites-available/pizza
sudo ln -s /etc/nginx/sites-available/pizza /etc/nginx/sites-enabled/pizza
sudo /etc/init.d/nginx restart
