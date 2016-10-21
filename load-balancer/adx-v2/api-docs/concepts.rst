.. _concepts:

========
Concepts
========

To use the |apiservice| effectively, you should understand the following terminology:


.. _load-balancer-concept: 

Load balancer
~~~~~~~~~~~~~~~

A load balancer is a logical device which belongs to a Rackspace dedicated account. 
It is used to distribute workloads between multiple back-end systems or services, 
based on the criteria defined as part of its configuration.

.. _node-concept:

Node
~~~~~~~~~~~~~

A node is a back-end device providing a service on a specified IP and port.


.. _virtual-ip-concept:

Virtual IP
~~~~~~~~~~~~~

A virtual IP is an Internet Protocol (IP) address configured on the load balancer for 
use by clients connecting to a service that is load balanced. Incoming connections are 
distributed to back-end nodes based on the configuration of the load balancer.


.. _event-concept:

Event
~~~~~~~

An event is an occurence of an API request to retrieve, create or modify load 
balancer resources. The load balancer API logs information about each event/request. 
Each event is assigned an event ID which can be used to request details about the event.
