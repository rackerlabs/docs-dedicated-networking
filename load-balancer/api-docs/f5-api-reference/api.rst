**Endpoint**:
https://bpi.automation.api.rackspacecloud.com/2.0/{tenant\_id}/f5loadbalancers/{core\_id}

.. code:: javascript

    GET /

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": [{
        "customer": "1234567",
        "uptime": "396 days,  9:22",
        "ha_role": "true",
        "hostname": "1234567-lb1.example.rackspace.com",
        "ram_mem": [{
          "total_kbytes": "4158218",
          "free_kbytes": "162846",
          "name": "TMM",
          "used_kbytes": "2860515"
        }],
        "model_name": "BIG-IP 1600",
        "os_version": "11.5.1, build: 3.0.131, edition: Hotfix HF3",
        "management_ip": "127.0.0.1",
        "role": "unimplemented",
        "cpu_load": [{
          "load_1_sec_avg": {
            "percent_load": 19,
            "seconds_since": 0
          },
          "average": {
            "percent_load": 17,
            "seconds_since": 0
          },
          "load_60_sec_avg": {
            "percent_load": -1,
            "seconds_since": -1
          },
          "last_peak_load": {
            "percent_load": 50,
            "seconds_since": 0
          },
          "mod_name": "System CPU",
          "load_5_sec_avg": {
            "percent_load": -1,
            "seconds_since": -1
          },
          "load_300_sec_avg": {
            "percent_load": -1,
            "seconds_since": -1
          }
        }],
        "ha_status": "active",
        "id": "1234567"
      }]
    }

Retrieve nodes
--------------

Retrieve all nodes that have been configured in the load balancer.

.. code:: javascript

    GET /nodes

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "127.0.0.1",
                "address": "127.0.0.1",
                "appService": "none",
                "connectionLimit": 0,
                "description": "a node",
                "dynamicRatio": 1,
                "logging": "disabled",
                "metadata": {},
                "monitors": {},
                "partition": "Common",
                "rateLimit": "disabled",
                "ratio": 1,
                "session": "user-enabled",
                "state": "unchecked"
            }
        ]
    }

Create a node
-------------

Add a node to the load balancer.

You can use the event ID returned in the API response to submit an event
request to verify that the operation completed and get the ID for the
new node.

.. code:: javascript

    POST /nodes

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "address": "162.242.206.208",
        "appService": null,
        "connectionLimit": 2,
        "description": "test truncated",
        "dynamicRatio": 11,
        "logging": "enabled",
        "rateLimit": "disabled",
        "ratio": 1
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "Nodes",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve node statistics
------------------------

Retrieve statistics for all nodes that were added to the load balancer.

.. code:: javascript

    GET /nodes/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "my-special-node",
                "address": "127.0.0.1",
                "curSessions": 1,
                "monitorRule": {
                    "monitors": [
                        "default"
                    ],
                    "minimum": "all"
                },
                "serverside": {
                    "bitsIn": 1,
                    "bitsOut": 1,
                    "curConns": 1,
                    "maxConns": 2,
                    "pktsIn": 1,
                    "pktsOut": 1,
                    "totConns": 1
                },
                "sessionStatus": "fine",
                "status": {
                    "availabilityState": "available",
                    "enabledState": "maybe",
                    "statusReason": "because"
                },
                "totRequests": 3
            }
        ]
    }

Retrieve node information by node ID
------------------------------------

Returns information about the node associated with the node ID.

.. code:: javascript

    GET /nodes/{nodeId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [  
            {
                "id": "127.0.0.1",
                "address": "127.0.0.1",
                "appService": "none",
                "connectionLimit": 0,
                "description": "a node",
                "dynamicRatio": 1,
                "logging": "disabled",
                "monitors": {},
                "metadata": {},
                "partition": "Common",
                "rateLimit": "disabled",
                "session": "user-enabled",
                "state": "unchecked"
            }
        ]
    }

Update a node
-------------

Change description and configuration settings for an existing node. You
need the node ID to complete this operation.

.. code:: javascript

    PUT /nodes/{nodeId}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "appService": null,
        "connectionLimit": 2,
        "description": "Updated node",
        "dynamicRatio": 11,
        "logging": "enabled",
        "rateLimit": "disabled",
        "ratio": 1
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<nodeId:str>",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Delete a node
-------------

Remove a node from the load balancer configuration. You need the node ID
to complete this operation.

.. code:: javascript

    DELETE /nodes/{nodeId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": {
        "eventId": "<eventId:str>",
        "resource": "<nodeId:str>",
        "timestamp": "2016-03-08T17:22:33.6349648Z",
        "eventRef": "/events/<eventId:str>"
      }
    }

