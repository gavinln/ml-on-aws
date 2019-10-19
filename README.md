# ml-on-aws

* Source code - [Github][1]
* Author - Gavin Noronha - <gnoronha@hotmail.com>

[1]: https://github.com/gavinln/ml-on-aws.git

## 1. About

This project helps to run the [Keras][10] library with [TensorFlow][20] on
a GPU instance on Amazon AWS. It uses an  [Ubuntu (16.04)][30] [Vagrant][40]
Virtual Machine (VM) with [Jupyter][50] notebooks to make it easy to run the
code.

[10]: https://github.com/fchollet/keras
[20]: http://tensorflow.org/
[30]: http://releases.ubuntu.com/16.04/
[40]: http://www.vagrantup.com/
[50]: http://jupyter.org/

Follow the **Requirements** section below for a one-time setup of Virtualbox,
Vagrant and Git before running the commands below. These instructions should
work on Windows, Mac and Linux operating systems.

## 2. Start the virtual machine

### 2.1. Start the VM

1. Change to the ml-on-aws root directory

```
cd ml-on-aws
```

2. Create a do_not_checkin directory ignored by Git for AWS credentials.

```
mkdir do_not_checkin
```

3. Make sure you have a new verion of Vagrant (1.9.1 or higher)

```
vagrant -v
```

4. Start the Virtual machine (VM)

```
vagrant up
```

5. Login to the VM

```
vagrant ssh
```


## [3. Setup the keras-vm user on AWS](doc/setup-keras-user.md)

## 4. Setup ssh key

1. List all tasks (optional)

```
ec2 -l
```

2. Get parameters for configure task (optional)

```
ec2 -h configure
```

3. Setup AWS configuration

```
ec2 configure /vagrant/do_not_checkin/credentials.csv
```

4. Set AWS default region - Oregon, US

```
aws configure set default.region us-west-2
```

5. Display AWS identity (optional)

```
aws sts get-caller-identity
```

5. Display AWS configuration (optional)

```
aws configure list
```

7. Setup SSH key

```
export KEY_NAME=keras-vm
if [[ ! -s /vagrant/do_not_checkin/$KEY_NAME.pem ]]; then
    ec2 ckp --name $KEY_NAME > /vagrant/do_not_checkin/$KEY_NAME.pem
fi
export ANSIBLE_PRIVATE_KEY_FILE=~/$KEY_NAME.pem
cp -f /vagrant/do_not_checkin/$KEY_NAME.pem $ANSIBLE_PRIVATE_KEY_FILE
chmod 400 $ANSIBLE_PRIVATE_KEY_FILE
```

8. Setup ssh-agent with key

```
eval `ssh-agent`
ssh-add $ANSIBLE_PRIVATE_KEY_FILE
```

9. Change to scripts directory

```
cd /vagrant/code
```

## [5. Run EC2 instance](doc/aws-spot-instance.txt)

## 6. Links

[Download link with curl or wget][dlwcow]

[dlwcow]: https://chrome.google.com/webstore/detail/curlwget/jmocjfidanebdlinpbcdkcmgdifblncg

[JMESPATH (used by AWS)][jmespath]

[jmespath]: http://jmespath.org/examples.html

[fire command line][fire]

[fire]: https://github.com/google/python-fire/blob/master/docs/guide.md

[SQL on CSV][textql]

[textql]: https://github.com/dinedal/textql

[CSV toolkit][csvtk]

[csvtk]: https://github.com/shenwei356/csvtk

[cudf - nvidia version of dataframes][cudf]

[cudf]: https://github.com/rapidsai/cudf

[GPU cupy and cudf: first impressions][gpu_first_impression]

[gpu_first_impression]: https://medium.com/rapids-ai/first-impressions-of-gpus-and-pydata-348194660e40

## 7. Requirements

The following software is needed to get the software from github and run
Vagrant. The Git environment also provides an [SSH client][200] for Windows.

* [Oracle VM VirtualBox][210]
* [Vagrant][220] version 1.9.1 or higher
* [Git][230]

[200]: http://en.wikipedia.org/wiki/Secure_Shell
[210]: https://www.virtualbox.org/
[220]: http://vagrantup.com/
[230]: http://git-scm.com/
