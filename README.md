## IPmininet installation

You can install ipmininet for ubuntu 20.04 from https://ipmininet.readthedocs.io/en/latest/install.html#manual-installation

```
sudo pip install --upgrade git+https://github.com/cnp3/ipmininet.git@v1.0

```

You can use my repository if you want

```
sudo pip install --upgrade git+https://github.com/akemery/ipmininet.git@v0.9
```

You can install frrouting if it is not install y following instructions at http://docs.frrouting.org/projects/dev-guide/en/latest/building-frr-for-ubuntu2004.html

## Run the topo

```
sudo python3 topo_uac.py
```

## Commons errors

If you have the following error messages:

```
*** No default OpenFlow controler found
*** Falling back to OVS bridge
```


You can fix it with

```
sudo apt install openvswitch-testcontroller
sudo ln -s /usr/bin/ovs-testcontroller /usr/bin/controller
```

If you have the following error messages:

```
Exception: Please shutdown the controller which is running on port 6653 
```

You can fix it with:


```
sudo fuser -k 6653/tcp
```