Retrieve node statistics
------------------------

Retrieve information about availability, session status, monitor rules
for the device with the specified node ID.

.. code:: javascript

    GET /nodes/{nodeId}/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "my-special-node",
                "address": "127.0.0.1",
                "curSessions": 1,
                "monitorRule": {
                    "monitors": [
                        "default"
                    ],
                    "minimum": "all"
                },
                "serverside": {
                    "bitsIn": 1,
                    "bitsOut": 1,
                    "curConns": 1,
                    "maxConns": 2,
                    "pktsIn": 1,
                    "pktsOut": 1,
                    "totConns": 1
                },
                "sessionStatus": "fine",
                "status": {
                    "availabilityState": "available",
                    "enabledState": "maybe",
                    "statusReason": "because"
                },
                "totRequests": 3
            }
        ]
    }

Retrieve monitor rule for node
------------------------------

Retrieve information about the monitor rule applied to a specific node.

.. code:: javascript

    GET /nodes/{nodeId}/monitor-rule

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "monitors": [
                    "https_443",
                    "real_server",
                    "tcp_echo"
                ],
                "minimum": 1
            }
        ]
    }

Add a monitor rule to automate checks
-------------------------------------

Apply monitor rule to the specified node. To find the names of the
available monitors, submit a GET monitors request.

.. code:: javascript

    POST /nodes/{nodeId}/monitor-rule

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "names": [
            "https_443"
        ],
        "minimum": 1
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": {
        "eventId": "<eventId:str>",
        "status": "PROCESSING",
        "resource": "<nodeId:str>"
        "eventRef": "/events/<eventId:str>",
        "timestamp": "2016-03-18T03:18:35.5077939Z"
      }
    }

Update a monitor rule on node
-----------------------------

Update the monitor rule configured for a specified node.

.. code:: javascript

    PUT /nodes/{nodeId}/monitor-rule

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "names": [
            "https_443",
            "real_server",
            "tcp_echo"
        ],
        "minimum": 1
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<nodeId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove monitor rule from a node
-------------------------------

Remove the monitor rule from the specified node.

.. code:: javascript

    DELETE /nodes/{nodeId}/monitor-rule

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data" : {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve pools
--------------

Retrieve information about all pools created in the current load
balancer.

.. code:: javascript

    GET /pools

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "POOL-127.0.0.1-80",
                "allowNat": "yes",
                "allowSnat": "yes",
                "appService": null,
                "gatewayFailsafeDevice": null,
                "ignorePersistedWeight": "disabled",
                "ipTosToClient": "pass-through",
                "ipTosToServer": "pass-through",
                "linkQosToClient": "pass-through",
                "linkQosToServer": "pass-through",
                "loadBalancingMode": "round-robin",
                "metadata": {},
                "minActiveMembers": 0,
                "minUpMembers": 0,
                "minUpMembersAction": "failover",
                "minUpMembersChecking": "disabled",
                "partition": "Common",
                "profiles": null,
                "queueDepthLimit": 0,
                "queueOnConnectionLimit": "disabled",
                "queueTimeLimit": 0,
                "reselectTries": 0,
                "serviceDownAction": null,
                "slowRampTime": 10,
                "description": null,
                "members": {},
                "monitors": {}
            }
        ]
    }

Retrieve pool statistics
------------------------

Retrieve statistics for all pools associated have been created in a load
balancer.

.. code:: javascript

    GET /pools/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": [
        {
          "id": "POOL-127.0.0.1-80",
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
          "minActiveMembers": 0,
          "monitorRule": {
            "monitors": [
              "MON-TCP-80"
            ],
            "minimum": "all"
          },
          "name": "POOL-127.0.0.1-80",
          "totRequests": 0,
          "serverside": {
            "bitsIn": 0,
            "bitsOut": 0,
            "curConns": 0,
            "maxConns": 0,
            "pktsIn": 0,
            "pktsOut": 0,
            "totConns": 0
          },
          "status": {
            "availabilityState": "available",
            "enabledState": "enabled",
            "statusReason": "The pool is available"
          }
        }
      ]
    }

Retrieve a pool by ID
---------------------

Retrieve information about a specified pool by pool ID. Use the retrieve
pools operation to pool specified by a pool id.

