# complains  
1. GCloud's default disk is too small
2. GCloud meets error when installing cuda: Err: Not enough space on parition mounted at /.Need 5466499072 bytes.

# create an instance with GPU


gcloud compute instances create gpu-instance
```
--zone us-east1-d
--machine-type n1-standard-4-k80x1
--maintenance-policy TERMINATE
--project PROJECT_NAME
--image-family ubuntu-1604-lts
--image-project ubuntu-os-cloud
--local-ssd interface=SCSI
```

install gcc, perl, g++, python-dev, build-essential, 
```
sudo apt-get update && sudo apt-get install gcc perl g++ linux-source linux-headers-$(uname -r) linux-image-extra-$(uname -r) linux-image-extra-virtual -y && sudo reboot


sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv

```

connect
```
gcloud compute ssh gpu-instance-1 --zone us-east1-d --project PROJECT_NAME

gcloud compute instances list

gcloud compute instances stop

```
# install CUDA

```
wget https://developer.nvidia.com/compute/cuda/8.0/prod/local_installers/cuda_8.0.44_linux-run

```

#install theano

```
sudo pip install theano


```

add to .theanorc
```
[global]
floatX = float32
device = gpu0
[lib]
cnmem = 1
```

add to .bashrc
```

export PATH=/usr/local/cuda-8.0/bin/:$PATHexport LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH

```
