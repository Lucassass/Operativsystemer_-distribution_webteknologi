# Lab 03: Network

The exercises marked with * are obligatory to complete before the upcoming weeks lecture.

The purpose of this lab is to introduce tools that provide valuable information when working with networks.  Additionally it enforces the students understanding of the layers in both the OSI and TCP/IP models. 

Remember to write useful commands in your cheat sheets.

Table of content
Exercise 01*	
ip (or ifconfig)	
Exercise 02*	
Exercise 03*	
Exercise 04	
Exercise 05*	
Exercise 06*	
Exercise 07	
Exercise 08	

## Exercise 01
In this exercise the student and his/her group is going to connect their computers to a mobile hotspot. The students find each other’s ip and try to visit the website hosted as a docker container.
ip (or ifconfig)
The two commands $ ip a and $ ifconfig are two commands used to show the interfaces of a device, and which ip these interfaces hold. The commands are not described further as they are used in exercise 05.

Your tasks:
Connect your computer to a mobile hotspot, a switch or another computer.
Find your ip through the Terminal.
Spin up the Docker compose from the previous exercise.
Let your group visit your website through your ip.
When using Windows one has to open the exposed port in the firewall

## Exercise 02*
In this exercise the student is going to investigate the two network models, explain how they work and what happens at each layer.


### Your tasks:

#### Name the two network models:

There are two models the OSI model and the TCP/IP model.
the osi model have 7 layers while the TCP/IP only has 4 layers

Explain the different layers of the OSI model:
layer 1 is the physical layer which transmits raw data
layer 2 is the datalink layer which defines format of data
layer 3 is the network layer which decides which physical patht the data will take 
layer 4 is the transport layer which transmits data using transmission protocols including TCP og UDP
layer 5 is the session layer which maintains connections and is responsible for controling ports and sessions
layer 6 is the presentation layer which ensures data is in a usable format and is where data is encrypted 
layer 7 is the application layer human computer interaction layer, where applications can access the network servers

#### Which layers in the OSI model corresponds to which layers in the TCP/IP model.

layer 1 is the application layer which allows access to network resources
layer 2 is the transport layer which provides reliable process to process message delivery and error handling
layer 3 is the internet layer which moves packets from source to destination 
layer 4 is the network interface responsible for the transmission for the between to device on the same network

#### comparing the two models 

layers 1-2 (OSI) is the same as layer 1 on TCP/IP
layer 3 (OSI) is the same as layer 2 on TCP/IP
layer 4 (OSI) is the same as layer 3 on TCP/IP
layers 5-7 (OSI) is the same as layer 4 on TCP/IP


## Exercise 03*
In this exercise the student is going to explain how packages are sent over a network.


### Your tasks:
#### Explain step by step how a package from Computer A with the ip 185.8.135.136 gets to Computer B with the ip 101.24.34.2.

the package or data get passed trough each steps of the osi model starting with the 7 layer when sending the package once
the package reaches the data transmission layer the package is routed through DNAT in which your router converts your DST ip to the DST of the target computer the package then reaches the computer and is passed the otherway around through the osi model starting at layer 1 and ending at layer 7 where the person on the other computer are able to read/write or what ever the package is made for. 


#### Which layers (in the OSI model) does communication happen through:

it happens doing layer 4 which is the transport layer here the data is transmitted using transmission protocols including TCP and UDP

## Exercise 04
In this exercise the student is going to explain what Network Address Translation (NAT) is and how it works.


### Your tasks: 
Give an explanation to the following questions: 

#### What are NAT:

stands for networking address translation and is used for translating network adresses

#### Why is it useful:

it is very useful because it makes it easy to send information as the network adress translation is handled for you by nat

#### How does NAT work:

NAT uses something called PAT which stand for port adress translation which translates any IP adress on the the inside network e.g. 185.8.135.136 to 101.24.34.2. when packages are translated, the router makes note of the attributes of the original and translated packet in the router translation table. 