.. code:: javascript

    GET /pools/{poolId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "POOL-127.0.0.1-80",
                "allowNat": "yes",
                "allowSnat": "yes",
                "appService": null,
                "gatewayFailsafeDevice": null,
                "ignorePersistedWeight": "disabled",
                "ipTosToClient": "pass-through",
                "ipTosToServer": "pass-through",
                "linkQosToClient": "pass-through",
                "linkQosToServer": "pass-through",
                "loadBalancingMode": "round-robin",
                "metadata": {},
                "minActiveMembers": 0,
                "minUpMembers": 0,
                "minUpMembersAction": "failover",
                "minUpMembersChecking": "disabled",
                "partition": "Common",
                "profiles": "none",
                "queueDepthLimit": 0,
                "queueOnConnectionLimit": "disabled",
                "queueTimeLimit": 0,
                "reselectTries": 0,
                "serviceDownAction": null,
                "slowRampTime": 10,
                "description": "none",
                "members": {},
                "monitors": {}
            }
        ]
    }

Update a Pool
-------------

Update the configuration for a specified pool.

.. code:: javascript

    PUT /pools/{poolId}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "allowNat": "yes",
        "allowSnat": "yes",
        "appService": null,
        "description": null,
        "gatewayFailsafeDevice": null,
        "ignorePersistedWeight": "disabled",
        "ipTosToClient": "pass-through",
        "ipTosToServer": "pass-through",
        "linkQosToClient": "pass-through",
        "linkQosToServer": "pass-through",
        "loadBalancingMode": "round-robin",
        "minActiveMembers": 0,
        "minUpMembers": 0,
        "minUpMembersAction": "failover",
        "minUpMembersChecking": "disabled",
        "profiles": null,
        "queueDepthLimit": 0,
        "queueOnConnectionLimit": "disabled",
        "queueTimeLimit": 0,
        "reselectTries": 0,
        "serviceDownAction": null,
        "slowRampTime": 10
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-24T10:41:08.6194067Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove a pool
-------------

Remove a specified pool from the load balancer configuration.

.. code:: javascript

    DELETE /pools/{poolId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-24T10:41:08.6194067Z",
        }
    }

Retrieve stats for a Pool
-------------------------

Retrieve stats for a Pool specified by a Pool id.

.. code:: javascript

    GET /pools/{poolId}/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "POOL-127.0.0.1-80",
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
                "minActiveMembers": 0,
                "monitorRule": {
                    "monitors": [
                        "MON-TCP-80"
                    ],
                    "minimum": "all"
                },
                "name": "POOL-127.0.0.1-80",
                "totRequests": 0,
                "serverside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "status": {
                    "availabilityState": "available",
                    "enabledState": "enabled",
                    "statusReason": "The pool is available"
                }
            }
        ]
    }

Retrieve monitor rule for a pool
--------------------------------

Retrieve a monitor rule associated with a specified pool.

.. code:: javascript

    GET /pools/{poolId}/monitor-rule

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "names": [
                    "https_443",
                    "real_server",
                    "tcp_echo"
                ],
                "minimum": 1
            }
        ]
    }

Add a monitor rule to a pool
----------------------------

Add a monitor rule to a specified pool. To find the names of the
available monitors, submit a GET monitors request.

.. code:: javascript

    POST /pools/{poolId}/monitor-rule

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "names": [
            "tcp"
        ],
        "minimum": 1
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": {
        "eventId": "<eventId:str>",
        "status": "PROCESSING",
        "timestamp": "2016-03-18T03:18:35.5077939Z",
        "resource": "<poolId:str>",
        "eventRef": "/events/<eventId:str>"
      }
    }

Update monitor rule for a pool
------------------------------

Update the monitor rule applied to a specified pool. Use the retrieve
monitors by pool ID operation to find the monitor rule name.

.. code:: javascript

    PUT /pools/{poolId}/monitor-rule

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "names": [
            "tcp"
        ],
        "minimum": "all"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str)",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-16T17:09:53.1059638Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove monitor rule from a pool
-------------------------------

Remove a monitor rule for the specified pool.

.. code:: javascript

    DELETE /pools/{poolId}/monitor-rule

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str]",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-16T17:09:53.1059638Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve pool members for a pool
--------------------------------

Retrieve a list of members associated with a specific pool ID.

.. code:: javascript

    GET /pools/{poolId}/members

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": [
        {
          "id": "127.0.0.1:80",
          "port": {
            "type": "equal",
            "value": 80
          },
          "monitors": {},
          "address": "127.0.0.1",
          "appService": "none",
          "connectionLimit": 0,
          "description": "none",
          "dynamicRatio": 1,
          "inheritProfile": "enabled",
          "logging": "disabled",
          "monitor": "default",
          "priorityGroup": 0,
          "rateLimit": "disabled",
          "ratio": 1,
          "session": "monitor-enabled",
          "state": "down",
          "metadata": {},
          "profiles": []
        }
      ]
    }

