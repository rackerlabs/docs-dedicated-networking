View and manage pools and pool members
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Load balancer pools are a logical grouping of devices used to receive and
process traffic from a virtual server configured in the load balancer.
Each pool must contain one or more members.

You use the Pools operations described in :ref:`F5 BigIP API<f5-api-reference>`
to add, configure, and update pools and pool members. You can also view
statistics and configure monitor rules for pools and pool members.

To use a pool for load balancing, you need to associate it with a
Manage virtual servers`.


Retrieve details for pools
--------------------------

The following example retrieves detailed information about the
pools configured in the load balancer.

The response includes links that you can use to retrieve
additional information about the pools configuration.
For example, use the self link to retrieve information about a specific pool,
and use the members link to retrieve information about
the backend devices that the virtual server uses to manage the load balancer
workloads.

**Example: Retrieve pools in load balancer cURL request**

.. code::

   curl $BASE_URL/pools \
       -H "X-Auth-Token: $TOKEN" \
       -H "Content-type: application/json" \
       | python -m json.tool


If the request is successful, you see an HTTP 200 response header
followed by information about each pool configured in the load balancer.

**Example: Retrieve pools in load balancer response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "http://localhost:8000/f5/12345/pools/POOL-50.56.8.43-80"
                   }
               },
               "allowNat": "yes",
               "allowSnat": "yes",
               "appService": null,
               "description": null,
               "gatewayFailsafeDevice": null,
               "id": "POOL-50.56.8.43-80",
               "ignorePersistedWeight": "disabled",
               "ipTosToClient": "pass-through",
               "ipTosToServer": "pass-through",
               "linkQosToClient": "pass-through",
               "linkQosToServer": "pass-through",
               "loadBalancingMode": "round-robin",
               "members": {
                  "href": "http://localhost:8000/f5/12345/pools/POOL-50.56.8.43-80/members"
               },
               "metadata": [],
               "minActiveMembers": 1,
               "minUpMembers": 0,
               "minUpMembersAction": "failover",
               "minUpMembersChecking": "disabled",
               "monitorRule": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-50.56.8.43-80/monitor-rule"
               },
               "partition": "Common",
               "profiles": null,
               "queueDepthLimit": 0,
               "queueOnConnectionLimit": "disabled",
               "queueTimeLimit": 0,
               "reselectTries": 0,
               "serviceDownAction": null,
               "slowRampTime": 10
           },
           {
               "_links": {
                   "self": {
                       "href": "http://localhost:8000/f5/12345/pools/POOL-192.168.19.5-80"
                   }
               },
               "allowNat": "yes",
               "allowSnat": "yes",
               "appService": null,
               "description": "\"New Test VIP Created\"",
               "gatewayFailsafeDevice": null,
               "id": "POOL-192.168.19.5-80",
               "ignorePersistedWeight": "disabled",
               "ipTosToClient": "pass-through",
               "ipTosToServer": "pass-through",
               "linkQosToClient": "pass-through",
               "linkQosToServer": "pass-through",
               "loadBalancingMode": "round-robin",
               "members": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-192.168.19.5-80/members"
               },
               "metadata": [],
               "minActiveMembers": 0,
               "minUpMembers": 0,
               "minUpMembersAction": "failover",
               "minUpMembersChecking": "disabled",
               "monitorRule": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-192.168.19.5-80/monitor-rule"
               },
               "partition": "Common",
               "profiles": null,
               "queueDepthLimit": 0,
               "queueOnConnectionLimit": "disabled",
               "queueTimeLimit": 0,
               "reselectTries": 0,
               "serviceDownAction": null,
               "slowRampTime": 10
           }
       ]
   }


Retrieve statistics for all pools
---------------------------------

The following example retrieves pool statistics like the number
of members, current session statistics, availability status, and other
information.

**Example: Retrieve pools statistics load balancer cURL request**

.. code::

   curl $BASE_URL/pools/stats \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool

**Example: Retrieve pools statistics load balancer response**

.. code::

   {
       "data": [
           {
               "activeMemberCnt": 1,
               "connq": {
                   "ageEdm": 0,
                   "ageEma": 0,
                   "ageHead": 0,
                   "ageMax": 0,
                   "depth": 0,
                   "serviced": 0
               },
               "connqAll": {
                   "ageEdm": 0,
                   "ageEma": 0,
                   "ageHead": 0,
                   "ageMax": 0,
                   "depth": 0,
                   "serviced": 0
               },
               "curSessions": 0,
               "id": "POOL-50.56.8.43-80",
               "minActiveMembers": 1,
               "monitorRule": "min 1 of /Common/tcp_half_open",
               "name": "POOL-50.56.8.43-80",
               "serverside": {
                   "bitsIn": 19240,
                   "bitsOut": 22656,
                   "curConns": 0,
                   "maxConns": 2,
                   "pktsIn": 36,
                   "pktsOut": 30,
                   "totConns": 6
               },
               "status": {
                   "availabilityState": "available",
                   "enabledState": "enabled",
                   "statusReason": "The pool is available"
               },
               "totRequests": 6
           }
       ]
   }

Retrieve statistics by pool ID
-------------------------------

The following example retrieves pool statistics for a specific pool. You
can use links in the response to get information about members and monitors
that have been configured for the specified pool.


**Example: Retrieve pools statistics load balancer cURL request**

.. code::

   curl $BASE_URL/pools/POOL-50.56.8.43-80 \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool

**Example: Retrieve pool statistics response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "http://localhost:8000/f5/12345/pools/POOL-50.56.8.43-80"
                   }
               },
               "allowNat": "yes",
               "allowSnat": "yes",
               "appService": null,
               "description": null,
               "gatewayFailsafeDevice": null,
               "id": "POOL-50.56.8.43-80",
               "ignorePersistedWeight": "disabled",
               "ipTosToClient": "pass-through",
               "ipTosToServer": "pass-through",
               "linkQosToClient": "pass-through",
               "linkQosToServer": "pass-through",
               "loadBalancingMode": "round-robin",
               "members": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-50.56.8.43-80/members"
               },
               "metadata": [],
               "minActiveMembers": 1,
               "minUpMembers": 0,
               "minUpMembersAction": "failover",
               "minUpMembersChecking": "disabled",
               "monitor": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-50.56.8.43-80/monitor-rule"
               },
              "monitorRule": {
                   "minimum": 1,
                   "names": [
                       "tcp_half_open"
                   ]
               },
               "partition": "Common",
               "profiles": null,
               "queueDepthLimit": 0,
               "queueOnConnectionLimit": "disabled",
               "queueTimeLimit": 0,
               "reselectTries": 0,
               "serviceDownAction": null,
               "slowRampTime": 10
           }
       ]
   }


Update a pool by ID
-------------------

The following example updates an existing pool to change the description and
the settings for the ``least-connections-member`` and ``serviceDownAction``
parameters.

**Example: Update a pool by ID cURL request**

.. code::

   curl $BASE_URL/pools/POOL-50.56.8.43-80 \
      -X PUT \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
           "description": "New description for pools (LBS testing)",
           "loadBalancingMode": "least-connections-member",
           "serviceDownAction": "reset"
          }' \
      | python -m json.tool


**Example: Update a pool by ID response**

.. code::

   {
       "data": {
           "eventId": "5d050b92-6d54-483c-b1e3-4a6dbd431c3f",
           "eventRef": "/events/5d050b92-6d54-483c-b1e3-4a6dbd431c3f",
           "resource": "POOL-50.56.8.43-80",
           "status": "PROCESSING",
           "timestamp": "2016-10-20T14:20:45.2018573Z"
       }
   }

To review the results,
:ref:`submit an event request <retrieve-event-info>` with the event ID
included in the response to the update pool operation.


Update the monitor rule for a pool
----------------------------------

When you update the monitor rule for a pool, the operation
replaces the existing rule.

The following example updates the pool
*POOL-TEST* to add the *MON-TCP-80* rule.

**Example: Update the pool monitor rule cURL request**

.. code::

   curl $BASE_URL/pools/POOL-TEST/monitor-rule \
      -X PUT \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
           "names": [
           "MON-TCP-80
          ],
         "minimum": 1
        }' \
      | python -m json.tool

**Example: Update the pool monitor rule response**

.. code::

   {
    "data": {
        "eventId": "2d7c7a58-1f70-483c-8134-a5ada1b6b91f",
        "eventRef": "/events/2d7c7a58-1f70-483c-8134-a5ada1b6b91f",
        "resource": "POOL-TEST",
        "status": "PROCESSING",
        "timestamp": "2016-10-20T14:50:03.2590261Z"
       }
   }

To review the results,:ref:`submit an event request <retrieve-event-info>`
with the event ID included in the response to the update monitor rule
operation.


Retrieve pool members
---------------------

The following example retrieves the backend devices that are
members of the specified pool.


**Example: Add a pool member cURL request**

.. code::

   curl $BASE_URL/pools/POOL-TEST/members \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool



**Example: Add a pool member response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "http://localhost:8000/f5/12345/pools/POOL-TEST/members/NODE-192.168.20.70:80"
                   }
               },
               "address": "192.168.20.70",
               "appService": null,
               "connectionLimit": 0,
               "description": null,
               "dynamicRatio": 1,
               "id": "NODE-192.168.20.70:80",
               "inheritProfile": "enabled",
               "logging": "disabled",
               "metadata": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-TEST/members/NODE-192.168.20.70:80/metadata"
               },
               "monitorRule": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-TEST/members/NODE-192.168.20.70:80/monitor-rule"
               },
               "port": {
                   "type": "equal",
                   "value": 80
               },
               "priorityGroup": 0,
               "profiles": null,
               "rateLimit": "disabled",
               "ratio": 1,
               "session": "user-enabled",
               "state": "unchecked"
           }
       ]
   }

Create a pool member
---------------------

You can create a pool member by adding an existing node to a pool. To add
a node, use the :ref:`add a node <add-a-node-to-lb>` operation.

The following example adds a backend device with
node ID *VM-321370* to the *POOL-TEST* pool.

**Example: Add a pool member cURL request**

.. code::

   curl $BASE_URL/pools/POOL-TEST/members \
      -X POST \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
           "nodeId": "VM-391370",
           "port": {
              "type": "equal",
              "value": 161
           }
          }' \
      | python -m json.tool

**Example: Add a pool member response**

.. code::

   {
       "data": {
           "eventId": "66d853f0-0f6f-476a-8a12-6107285dfa47",
           "eventRef": "/events/66d853f0-0f6f-476a-8a12-6107285dfa47",
           "resource": "POOL-TEST",
           "status": "PROCESSING",
           "timestamp": "2016-10-20T15:00:11.8748Z"
       }
   }


Check the operation results by submitting an event request using the event ID
included in the response.

**Example: Retrieve event information**

.. code::

   curl $BASE_URL/events/66d853f0-0f6f-476a-8a12-6107285dfa47 \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool

**Example: cURL Retrieve event information response**

.. code::

   {
       "data": [
          {
              "entrytimestamp": "2016-10-20T15:00:12",
              "event_id": "66d853f0-0f6f-476a-8a12-6107285dfa47",
              "message": "COMPLETED",
              "modifiedtimestamp": "2016-10-20T15:01:45",
              "output": "{\"poolId\":\"POOL-TEST\",\"member Id\":\"VM-391370:161\"}",
              "status": "200"
          }
          ]
      }




Retrieve a pool member by ID
----------------------------

Use the pool member ID to retrieve information about a specific pool member.


**Example: Retrieve a pool member by ID cURL request**

.. code::

   curl $BASE_URL/pools/POOL-TEST/members/NODE-192.168.20.70:80 \
        -H "X-Auth-Token: $TOKEN" \
        -H "Content-type: application/json" \
        python -m json.tool


**Example: Retrieve a pool member by ID response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "http://localhost:8000/f5/12345/pools/POOL-TEST/members/NODE-192.168.20.70:80"
                   }
               },
               "address": "192.168.20.70",
               "appService": null,
               "connectionLimit": 0,
               "description": null,
               "dynamicRatio": 1,
               "id": "NODE-192.168.20.70:80",
               "inheritProfile": "enabled",
               "logging": "disabled",
               "metadata": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-TEST/members/NODE-192.168.20.70:80/metadata"
               },
               "monitorRule": {
                   "href": "http://localhost:8000/f5/12345/pools/POOL-TEST/members/NODE-192.168.20.70:80/monitor-rule"
               },
               "port": {
                   "type": "equal",
                   "value": 80
               },
               "priorityGroup": 0,
               "profiles": null,
               "rateLimit": "disabled",
               "ratio": 1,
               "session": "user-enabled",
               "state": "unchecked"
           }
       ]
   }


Update the monitor rule for a pool member
-----------------------------------------

When you update the monitor rule for a pool member, the operation
replaces any existing rule.

The following example updates the pool
*POOL-TEST* to add the *MON-TCP-80* rule.

**Example: Update the pool member monitor rule cURL request**

.. code::

   curl $BASE_URL/pools/POOL-TEST/members/NODE-192.168.20.70:8080/monitor-rule \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool


**Example: Update the pool member monitor rule response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "https": {
                       "href": "http://localhost:8000/f5/12345/monitors/https"
                   },
                   "self": {
                       "href": "http://localhost:8000/f5/12345/pools/POOL-TEST/members/NODE-192.168.20.70:8080"
                   },
                   "tcp": {
                       "href": "http://localhost:8000/f5/12345/monitors/tcp"
                   },
                   "udp": {
                       "href": "http://localhost:8000/f5/12345/monitors/udp"
                   }
               },
               "minimum": "all",
               "names": [
                   "https",
                   "tcp",
                   "udp"
               ]
           }
       ]
   }
