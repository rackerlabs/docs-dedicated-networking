# F5 Load Balancer API documentation version 1

.. raw:: html

   <p style="font-size:17px; color:black">

Last modified date - June 6, 2016

.. raw:: html

   </p>

.. raw:: html

   <hr>

https://bpi.automation.api.rackspacecloud.com/2.0/{account_id}/f5loadbalancers/{device_id}

API Overview
~~~~~~~~~~~~

This API exposes methods to view and manage F5 Load Balancer resources

Authentication and Authorization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Access to this API is granted through a valid token acquired through the
Internal Identity service . The token is passed within the
*X-Auth-Token* HTTP header.

\*\* Roles required to access API : \*\* "bpi\_lbs\_read" is required
for GET calls "bpi\_lbs\_write" is required for PUT, POST, DELETE calls

Standard errors
~~~~~~~~~~~~~~~

-  **400**: Bad request.
-  **401**: Authentication error, the user does not have valid
   authentication details.
-  **403**: Forbidden, you are not authorized to view this resource.
-  **404**: The page or resource requested does not exist.
-  **500**: An indeterminate error occurred. This is caused by an
   unexpected error.
-  **501**: Retrieving a list of details is not supported and/or not
   implemented.
-  **510**: An indeterminate error occurred. This is caused by an
   unexpected error.

--------------

Retrieve load balancer details
------------------------------

Retrieve device details like the model number, OS version, cpu stats,
and so on

/
~

-  **get** *(secured)*:

Nodes
-----

Nodes are a combination of an IP and a port that process requests
directed from a Pool in a Virtual Server. Nodes can be bound to one or
more Pools.

/nodes
~~~~~~

-  **get** *(secured)*: Retrieve all Nodes in the load balancer

-  **post** *(secured)*: Create a Node. The nodeId will be returned by
   querying the eventId.

/nodes/stats
~~~~~~~~~~~~

Retrieve stats for all Nodes in the Node pool.

-  **get** *(secured)*: Retrieve a list of Node stats in the load
   balancer

/nodes/{nodeId}
~~~~~~~~~~~~~~~

Retrieve, update and delete an existing Node specified by a Node id.

-  **get** *(secured)*: Retrieve a Node specified by a Node id

-  **put** *(secured)*: Update a Node specified by a Node id

-  **delete** *(secured)*: Delete a Node in the load balancer specified
   by a Node id.

/nodes/{nodeId}/stats
~~~~~~~~~~~~~~~~~~~~~

Retrieve stats for a Node.

-  **get** *(secured)*: Retrieve a stats for a Node.

/nodes/{nodeId}/monitor-rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

-  **get** *(secured)*: Retrieve monitor rule associated to a Node.

-  **post** *(secured)*: Create monitor rule information for the
   specified Node.

-  **put** *(secured)*: Update a Monitor Rule for the specified Node.

-  **delete** *(secured)*: Delete Node Monitor Rule

Pools
-----

Pools are customizable containers that exist on Load Balancers. Pools
may contain zero or more Nodes. Pools can be bound to one or more
virtuals

/pools
~~~~~~

-  **get** *(secured)*: Retrieve all Pools that have been created in the
   current Load Balancer.

/pools/stats
~~~~~~~~~~~~

Retrieve all stats associated to all Pools that have been created in a
Load Balancer.

-  **get** *(secured)*: Retrieve a list of all stats associated with all
   Pools in a Load Balancer.

/pools/{poolId}
~~~~~~~~~~~~~~~

Retrieve, update and delete on a specified Pool.

-  **get** *(secured)*: Retrieve a Pool specified by a Pool id.

-  **put** *(secured)*: Update a Pool specified by a Pool id.

-  **delete** *(secured)*: Delete a Pool specified by a Pool id.

/pools/{poolId}/stats
~~~~~~~~~~~~~~~~~~~~~

Retrieve all stats associated to this specific Pool.

-  **get** *(secured)*: Retrieve stats for a Pool specified by a Pool
   id.

/pools/{poolId}/monitor-rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a monitor rule associated with this Pool.

-  **get** *(secured)*: Retrieve a monitor rule for the specified Pool.

-  **post** *(secured)*: Create a Monitor Rule for the specified Pool.

-  **put** *(secured)*: Update a Monitor Rule for the specified Pool.

-  **delete** *(secured)*: Delete a Monitor Rule for the specified Pool.

/pools/{poolId}/members
~~~~~~~~~~~~~~~~~~~~~~~

Retrieve and create Pool Members within a Pool.