Create a pool member in a pool
------------------------------

Create a pool member by adding an existing node to a specified pool.

.. code:: javascript

    POST /pools/{poolId}/members

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "nodeId": "<nodeId>",
        "port": {
            "type": "equal",
            "value": 80
        }
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "resource": "<poolId:str>",
            "type": "<memberId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve statistics for pool members
------------------------------------

Retrieve statistics for all pool members in a specified pool including
configuration settings, availability, and monitoring status.

.. code:: javascript

    GET /pools/{poolId}/members/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": [
        {
          "id": "test1:80",
          "address": "127.0.0.1",
          "connq": {
            "ageEdm": 0,
            "ageEma": 0,
            "ageHead": 0,
            "ageMax": 0,
            "depth": 0,
            "serviced": 0
          },
          "curSessions": 0,
          "monitorRule": {
            "monitors": [
              "default"
            ],
            "minimum": "all"
          },
          "monitorStatus": "unchecked",
          "nodeName": "test1",
          "poolName": "test2",
          "port": {
            "type": "equal",
            "value": 80
          },
          "serverside": {
            "bitsIn": 0,
            "bitsOut": 0,
            "curConns": 0,
            "maxConns": 0,
            "pktsIn": 0,
            "pktsOut": 0,
            "totConns": 0
          },
          "sessionStatus": "enabled",
          "status": {
            "availabilityState": "unknown",
            "enabledState": "enabled",
            "statusReason": "Pool member does not have service checking enabled"
          },
          "totRequests": 0
        }
      ]
    }

Retrieve statistics for a pool member
-------------------------------------

Retrieve configuration, monitor settings, and other data for a pool
member.

.. code:: javascript

    GET /pools/{poolId}/members/{memberId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "127.0.0.1:80",
                "address": "127.0.0.1",
                "appService": null,
                "connectionLimit": 0,
                "description": null,
                "dynamicRatio": 1,
                "inheritProfile": "enabled",
                "logging": "disabled",
                "monitor": "default",
                "priorityGroup": 0,
                "rateLimit": "disabled",
                "ratio": 1,
                "session": "monitor-enabled",
                "state": "down",
                "metadata": {},
                "monitors": {},
                "profiles": []
            }
        ]
    }

Update pool member configuration
--------------------------------

Update configuration settings for a specified pool member

.. code:: javascript

    PUT /pools/{poolId}/members/{memberId}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "appService": null,
        "connectionLimit": 0,
        "description": null,
        "dynamicRatio": 1,
        "inheritProfile": "enabled",
        "logging": "enabled",
        "priorityGroup": 0,
        "rateLimit": "enabled"
     }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "type": "<memberId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove pool member from pool
----------------------------

Remove a pool member by pool ID

.. code:: javascript

    DELETE /pools/{poolId}/members/{memberId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "type": "<memberId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve pool member monitor rule
---------------------------------

Retrieves configuration settings for the monitor rule applied to a
specified pool member.

.. code:: javascript

    GET /pools/{poolId}/members/{memberId}/monitor-rule

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": [
        {
          "minimum": "all",
          "address": "127.0.0.1"
        }
      ]
    }

Create a monitor rule for a pool member
---------------------------------------

Add monitors to a pool member in a specified pool.

.. code:: javascript

    POST /pools/{poolId}/members/{memberId}/monitor-rule

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "names": [
        "tcp",
        "https"
      ],
      "minimum": 1
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "type": "<memberId:str>",
            "timestamp": "2016-03-24T10:41:08.6194067Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Update monitor rule for pool member
-----------------------------------

Update the configuration settings for the monitor rule applied to a
specified pool member.

.. code:: javascript

    PUT /pools/{poolId}/members/{memberId}/monitor-rule

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "names": [
            "tcp"
        ],
        "minimum": 1
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "type": "<memberId:str>",
            "timestamp": "2016-03-16T17:09:53.1059638Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove monitor rule from pool member
------------------------------------

Remove the monitor rule applied to a specified pool member (memberId) in
a specified pool (poolId).

.. code:: javascript

    DELETE /pools/{poolId}/members/{memberId}/monitor-rule

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "resource": "<poolId:str>",
            "type": "<memberId:str>",
            "eventRef": "/events/<eventId:str}",
            "status": "PROCESSING",
            "timestamp": "2016-03-08T17:22:33.6249648Z"
        }
    }

Retrieve statistics for pool member
-----------------------------------