that way each web server sends the reponse traffic to the destination of the shared IP address with the destination port number which the router had selected in the original outbound traffic When the packets arrive on the Router, it matches them against the translation table to know how to “un-translate” the packet to their original attributes to get them to the appropriate host:


## Exercise 05
In this exercise the student is going to use the Linux tools ifconfig, route, netstat and ip.

The tools are used to configure network interfaces, manipulating the routing table and showing network status.

NB: ifconfig, route and netstat are all deprecated. The tool ip is used instead.


### Your tasks:
#### Examine the tools ifconfig, route and netstat and document their purposes and how they work:

ifconfig 
ifconfig is used to configure the system's kernel-resident network interfaces.

Netstat 
In computing, netstat (network statistics) is a command-line network utility that displays network connections for Transmission Control Protocol (both incoming and outgoing), routing tables, and a number of network interface (network interface controller or software-defined network interface) and network protocol statistics.

route 
The route command allows you to make manual entries into the network routing tables. The route command distinguishes between routes to hosts and routes to networks by interpreting the network address of the Destination variable, which can be specified either by symbolic name or numeric address.


#### Examine the ip tool and how it can be used instead of the three above-mentioned tools:

IP
IP Tools provide calculators and real-time lookups to assist you with your day-to-day system administration and research tasks.

it simplifies the interface and make the 3 commands come under 1 call instead of 3 different calls 

The exercise will return the following message:
$ ifconfig
enxb827eb6429da: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.87.27  netmask 255.255.255.0  broadcast 192.168.87.255
        inet6 fe80::7bed:a5b1:82d5:91ae  prefixlen 64  scopeid 0x20<link>
        ether b8:27:eb:64:29:da  txqueuelen 1000  (Ethernet)
        RX packets 554  bytes 55474 (54.1 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 491  bytes 85268 (83.2 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


$ route
Kernel IP routing table
Destination  Gateway      Genmask      Flags Metric Ref Use Iface
default      192.168.87.1 0.0.0.0      UG    209    0     0 enxb827eb6429da
172.17.0.0   0.0.0.0      255.255.0.0  U     0      0     0 docker0

$ netstat
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0     64 192.168.87.27:ssh       192.168.87.24:56600     ESTABLISHED

Active UNIX domain sockets (w/o servers)
Proto RefCnt Flags       Type       State         I-Node   Path
unix  3      [ ]         DGRAM                    1557     /run/systemd/notify

## Exercise 06*
In this exercise the student is going to examine the interfaces that their computer has, what their IP is.

### Your tasks:
#### Check how many interfaces your computer has. Localise your wireless and wired interfaces. What is their ip: Start two ubuntu containers in the background. Check the containers ip addresses.

docker run -it ubuntu
top
ip addr


## Exercise 07
In this exercise the student is going to describe what DHCP is and how it is useful.


### Your tasks:
#### What is DHCP?

Dynamic Host Configuration Protocol (DHCP) is a network management protocol 

#### Where is it used?

it's used in almost every device that connects to a network including computers, switches, smartphones, and gaming consoles.

#### What is it used for?

it is used to automate the process of configuring devices on IP networks, thus allowing them to use network services such as DNS, NTP, and any communication protocol based on UDP or TCP. A DHCP server dynamically assigns an IP address and other network configuration parameters to each device on a network so they can communicate with other IP networks.

## Exercise 08
In this exercise the student is going to explain the different zones found on a network.


### Your tasks:
#### What are the different zones?
the 3 most commen refered to are inside zone, outside zone, and DMZ zone

#### What is the internal zone?
the internal zone is the inside (trusted, private) behind a firewall

#### What is the external zone?

the external zone is the outside (untrusted, public) not behind a firewall

#### What is the DMZ zone?

the DMZ zone is the demilitarized zone, the DMZ is seen as not belonging to either party bordering it
This metaphor applies to the computing use as the DMZ acts as a gateway to the public Internet.
It is neither as secure as the internal network, nor as insecure as the public internet.