-  **get** *(secured)*: Retrieve Pool members for the specified Pool id.

-  **post** *(secured)*: Create a new pool member.

/pools/{poolId}/members/stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a Pool members stats.

-  **get** *(secured)*: Retrieve a Pool members list of stats.

/pools/{poolId}/members/{memberId}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve, update and delete a Pool member specified by a member id.

-  **get** *(secured)*: Retrieve a Pool Member from the Pool specified
   by the Pool id.

-  **put** *(secured)*: Update a new Pool Member

-  **delete** *(secured)*: Delete a Pool Member

/pools/{poolId}/members/{memberId}/monitor-rule
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **get** *(secured)*: Retrieve a Pool Member Monitor Rule.

-  **post** *(secured)*: Create a Pool Member Monitor Rule.

-  **put** *(secured)*: Update a Pool Member Monitor Rule.

-  **delete** *(secured)*: Delete a Pool Member's Monitor Rule.

/pools/{poolId}/members/{memberId}/stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **get** *(secured)*: Retrieve a list of stats.

Virtuals
--------

Virtuals are a combination of an ip and a port that distributes trafic
among Nodes in a Pool. Virtuals can contain one or more Pools.

/virtuals
~~~~~~~~~

-  **get** *(secured)*: Retrieve a list of all Virtuals in the Load
   Balancer.

-  **post** *(secured)*: Create a new virtual in a load balancer
   **``address`` is not required, however, if supplied, it will update
   an existing Virtual. To create a new virtual, you must not provide an
   IP or provide a different port number.**

/virtuals/stats
~~~~~~~~~~~~~~~

Retrieve a list of stats for all Virtuals in the Load Balancer.

-  **get** *(secured)*: Retrieve a list of stats for all Virtuals in the
   Load Balancer.

/virtuals/{virtualId}
~~~~~~~~~~~~~~~~~~~~~

Retrieve, update and delete a Virtual in a Load Balancer specified by a
Virtual id.

-  **get** *(secured)*: Retrieve a Virtual in a Load Balancer specified
   by a Virtual id.

-  **put** *(secured)*: Update a virtual in a load balancer specified by
   virtual id **``address`` and port are required in order to make an
   update on the existing virtual.**

-  **delete** *(secured)*: Delete a virtual in a load balancer specified
   by virtual id.

/virtuals/{virtualId}/traffic-classes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve, update and delete Virtual traffic classes in the Load
Balancer.

**Has not been implemented**

-  **get** *(secured)*: Retrieve Virtual's Traffic Classes

/virtuals/{virtualId}/persists
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

-  **get** *(secured)*: Retrieve a single Virtual's persists.

-  **post** *(secured)*: Create a Virtual Persists in the F5 load
   balancer

-  **put** *(secured)*: Update a Virtual Persists.

-  **delete** *(secured)*: Delete a Virtual Persists in the F5 load
   balancer

/virtuals/{virtualId}/stats
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve stats for a Virtual specified by a Virtual id in the Load
Balancer.

-  **get** *(secured)*: Retrieve stats for a Virtual specified by a
   Virtual id.

/virtuals/{virtualId}/auth
~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve, update and delete a Virtual's Auth in the Load Balancer.

**Has not been implemented**

-  **get** *(secured)*: Retrieve a Virtual's auth specified by a Virtual
   id.

/virtuals/{virtualId}/pool
~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve an existing Virtual Pool specified by a Virtual id in the Load
Balancer.

-  **get** *(secured)*: Retrieve a Virtual Pool specified by a Virtual
   id.

Monitors
--------

Monitors verify the health and availability of a Node, a Pool, or group
of Nodes in a Pool.

/monitors
~~~~~~~~~

-  **get** *(secured)*: Retrieve all Monitors in Load Balancer.

/monitors/{monitorId}
~~~~~~~~~~~~~~~~~~~~~

Retrieve, create, update and delete a monitor in a Load Balancer
specified by a monitor id.

-  **get** *(secured)*:
-  **post** *(secured)*: Create a new monitor in the load balancer.

-  **put** *(secured)*: Update a Monitor in the Load Balancer.

-  **delete** *(secured)*: Delete a Monitor in load balancer

Events
------

Retrieve all events.

/events
~~~~~~~

-  **get** *(secured)*: Retrieve all events.

/events/{eventId}
~~~~~~~~~~~~~~~~~

Retrieve a single Event provided an event id

-  **get** *(secured)*: Retrieve an Event with an event id.