Retrieve configuration, monitor settings, and other data for a pool
member.

.. code:: javascript

    GET /pools/{poolId}/members/{memberId}/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "test1:80",
                "address": "127.0.0.1",
                "connq": {
                    "ageEdm": 0,
                    "ageEma": 0,
                    "ageHead": 0,
                    "ageMax": 0,
                    "depth": 0,
                    "serviced": 0
                },
                "curSessions": 0,
                "monitorRule": {
                    "monitors": [
                        "default"
                    ],
                    "minimum": "all"
                },
                "monitorStatus": "unchecked",
                "nodeName": "test1",
                "poolName": "test2",
                "port": {
                    "type": "equal",
                    "value": 80
                },
                "serverside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "sessionStatus": "enabled",
                "status": {
                    "availabilityState": "unknown",
                    "enabledState": "enabled",
                    "statusReason": "Pool member does not have service checking enabled"
                },
                "totRequests": 0
            }
        ]
    }

Retrieve virtual server details
-------------------------------

Retrieve information about all virtual servers configured in the load
balancer including configuration data and status information.

.. code:: javascript

    GET /virtuals

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "VIP-127.0.0.1-80",
                "address": "127.0.0.1",
                "addressStatus": "yes",
                "appService": "none",
                "auth": "none",
                "autoLasthop": "default",
                "bwcPolicy": "none",
                "clonePools": "none",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "description": "none",
                "destination": "127.0.0.1:http",
                "enabled": "enabled",
                "fallbackPersistence": "none",
                "gtmScore": 0,
                "ipForward": "",
                "ipProtocol": "tcp",
                "lastHopPool": "none",
                "mask": "255.255.255.255",
                "metadata": "none",
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "nat64": "disabled",
                "partition": "Common",
                "persist": {
                    "cookie": {
                        "default": "yes"
                    }
                },
                "policies": "none",
                "pool": {},
                "port": {
                    "type": "equal",
                    "value": 80
                },
                "profiles": {
                    "http": {
                        "context": "all"
                    },
                    "tcp": {
                        "context": "all"
                    }
                },
                "rateClass": "none",
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "relatedRules": "none",
                "rules": "none",
                "securityLogProfiles": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {
                    "pool": "none",
                    "type": "none"
                },
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "trafficClasses": "none",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlansDisabled": "vlans-disabled",
                "vsIndex": 7
            }
        ]
    }

Add a virtual server
--------------------

Add a virtual server configuration to the load balancer. When you add a
virtual server configuration, do not specify an IP address unless you
want to add a configuration to an existing address on a unique port.

**``address`` is not required, however, if supplied, it will update an
existing Virtual. To create a new virtual, you must not provide an IP or
provide a different port number.**

.. code:: javascript

    POST /virtuals

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "address": "172.16.1.160",
      "source": "0.0.0.0\/0",
      "ipProtocol": "tcp",
      "ipForward": "disabled",
      "gtmScore": 0,
      "description": "New Description",
      "port": {
        "value": 80,
        "type": "equal"
      },
      "connectionLimit": 99
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": {
        "eventId": "02d1ba2a-0edf-4583-8e2c-ab0b54c78193",
        "status": "PROCESSING",
        "resource": "Virtuals",
        "eventRef": "/events/<eventId:str>",
        "timestamp": "2016-03-18T03:18:35.5077939Z"
      }
    }

Retrieve virtual server statistics
----------------------------------

Retrieve statistical information for all virtual servers configured in
the load balancer.

.. code:: javascript

    GET /virtuals/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "clientside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 0,
                "csMeanConnDur": 0,
                "csMinConnDur": 0,
                "destination": "127.0.0.1:80",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "VIP-127.0.0.1-80",
                "name": "VIP-127.0.0.1-80",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "unknown",
                    "enabledState": "enabled",
                    "statusReason": "The children pool member(s) either don't have service checking enabled, or service check results are not available yet"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 0,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            },
            {
                "clientside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 0,
                "csMeanConnDur": 0,
                "csMinConnDur": 0,
                "destination": "127.0.0.1:443",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "TestVip-DONT-DELETE",
                "name": "TestVip-DONT-DELETE",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "unknown",
                    "enabledState": "enabled",
                    "statusReason": "The children pool member(s) either don't have service checking enabled, or service check results are not available yet"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 0,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            },
            {
                "clientside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 0,
                "csMeanConnDur": 0,
                "csMinConnDur": 0,
                "destination": "127.0.0.1:443",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "VIP-127.0.0.1-443",
                "name": "VIP-127.0.0.1-443",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "available",
                    "enabledState": "enabled",
                    "statusReason": "The virtual server is available"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 0,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            },
            {
                "clientside": {
                    "bitsIn": 2784874696,
                    "bitsOut": 13416053656,
                    "curConns": 5,
                    "maxConns": 61,
                    "pktsIn": 5698557,
                    "pktsOut": 1560895,
                    "totConns": 1485109
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 14319373760,
                "csMeanConnDur": 7972,
                "csMinConnDur": 56,
                "destination": "any:any",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "VS-FORWARDING",
                "name": "VS-FORWARDING",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "unknown",
                    "enabledState": "enabled",
                    "statusReason": "The children pool member(s) either don't have service checking enabled, or service check results are not available yet"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 2,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            }
        ]
    }

