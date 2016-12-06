Manage nodes in the load balancer configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you want to provide load balancing to manage workloads across
backend devices, you must update the load balancer configuration to
add a node for each device.

After you create node, use the Node operations described in the
:ref: `<f5-api-reference>` to retrieve information about
configuration, statistics, monitoring rules, and other details. You can
also update node configuration and monitoring rules and delete nodes.

.. _add-a-node-to-lb:

Add node to load balancer
-------------------------

You add a node to the load balancer configuration by adding its IP address.

The following examples demonstrate how to add the device by using the
naming convention ``NODE<IP_ADDRESS>``.  After you add the node, you
can check the event log to review the configuration details and
get the node ID assigned to the device.

**cURL Add node to load balancer request**

.. code:: bash

   curl $BASE_URL/nodes \
      -X POST \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d'{"address": "192.168.20.70","description": "Test DMZ Node for LBS service"}' \
      | python -m json.tool


A successful request returns an HTTP 200 response header followed by detailed
load balancer information. The API also returns an
event ID associated with the create operation that you can use to check the
status.

**Example: cURL Add node to load balancer response**

.. code:: bash

   {
       "data": {
           "eventId": "e970205c-6103-4a4c-8e3b-703eeec7d810",
           "eventRef": "/events/e970205c-6103-4a4c-8e3b-703eeec7d810",
           "resource": "Nodes",
           "status": "PROCESSING",
           "timestamp": "2016-10-20T13:40:01.7846Z"
       }
   }


Check the operation results by submitting an event request with the event ID
included in the response.


.. _retrieve-event-info:

**Example: cURL Retrieve event information request**

.. code:: bash

   curl $BASE_URL/events/e970205c-6103-4a4c-8e3b-703eeec7d810 \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" | python -m json.tool

**Example: cURL Retrieve event information response**

.. code:: bash

   {
       "data": [
           {
               "entrytimestamp": "2016-10-20T13:40:02",
               "event_id": "e970205c-6103-4a4c-8e3b-703eeec7d810",
               "message": "COMPLETED",
               "modifiedtimestamp": "2016-10-20T13:40:06",
               "output": "{\"nodeId\":\"NODE-192.168.20.70\"}",
               "status": "200"
           }
       ]
   }


Update a node
-------------

If you have the correct :ref:`access permissions <verify-account-permissions>`,
you can update node configuration by using the API. For example, you can
change the description and configuration details like descriptions, logging
status, and rate limits.

The following cURL example shows how to update the node description.

**Example: cURL Update a node request**

.. code:: bash

  curl $BASE_URL/nodes/NODE-192.168.20.70 \
       -X PUT \
       -H "X-Auth-Token: $TOKEN" \
       -H "Content-type: application/json" \
       -d'{"description": "192.168.20.70"}' | python -m json.tool


**cURL Update a node response**

.. code:: bash

   {
       "data": {
           "eventId": "43952b7f-a2fe-42c6-8503-654bfbead31a",
           "eventRef": "/events/43952b7f-a2fe-42c6-8503-654bfbead31a",
           "resource": "NODE-192.168.20.70",
           "status": "PROCESSING",
           "timestamp": "2016-10-20T19:33:46.1658Z"
       }
   }

After you get the response, submit an event request to review the
:ref:`submit an event request <retrieve-event-info>`.


Retrieve all nodes
~~~~~~~~~~~~~~~~~~

The following example shows how to view information about all the nodes
configured in the load balancer.

**Example: cURL Retrieve all nodes request**

.. code::  bash

   curl $BASE_URL/nodes \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" | python -m json.tool


**Example: cURL Retrieve all nodes response**

.. code:: bash

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "https://localhost/f5/127.0.0.1/nodes/VM-391371"
                   }
               },
               "address": "192.168.20.47",
               "appService": null,
               "connectionLimit": 0,
               "description": null,
               "dynamicRatio": 1,
               "id": "VM-391371",
               "logging": "disabled",
               "metadata": {
                   "href": "https://localhost/f5/127.0.0.1/nodes/VM-391371/metadata"
               },
               "monitorRule": {
                   "href": "https://localhost/f5/127.0.0.1/nodes/VM-391371/monitor-rule"
               },
               "partition": "Common",
               "rateLimit": "disabled",
               "ratio": 1,
               "session": "user-enabled",
               "state": "unchecked"
           },
           {
               "_links": {
                  "self": {
                       "href": "https://localhost/f5/127.0.0.1/nodes/VM-391370"
                   }
               },
               "address": "192.168.20.46",
               "appService": null,
               "connectionLimit": 0,
               "description": null,
               "dynamicRatio": 1,
               "id": "VM-391370",
               "logging": "disabled",
               "metadata": {
                   "href": "https://localhost/f5/127.0.0.1/nodes/VM-391370/metadata"
               },
               "monitorRule": {
                   "href": "https://localhost/f5/127.0.0.1/nodes/VM-391370/monitor-rule"
               },
               "partition": "Common",
               "rateLimit": "disabled",
               "ratio": 1,
               "session": "user-enabled",
               "state": "unchecked"
           }
       ]
   }

Add monitor for a node
----------------------

The following example adds a TCP monitor rule for port 80
to the node ``NODE-192.168.10.10``.

**Example: Add monitor rule to a node cURL request**

.. code::

   curl $BASE_URL/nodes/NODE-192.168.10.10/monitor-rule \
       -X POST \
       -H "X-Auth-Token: $TOKEN" \
       -H "Content-type: application/json" \
       -d '{ "names": ["MON-TCP-8080"] }' \
       | python -m json.tool


**Example: Add monitor rule to a node response**

.. code::

   {
       "data": {
           "eventId": "6a67df95-f89c-44bf-8199-ea21f6957fa6",
           "eventRef": "/events/6a67df95-f89c-44bf-8199-ea21f6957fa6",
           "resource": null,
           "status": "PROCESSING",
           "timestamp": "2016-10-20T13:24:39.493Z"
       }
   }

After you get the response, use the event ID to
:ref:`submit an event request <retrieve-event-info>` to check the status
of the operation.
