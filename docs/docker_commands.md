Fixing ‘Got permission denied while trying to connect 
to the Docker daemon socket’ error with Docker in Ubuntu

Fix 1: Run all the docker commands with sudo

Fix 2: Running docker commands without sudo
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker
Now running the docker commands without sudo should work just fine.

Sources:
* [How to Fix Docker Permission Denied Error on Ubuntu](https://linuxhandbook.com/docker-permission-denied/)
* [How to fix docker: Got permission denied issue](https://stackoverflow.com/questions/48957195/how-to-fix-docker-got-permission-denied-issue)

docker pull nipreps/fmriprep:<latest-version>