Retrieve virtual server information by ID
-----------------------------------------

Retrieve information about the specified virtual server.

.. code:: javascript

    GET /virtuals/{virtualId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "VIP-127.0.0.1-80",
                "address": "127.0.0.1",
                "addressStatus": "yes",
                "appService": "none",
                "auth": "none",
                "autoLasthop": "default",
                "bwcPolicy": "none",
                "clonePools": "none",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "description": "none",
                "destination": "127.0.0.1:http",
                "enabled": "enabled",
                "fallbackPersistence": "none",
                "gtmScore": 0,
                "ipForward": "",
                "ipProtocol": "tcp",
                "lastHopPool": "none",
                "mask": "255.255.255.255",
                "metadata": "none",
                "mirror": "disabled",
                "mobileAppTunnel": "disabled",
                "nat64": "disabled",
                "partition": "Common",
                "persist": {
                    "cookie": {
                        "default": "yes"
                    }
                },
                "policies": "none",
                "pool": {},
                "port": {
                    "type": "equal",
                    "value": 80
                },
                "profiles": {
                    "http": {
                        "context": "all"
                    },
                    "tcp": {
                        "context": "all"
                    }
                },
                "rateClass": "none",
                "rateLimit": "disabled",
                "rateLimitDstMask": 0,
                "rateLimitMode": "object",
                "rateLimitSrcMask": 0,
                "relatedRules": "none",
                "rules": "none",
                "securityLogProfiles": "none",
                "source": "0.0.0.0/0",
                "sourceAddressTranslation": {
                    "pool": "none",
                    "type": "none"
                },
                "sourcePort": "preserve",
                "synCookieStatus": "not-activated",
                "trafficClasses": "none",
                "translateAddress": "enabled",
                "translatePort": "enabled",
                "vlansDisabled": "vlans-disabled",
                "vsIndex": 7
            }
        ]
    }

Update a virtual server by ID
-----------------------------

When you update an existing virtual server, you must specify the address
and port in the request.

**``address`` and port are required in order to make an update on the
existing virtual.**

.. code:: javascript

    PUT /virtuals/{virtualId}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "address": "172.16.1.160",
        "source": "0.0.0.0\/0",
        "ipProtocol": "tcp",
        "ipForward": "disabled",
        "gtmScore": 0,
        "description": "New Description updated",
        "port": {
            "value": 80,
            "type": "equal"
        },
        "connectionLimit": 99
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "02d1ba2a-0edf-4583-8e2c-ab0b54c78193",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z"
        }
    }

Remove a virtual server
-----------------------

Remove a specified virtual server from the load balancer configuration.

.. code:: javascript

    DELETE /virtuals/{virtualId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventid:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve Traffic Classes
------------------------

Retrieve Virtual's Traffic Classes

.. code:: javascript

    GET /virtuals/{virtualId}/traffic-classes

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "names": [
                    "local-trafficClass"
                ]
            }
        ]
    }

Retrieve persistent profiles for a virtual server
-------------------------------------------------

Returns information about the persistent profiles configured for a
virtual server. These profiles enable tracking and storage of session
data to ensure that client requests are directed to the same pool member
throughout the life of a session or during subsequent sessions.

.. code:: javascript

    GET /virtuals/{virtualId}/persists

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
              "profileName": "my-cool-persist"
            }

        ]
    }

Create a persistent profile
---------------------------

Create a persistent profile configuration for a specified virtual
server.

.. code:: javascript

    POST /virtuals/{virtualId}/persists

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "names": [
            "source_addr",
            "dest_addr"
        ]
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Update virtual server persistent profile
----------------------------------------

Update the persistent profile for a virtual server.

.. code:: javascript

    PUT /virtuals/{virtualId}/persists

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "names": [
            "hash"
        ]
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove a persistent profile
---------------------------

