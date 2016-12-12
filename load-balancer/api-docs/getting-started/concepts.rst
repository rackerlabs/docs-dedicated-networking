.. _concepts:

========
Concepts
========

To use the |apiservice| effectively, you should understand the following
terminology:


.. _load-balancer-concept:

Load balancer
~~~~~~~~~~~~~~~

A load balancer distributes workloads across two or more servers,
network links, or other resources based on criteria defined in the
load balancer configuration.

.. _virtuals-concept:

Virtual server
~~~~~~~~~~~~~~

A virtual server is an IP address (virtual IP) and service port combination,
for example ``172.16.200.210:80``. A virtual server's main function is to
distribute traffic loads to a group of internal, back-end servers. All traffic
is directed to the virtual server, and the server distributes the traffic
across the backend devices.

Virtual servers are configured differently on |ADX| and |F5| devices.

|ADX| virtual server configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On an |ADX|, virtual servers are defined explicitly by binding
virtual servers with real server resources. A real
server is a configuration object that exists within the ADX that defines the
IP address of the internal, back-end server. You associate server resources
with a virtual server using the virtual server binding syntax as shown in
the following example.

.. list-table:: **Brocade ADX load balancer configuration**
   :widths: 20 50
   :header-rows: 1

   * - Logical component
     - Configuration
   * - Virtual server
     - server virtual VS-1.2.3.4 172.16.200.210
   * -   real server1 binding
     -   bind http web1 bind http web2
   * -   real server2 binding
     -   bind http web2

.. note::

   If a real server has multiple service ports configured, you can use those
   ports as resources for the virtual server.


|F5| virtual server configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On a |F5|, you configure the backend devices associated with a virtual server
by using :ref:`pools <pools-concept>` that specify the configuration for the
backend devices and :ref:`pool members <pool-member-concept>` for managing
traffic.

.. list-table:: **BIG-IP F5 load balancer configuration**
   :widths: 20 50
   :header-rows: 1

   * - Logical component
     - Configuration
   * - VIP
     - VS-1.2.3.4:80
   * -   Pool
     -   POOL-172.16.200.210-80
   * -     Member 1
     -     10.200.10.25:80
   * -     Member 2
     -     10.200.10.26:80
   * -     Member 3
     -     10.200.10.27:80

After a pool is applied to a virtual server, client traffic that is destined
for the virtual server uses the pool as its resource. In order for a pool to
serve its function of fault tolerance and redundancy, multiple pool members
are required to be available inside the pool. When a pool has multiple
members, the load balancer decides which one receives the client traffic based
on the load balancing method configured on the device (Round Robin, Weighted
Robin, Least Connection).


.. _pools-concept:

Pools
~~~~~

On |F5|, a load balancing pool is a configuration object created in the Local
Traffic Management system. Each pool is a logical grouping of
devices used to receive and process traffic.

You can define multiple pools in the |F5| configuration. However,
each pool is associated with only one virtual server. The virtual server
distributes traffic across the devices in the pool.

After you create a pool, you configure the backend resources in the pool by
adding pool members.

.. _pool-member-concept:

Pool member
~~~~~~~~~~~

A pool member is a logical object that represents a single
internal physical server IP address and listener port. A pool member can be
included in multiple pools.

.. _node-concept:

Node
~~~~

A node is a logical object that provides the IP address of a single, physical
backend device like a web server. Nodes are the base configuration
object when creating a virtual server.

In an |F5|, a node is added automatically when you add a member to a pool.

.. _event-concept:

Event
~~~~~

The load balancer logs events locally to the log directory (``/var/log``).
Depending on the type of log event, the log message is stored in a specific
file. Each event includes a unique event ID, event type, status of the
request,

You can use the Events API resource to retrieve event information from the log.

On the |F5|, anytime you submit an API request to change the load balancer
configuration, the response includes an event ID that you can use to check
the status of the operation.


.. _monitor-concept:

Monitor
~~~~~~~

For a |F5|, monitors verify the health and availability of a node, pool, or a
group of nodes in a pool.

A health monitor, or a health check, is a configuration object that specifies
a check and parameter values to verify the health and status of a load
balancer component like a pool. Checks are run continuously at a time interval
specified in the monitor configuration. If the component does not
reply correctly to the health monitor before the timeout value expires, it is
identified as having degraded performance, and it is removed from the
availability pool.

A monitor does not take effect until you apply it to a virtual server,
a pool, or a pool member. You apply it by submitting an API request to
create a monitor rule. After applying a rule, you can use the update monitor
rule operations to change configuration settings.

On the |F5|, the default interval timer is 5 seconds, with a default timeout
value of 16 seconds.