Remove a persistent profile configuration from a specified virtual
server.

.. code:: javascript

    DELETE /virtuals/{virtualId}/persists

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z"
        }
    }

Retrieve virtual server information by ID
-----------------------------------------

Retrieve statistics for a specified virtual server configured in the
load balancer.

.. code:: javascript

    GET /virtuals/{virtualId}/stats

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "clientside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 0,
                "csMeanConnDur": 0,
                "csMinConnDur": 0,
                "destination": "127.0.0.1:80",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "VIP-127.0.0.1-80",
                "name": "VIP-127.0.0.1-80",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "unknown",
                    "enabledState": "enabled",
                    "statusReason": "The children pool member(s) either don't have service checking enabled, or service check results are not available yet"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 0,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            },
            {
                "clientside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 0,
                "csMeanConnDur": 0,
                "csMinConnDur": 0,
                "destination": "127.0.0.1:443",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "TestVip-DONT-DELETE",
                "name": "TestVip-DONT-DELETE",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "unknown",
                    "enabledState": "enabled",
                    "statusReason": "The children pool member(s) either don't have service checking enabled, or service check results are not available yet"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 0,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            },
            {
                "clientside": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 0,
                "csMeanConnDur": 0,
                "csMinConnDur": 0,
                "destination": "127.0.0.1:443",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "VIP-127.0.0.1-443",
                "name": "VIP-127.0.0.1-443",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "available",
                    "enabledState": "enabled",
                    "statusReason": "The virtual server is available"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 0,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            },
            {
                "clientside": {
                    "bitsIn": 2784874696,
                    "bitsOut": 13416053656,
                    "curConns": 5,
                    "maxConns": 61,
                    "pktsIn": 5698557,
                    "pktsOut": 1560895,
                    "totConns": 1485109
                },
                "cmpEnableMode": "all-cpus",
                "cmpEnabled": "enabled",
                "csMaxConnDur": 14319373760,
                "csMeanConnDur": 7972,
                "csMinConnDur": 56,
                "destination": "any:any",
                "ephemeral": {
                    "bitsIn": 0,
                    "bitsOut": 0,
                    "curConns": 0,
                    "maxConns": 0,
                    "pktsIn": 0,
                    "pktsOut": 0,
                    "totConns": 0
                },
                "fiveMinAvgUsageRatio": 0,
                "fiveSecAvgUsageRatio": 0,
                "id": "VS-FORWARDING",
                "name": "VS-FORWARDING",
                "oneMinAvgUsageRatio": 0,
                "status": {
                    "availabilityState": "unknown",
                    "enabledState": "enabled",
                    "statusReason": "The children pool member(s) either don't have service checking enabled, or service check results are not available yet"
                },
                "syncookie": {
                    "accepts": 0,
                    "hwAccepts": 0,
                    "hwSyncookies": 0,
                    "hwsyncookieInstance": 0,
                    "rejects": 2,
                    "swsyncookieInstance": 0,
                    "syncacheCurr": 0,
                    "syncacheOver": 0,
                    "syncookies": 0
                },
                "syncookieStatus": "not-activated",
                "totRequests": 0
            }
        ]
    }

Retrieve A Virtual's Auth
-------------------------

Retrieve a Virtual's auth specified by a Virtual id.

.. code:: javascript

    GET /virtuals/{virtualId}/auth

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "profileNames": [
                    "secure-auth",
                    "read-auth"
                ]
            }
        ]
    }

Retrieve a virtual pool by virtual ID.
--------------------------------------

Retrieve information about the virtual pools associated with a specified
virtual server.

.. code:: javascript

    GET /virtuals/{virtualId}/pool

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "name": "test_pool"
            } 
        ]
    }

Retrieve Monitors
-----------------

Retrieve monitors configured in the load balancer.

.. code:: javascript

    GET /monitors

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [
            {
                "id": "TestMonitor-DONT-DELETE",
                "appService": null,
                "address" : "127.0.0.1",
                "port": {
                    "type": "equal",
                    "value": 80
                },
                "defaultsFrom": "tcp",
                "description": null,
                "interval": 5,
                "ipDscp": 0,
                "manualResume": "disabled",
                "recv": null,
                "recvDisable": null,
                "reverse": "disabled",
                "send": null,
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "type": "tcp",
                "upInterval": 0
            },
            {
                "id": "MON-TCP-80",
                "appService": null,
                "address" : "127.0.0.1",
                "port": {
                    "type": "equal",
                    "value": 80
                },
                "defaultsFrom": "tcp",
                "description": null,
                "interval": 5,
                "ipDscp": 0,
                "manualResume": "disabled",
                "recv": null,
                "recvDisable": null,
                "reverse": "disabled",
                "send": null,
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "type": "tcp",
                "upInterval": 0
            },
            {
                "id": "test-monitor",
                "appService": null,
                "address" : "127.0.0.1",
                "port": {
                    "type": "any",
                    "value": "any"
                },
                "debug" : "enabled",
                "defaultsFrom": "udp",
                "description": null,
                "interval": 5,
                "manualResume": "disabled",
                "recv": null,
                "recvDisable": null,
                "reverse": "disabled",
                "send": "\"default send string\"",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "type": "udp",
                "upInterval": 0
            }
        ]
    }

Retrieve monitor by ID
----------------------

Retrieve information about a specified monitor by monitor ID.

.. code:: javascript

    GET /monitors/{monitorId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [        
            {
                "id": "MON-TCP-80",
                "type": "tcp",
                "address":"any",
                "port": {
                    "type": "equal",
                    "value": 80
                },
                "appService": "none",
                "defaultsFrom": "tcp",
                "description": "none",
                "interval": 5,
                "ipDscp": 0,
                "manualResume": "disabled",
                "partition": "Common",
                "recv": "none",
                "recvDisable": "none",
                "reverse": "disabled",
                "send": "none",
                "timeUntilUp": 0,
                "timeout": 16,
                "transparent": "disabled",
                "upInterval": 0
            }
        ]
    }

Create a monitor
----------------

Add a monitor to the load balancer configuration.

.. code:: javascript

    POST /monitors/{monitorId}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "address": "1.2.3.27",
      "port": {
        "type": "any",
        "value": "85"
      },
      "type": "tcp",
      "defaultsFrom": "/Common/tcp",
      "description": "A updated peg tcp monitor",
      "interval": 5,
      "ipDscp": 0,
      "manualResume": "disabled",
      "recv": "stuff",
      "recvDisable": "disabled",
      "reverse": "disabled",
      "send": null,
      "timeUntilUp": 0,
      "timeout": 0,
      "transparent": "enabled",
      "upInterval": 0
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<monitorId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z"
        }
    }

Update a monitor
----------------

Update a specified monitored configured in the load balancer.

.. code:: javascript

    PUT /monitors/{monitorId}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
        "address": "1.2.3.27",
        "port": {
            "type": "any",
            "value": "86"
        },
        "type": "tcp",
        "defaultsFrom": "/Common/tcp",
        "description": "Updated value",
        "interval": 5,
        "ipDscp": 0,
        "manualResume": "disabled",
        "recv": "stuff",
        "recvDisable": "disabled",
        "reverse": "disabled",
        "send": null,
        "timeUntilUp": 0,
        "timeout": 0,
        "transparent": "enabled",
        "upInterval": 0
    }

Response:
^^^^^^^^^

.. code:: javascript



    {
        "data": {
            "eventId": "32d1ba2a-0edf-4583-8e2c-ab0b54c78193",
            "status": "PROCESSING",
            "resource": "<monitorId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z",
        }
    }

Remove a monitor from the load balancer
---------------------------------------

Remove a specified monitor from the load balancer configuration.

.. code:: javascript

    DELETE /monitors/{monitorId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "data": {
        "eventId": "<eventId:str>",
        "status": "PROCESSING",
        "resource": "<monitorId>",
        "timestamp": "2016-03-24T10:41:08.6194067Z",
        "eventRef": "/events/<eventId:str>"
      }
    }

Retrieve events
---------------

Retrieve all events.

.. code:: javascript

    GET /events

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [{
            "event_id": "<eventId:str>",
            "status": "200",
            "message": "COMPLETED",
            "output": {"virtualId":"sowmyapegtest","Vlans":"["internal"]","message":"virtual/vlan association was updated   Successfully"},
            "ref": "/events/<eventId:str>",
            "entrytimestamp": "2016-03-04T21:29:12",
            "modifiedtimestamp": "2016-03-04T21:29:12"
        }]
    }

Retrieve event by event id
--------------------------

Retrieve event by event id

.. code:: javascript

    GET /events/{eventId}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
        "data": [{
            "event_id": "<eventId:str>",
            "status": "200",
            "message": "COMPLETED",
            "output": {"virtualId":"sowmyapegtest","Vlans":"["internal"]","message":"virtual/vlan association was updated   Successfully"},
            "ref": "/events/<eventId:str>",
            "entrytimestamp": "2016-03-04T21:29:12",
            "modifiedtimestamp": "2016-03-04T21:29:12"
        }]
    }
