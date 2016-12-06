**Endpoint:**
https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant\_id}/f5loadbalancers/{core\_id}

Retrieve load balancer details
------------------------------

Retrieve load balancer information like the model number, OS version,
CPU statistics, and so on.

::

    GET /

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve device information.

::

    {
      "data": [{
        "customer": "1234567",
        "uptime": "396 days,  9:22",
        "ha_role": "true",
        "links": {
          "vips": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/1234567/vips",
            "rel": "related"
          },
          "self": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/1234567",
            "rel": "self"
          },
          "device": {
            "href": "https://fe-staging.netsec.rackspace.net/devices/1234567",
            "rel": "alternate"
          },
          "lb": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers",
            "rel": "up"
          },
          "nodes": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/1234567/nodes",
            "rel": "related"
          },
          "availability": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/1234567/availability",
            "rel": "related"
          }
        },
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

Retrieve all nodes that have been configured in the load balancer.
------------------------------------------------------------------

Nodes are a combination of an IP and a port that process requests
directed from a Pool in a Virtual Server. Nodes can be bound to one or
more Pools.

::

    GET /nodes

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of nodes

::

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
                    "metadata": {
                        "href": "https://localhost/f5/127.0.0.1/metadata"
                    },
                "monitors": {
                    "href": "https://localhost/f5/12345/nodes/127.0.0.1/monitors"
                },
                "partition": "Common",
                "rateLimit": "disabled",
                "ratio": 1,
                "session": "user-enabled",
                "state": "unchecked",
                "links": [
                    {
                        "rel": "self",
                        "href": "https://localhost/f5/12345/nodes/127.0.0.1"
                    }
                ]
            }
        ]
    }

Create a node.
--------------

You can use the event ID returned in the API response to submit an event
request to verify that the operation completed and get the ID for the
new node.

Nodes are a combination of an IP and a port that process requests
directed from a Pool in a Virtual Server. Nodes can be bound to one or
more Pools.

::

    POST /nodes

**Request**

::

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

POST Nodes response
^^^^^^^^^^^^^^^^^^^

The node was created successfully.

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "Nodes",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve statistics for each node in the load balancer. You
-----------------------------------------------------------

can use links in the response to retrieve information about a specific
node.

Retrieve statistics for all nodes that were added to the load balancer.

::

    GET /nodes/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve statistics for nodes configured in the load balancer.

::

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
                "totRequests": 3,
                "links": [
                    {
                        "ref": "self",
                        "href": "https://localhost/f5/232323/nodes/my-special-node/stats"
                    },
                    {
                        "rel": "node",
                        "href": "https://localhost/f5/232323/nodes/my-special-node"
                    }
                ]
            }
        ]
    }

Retrieve node information by node ID.
-------------------------------------

Retrieve, update and delete an existing Node specified by a Node id.

::

    GET /nodes/{nodeId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns information about the node associated with the node ID.

::

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
                "monitors": {
                  "href": "https://localhost/f5/12345/nodes/127.0.0.1/monitors"
                },
                "metadata": {
                  "href": "https://localhost/f5/12345/nodes/127.0.0.1/metadata"
                },
                "partition": "Common",
                "rateLimit": "disabled",
                "session": "user-enabled",
                "state": "unchecked"
            }
        ]
    }

Change description and configuration settings for an
----------------------------------------------------

existing node. You need the node ID to complete this operation.

Retrieve, update and delete an existing Node specified by a Node id.

::

    PUT /nodes/{nodeId}

**Request**

::

    {
        "address": "162.242.206.208",
        "appService": null,
        "connectionLimit": 2,
        "description": "Updated node",
        "dynamicRatio": 11,
        "logging": "enabled",
        "rateLimit": "disabled",
        "ratio": 1
    }

PUT Node response
^^^^^^^^^^^^^^^^^

The node was successfully updated.

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<nodeId:str>",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove a node from the load balancer configuration. You need
------------------------------------------------------------

the node ID to complete this operation.

Retrieve, update and delete an existing Node specified by a Node id.

::

    DELETE /nodes/{nodeId}

DELETE Node response
^^^^^^^^^^^^^^^^^^^^

The node was successfully deleted.

::

    {
      "data": {
        "eventId": "<eventId:str>",
        "resource": "<nodeId:str>",
        "timestamp": "2016-03-08T17:22:33.6349648Z",
        "eventRef": "/events/<eventId:str>"
      }
    }

Retrieve information about availability, session status,
--------------------------------------------------------

monitor rules for the device with the specified node ID.

Retrieve statistics for a specified node.

::

    GET /nodes/{nodeId}/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns statistics for the specified node.

::

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

Retrieve information about the monitorng rule associated
--------------------------------------------------------

with a specified node.

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    GET /nodes/{nodeId}/monitor-rule

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve monitor settings for the specified Node.

::

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

Update a monitor rule on the specified node.
--------------------------------------------

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    PUT /nodes/{nodeId}/monitor-rule

**Request**

::

    {
        "names": [
            "https_443",
            "real_server",
            "tcp_echo"
        ],
        "minimum": 1
    }

PUT Node monitor rule response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update node monitor rule specified by node id

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<nodeId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Add a monitor rule to automate checks
-------------------------------------

on a specified node. To find the names of the available monitors, submit
a ``GET monitors`` request.

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    POST /nodes/{nodeId}/monitor-rule

**Request**

::

    {
        "names": [
            "https_443"
        ],
        "minimum": 1
    }

POST Node monitor rule response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Apply monitor rule to the specified node.

::

    {
      "data": {
        "eventId": "<eventId:str>",
        "status": "PROCESSING",
        "resource": "<nodeId:str>"
        "eventRef": "/events/<eventId:str>",
        "timestamp": "2016-03-18T03:18:35.5077939Z"
      }
    }

Remove monitor rule from a specified node.
------------------------------------------

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    DELETE /nodes/{nodeId}/monitor-rule

DELETE Node monitor rule response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete the monitor rule from the specified node.

::

    {
        "data" : {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve all pools created in the current load balancer.
--------------------------------------------------------

Pools are customizable containers configured on load balancers to
specify the backend devices (nodes) for managing web traffic. Each pool
can contain zero or more nodes, known as a pool member. Pools can be
bound to one or more virtual servers.

::

    GET /pools

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of pools.

::

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
                "metadata": {
                    "href": "http://localhost:8000/f5/12345/pools/POOL-127.0.0.1-80/members"
                },
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
                "members": {
                    "href": "http://localhost:8000/f5/12345/pools/POOL-127.0.0.1-80/members"
                },
                "monitors": {
                    "href": "http://localhost:8000/f5/12345/monitors"
                },
                "links": [
                    {
                        "rel": "self",
                        "href": "https://localhost/f5/12345/pools/test1/POOL-127.0.0.1-80"
                    }
                ]
            }
        ]
    }

Retrieve a list of all stats associated with all Pools in a Load Balancer.
--------------------------------------------------------------------------

Retrieve all statitistics associated to all pools that have been created
in a load balancer.

::

    GET /pools/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of stats.

::

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
          },
          "links": [
            {
              "rel": "self",
              "href": "https://localhost/f5/12345/pools/POOL-127.0.0.1-80/stats"
            },
            {
              "rel": "pool",
              "href": "https://localhost/f5/12345/pools/POOL-162.242.187.83-80"
            }
          ]
        }
      ]
    }

Retrieve a Pool specified by a Pool id.
---------------------------------------

Manage a pool, Retrieve, update and delete specified Pool.

::

    GET /pools/{poolId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the pool specified.

::

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
                "metadata": {
                    "href": "https://fe.netsec.rackspace.net/f5/12345/pools/POOL-127.0.0.1-80/metadata"
                },
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
                "members": {
                    "href": "https://fe.netsec.rackspace.net/f5/12345/pools/POOL-127.0.0.1-80/members"
                },
                "monitors": {
                    "href": "http://fe.netsec.rackspace.net/f5/12345/healthmonitors/MON-TCP-80"
                }
            }
        ]
    }

Update a Pool specified by a Pool id.
-------------------------------------

Manage a pool, Retrieve, update and delete specified Pool.

::

    PUT /pools/{poolId}

**Request**

::

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

PUT Single pool response
^^^^^^^^^^^^^^^^^^^^^^^^

Update a Pool specified by a Pool id

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-24T10:41:08.6194067Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Remove a specified pool from the load balancer configuration.
-------------------------------------------------------------

Manage a pool, Retrieve, update and delete specified Pool.

::

    DELETE /pools/{poolId}

DELETE Single pool response
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a pool specified by a Pool id

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-24T10:41:08.6194067Z",
        }
    }

Retrieve statistics for each pool member in a specified pool
------------------------------------------------------------

including configuration settings, availability and monitoring status.
The response includes links to access a detail view for each member.
responses: 200: description: \| Successfully retrieved statistics for
pool members. body: application/json: schema: !include
schemas/get\_pools\_poolid\_stats.sample example: !include
examples/get\_pools\_poolid\_stats.sample

::

    GET /pools/{poolId}/stats

Retrieve a monitor rule for the specified pool
----------------------------------------------

Retrieve a monitor rule associated with a specified pool.

::

    GET /pools/{poolId}/monitor-rule

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the monitor-rule specified.

::

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

Update a monitor rule for the specified pool.
---------------------------------------------

Retrieve a monitor rule associated with a specified pool.

::

    PUT /pools/{poolId}/monitor-rule

**Request**

::

    {
        "names": [
            "tcp"
        ],
        "minimum": "all"
    }

PUT Pool monitor rule response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a monitor Rule for the specified Pool.

::

    {
        "data": {
            "eventId": "<eventId:str)",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-16T17:09:53.1059638Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Add a monitor rule to automate checks
-------------------------------------

on a specified node. To find the names of the available monitors, submit
a ``GET monitors`` request.

Retrieve a monitor rule associated with a specified pool.

::

    POST /pools/{poolId}/monitor-rule

**Request**

::

    {
        "names": [
            "tcp"
        ],
        "minimum": 1
    }

POST Pool monitor rule response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a monitor rule for the specified pool.

::

    {
      "data": {
        "eventId": "<eventId:str>",
        "status": "PROCESSING",
        "timestamp": "2016-03-18T03:18:35.5077939Z",
        "resource": "<poolId:str>",
        "eventRef": "/events/<eventId:str>"
      }
    }

Delete a monitor rule for the specified pool.
---------------------------------------------

Retrieve a monitor rule associated with a specified pool.

::

    DELETE /pools/{poolId}/monitor-rule

DELETE Pool monitor rule response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a monitor rule for the specified pool.

::

    {
        "data": {
            "eventId": "<eventId:str]",
            "status": "PROCESSING",
            "resource": "<poolId:str>",
            "timestamp": "2016-03-16T17:09:53.1059638Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve pool members for the specified pool ID.
------------------------------------------------

Retrieve and create pool members within a specified pool.

::

    GET /pools/{poolId}/members

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of members associated with a specific pool ID.

::

    {
      "data": [
        {
          "id": "127.0.0.1:80",
          "port": {
            "type": "equal",
            "value": 80
          },
          "monitors": {
            "href": "https://fe.netsec.rackspace.net/f5/12345/monitors"
          },
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
          "metadata": {
            "href": "https://fe.netsec.rackspace.net/f5/12345/metadata"
          },
          "profiles": [],
          "links": [
            {
              "rel": "self",
              "href": "https://fe.netsec.rackspace.net/f5/12345/pools/my-pool/members/127.0.0.1:80"
            }
          ]
        }
      ]
    }

Creates a pool member by adding an existing node to a
-----------------------------------------------------

specified pool.

Retrieve and create pool members within a specified pool.

::

    POST /pools/{poolId}/members

**Request**

::

    {
        "nodeId": "<nodeId>",
        "port": {
            "type": "equal",
            "value": 80
        }
    }

POST Pool members response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Added pool member to the specified pool.

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "resource": "<poolId:str>",
            "type": "<memberId:str>",
            "timestamp": "2016-03-17T09:36:42.5274609Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve statistics for a specific pool member in a
---------------------------------------------------

specified pool including configuration settings, availability and
monitoring status.

::

    GET /pools/{poolId}/members/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully returned pool member statistics.

::

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
          "totRequests": 0,
          "links": [
            {
              "rel": "self",
              "href": "https://localhost/f5/12345/pools/test2/members/test1:80/stats"
            }
          ]
        }
      ]
    }

Retrieve configuration, monitor settings, and other
---------------------------------------------------

data for a pool member.eee

Retrieve, update and delete a pool member specified by a member id.

::

    GET /pools/{poolId}/members/{memberId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

::

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
                "metadata": {
                    "href": "https://localhost/f5/12345/nodes/127.0.0.1/metadata"
                },
                "monitors": {
                    "href": "https://localhost/f5/12345/nodes/127.0.0.1/monitors"
                },
                "profiles": []
            }
        ]
    }

Update configuration settings for a specified pool
--------------------------------------------------

member

Retrieve, update and delete a pool member specified by a member id.

::

    PUT /pools/{poolId}/members/{memberId}

**Request**

::

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

PUT Pool member response
^^^^^^^^^^^^^^^^^^^^^^^^

Update a pool member by pool id.

::

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

Remove a pool member from the specified pool.
---------------------------------------------

Retrieve, update and delete a pool member specified by a member id.

::

    DELETE /pools/{poolId}/members/{memberId}

DELETE Pool member response
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a pool member by pool id.

::

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

Retrieves configuration settings for the monitor
------------------------------------------------

rule applied to a specified pool member

Retrieve, add, update and delete monitor rule for a pool member

::

    GET /pools/{poolId}/members/{memberId}/monitor-rule

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a pool member monitor rule.

::

    {
      "data": [
        {
          "minimum": "all",
          "address": "127.0.0.1",
          "links": [
            {
              "rel": "self",
              "href": "https://fe-staging.netsec.net/f5/12345/pools/ppol1/members/test1:80"
            }
          ]
        }
      ]
    }

Update the configuration settings for a
---------------------------------------

monitor rule applied to a specified pool member

Retrieve, add, update and delete monitor rule for a pool member

::

    PUT /pools/{poolId}/members/{memberId}/monitor-rule

**Request**

::

    {
        "names": [
            "tcp"
        ],
        "minimum": 1
    }

PUT Manage monitor rule for a pool member response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns event information for the update monitor rule request. Use the
event ID to get event status and output information.

::

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

Add a monitor to a pool member in the specified
-----------------------------------------------

pool.

Retrieve, add, update and delete monitor rule for a pool member

::

    POST /pools/{poolId}/members/{memberId}/monitor-rule

**Request**

::

    {
      "names": [
        "tcp",
        "https"
      ],
      "minimum": 1
    }

POST Manage monitor rule for a pool member response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a pool Member Monitor Rule.

::

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

Remove the monitor rule applied to a specified
----------------------------------------------

pool member (``memberId``) in a specified pool (``poolId``).

Retrieve, add, update and delete monitor rule for a pool member

::

    DELETE /pools/{poolId}/members/{memberId}/monitor-rule

DELETE Manage monitor rule for a pool member response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Returns event information for the update monitor rule request. Use the
event ID to get event status and output information.

::

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

Retrieve a list of statistics
-----------------------------

::

    GET /pools/{poolId}/members/{memberId}/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of stats.

::

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

Retrieve details about virtuals configured in the load balancer
---------------------------------------------------------------

including configuration data and status information.

Virtuals define virtual server configurations in the load balancer. Each
configuration specifies the port and ip to route web traffic to the load
balancer and distribute it among the backend devices configured in a
load balancer pool. Virtuals can be associated with one or more pools.

::

    GET /virtuals

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns detailed information about each virtual server configured in the
load balancer.

::

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
                "pool": {
                    "href": "https://fe.netsec.rackspace.net/f5/12345/pools/POOL-127.0.0.1-80"
                },
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
                "vlans": "none",
                "vlansDisabled": "vlans-disabled",
                "vsIndex": 7
            } 
        ]
    }

Add a virtual server configuration to the load balancer. When you
-----------------------------------------------------------------

add the not need to supply an include the **``address`` is not required,
however, if supplied, it will update an existing Virtual. To create a
new virtual, you must not provide an IP or provide a different port
number.**

Virtuals define virtual server configurations in the load balancer. Each
configuration specifies the port and ip to route web traffic to the load
balancer and distribute it among the backend devices configured in a
load balancer pool. Virtuals can be associated with one or more pools.

::

    POST /virtuals

**Request**

::

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

POST Virtuals response
^^^^^^^^^^^^^^^^^^^^^^

Returns event information for the request. Use the event ID to get event
status and output information.

::

    {
      "data": {
        "eventId": "02d1ba2a-0edf-4583-8e2c-ab0b54c78193",
        "status": "PROCESSING",
        "resource": "Virtuals",
        "eventRef": "/events/<eventId:str>",
        "timestamp": "2016-03-18T03:18:35.5077939Z"
      }
    }

Retrieve a list of stats for all Virtuals in the Load Balancer.
---------------------------------------------------------------

Retrieve a list of stats for all Virtuals in the Load Balancer.

::

    GET /virtuals/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of stats for all Virtuals in the Load Balancer.

::

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

Retrieve a Virtual in a Load Balancer specified by a Virtual id.
----------------------------------------------------------------

Retrieve, update and delete a Virtual in a Load Balancer specified by a
Virtual id.

::

    GET /virtuals/{virtualId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the Virtual specified.

::

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
                "pool": {
                    "href": "https://fe.netsec.rackspace.net/f5/12345/pools/POOL-127.0.0.1-80"
                },
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
                "vlans": "none",
                "vlansDisabled": "vlans-disabled",
                "vsIndex": 7
            }
        ]
    }

Update a virtual in a load balancer specified by virtual id
-----------------------------------------------------------

**``address`` and port are required in order to make an update on the
existing virtual.**

Retrieve, update and delete a Virtual in a Load Balancer specified by a
Virtual id.

::

    PUT /virtuals/{virtualId}

**Request**

::

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

PUT A Virtual response
^^^^^^^^^^^^^^^^^^^^^^

Returns event information for the request. Use the event ID to get event
status and output information.

::

    {
        "data": {
            "eventId": "02d1ba2a-0edf-4583-8e2c-ab0b54c78193",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z"
        }
    }

Delete a virtual in a load balancer specified by virtual id.
------------------------------------------------------------

Retrieve, update and delete a Virtual in a Load Balancer specified by a
Virtual id.

::

    DELETE /virtuals/{virtualId}

DELETE A Virtual response
^^^^^^^^^^^^^^^^^^^^^^^^^

Returns event information for the request. Use the event ID to get event
status and output information.

::

    {
        "data": {
            "eventId": "<eventid:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Retrieve Virtual's Traffic Classes
----------------------------------

Retrieve, update and delete Virtual traffic classes in the Load
Balancer.

**Has not been implemented**

::

    GET /virtuals/{virtualId}/traffic-classes

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the traffic classes specified.

::

    {
        "data": [
            {
                "names": [
                    "local-trafficClass"
                ]
            }
        ]
    }

Retrieve a single Virtual's persists.
-------------------------------------

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

::

    GET /virtuals/{virtualId}/persists

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the persists specified.

::

    {
        "data": [
            {
              "profileName": "my-cool-persist"
            }

        ]
    }

Update a Virtual Persists.
--------------------------

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

::

    PUT /virtuals/{virtualId}/persists

**Request**

::

    {
        "names": [
            "hash"
        ]
    }

PUT Single Virtual Persists response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a Virtual Persists in the F5 load balancer.

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Create a Virtual Persists in the F5 load balancer
-------------------------------------------------

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

::

    POST /virtuals/{virtualId}/persists

**Request**

::

    {
        "names": [
            "source_addr",
            "dest_addr"
        ]
    }

POST Single Virtual Persists response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a Virtual Persists in the F5 load balancer.

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

Delete a Virtual Persists in the F5 load balancer
-------------------------------------------------

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

::

    DELETE /virtuals/{virtualId}/persists

DELETE Single Virtual Persists response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a Virtual Persists in the F5 load balancer.

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z"
        }
    }

Retrieve stats for a Virtual specified by a Virtual id.
-------------------------------------------------------

Retrieve stats for a Virtual specified by a Virtual id in the Load
Balancer.

::

    GET /virtuals/{virtualId}/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of stats.

::

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

Retrieve a Virtual's auth specified by a Virtual id.
----------------------------------------------------

Retrieve, update and delete a Virtual's Auth in the Load Balancer.

**Has not been implemented**

::

    GET /virtuals/{virtualId}/auth

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the auth specified.

::

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

Retrieve a virtual pool specified by the virtual pool specified by pool
ID.

::

    GET /virtuals/{virtualId}/pool

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of pools.

::

    {
        "data": [
            {
                "name": "test_pool",
                "_links": {
                    "self": {
                        "href": "http://localhost:8000/f5/12345/virtuals/VIP-127.0.0.1-80/pool/"
                    }
                }
            } 
        ]
    }

Retrieve all monitors in load balancer.
---------------------------------------

Monitors verify the health and availability of a Node, a Pool, or group
of Nodes in a Pool.

::

    GET /monitors

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of monitors.

::

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

Monitor
-------

Retrieve, create, update and delete a monitor in a load balancer
specified by a monitor id.

::

    GET /monitors/{monitorId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve details about a specified monitor.

::

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

Update a monitor in the load balancer.
--------------------------------------

Retrieve, create, update and delete a monitor in a load balancer
specified by a monitor id.

::

    PUT /monitors/{monitorId}

**Request**

::

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

PUT Monitor response
^^^^^^^^^^^^^^^^^^^^

Update a monitor in the load balancer.

::


    {
        "data": {
            "eventId": "32d1ba2a-0edf-4583-8e2c-ab0b54c78193",
            "status": "PROCESSING",
            "resource": "<monitorId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z",
        }
    }

Create a monitor
----------------

Retrieve, create, update and delete a monitor in a load balancer
specified by a monitor id.

::

    POST /monitors/{monitorId}

**Request**

::

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

POST Monitor response
^^^^^^^^^^^^^^^^^^^^^

Add a monitor to the load balancer configuration.

::

    {
        "data": {
            "eventId": "<eventId:str>",
            "status": "PROCESSING",
            "resource": "<monitorId:str>",
            "eventRef": "/events/<eventId:str>",
            "timestamp": "2016-03-18T03:18:35.5077939Z"
        }
    }

Remove a monitor from the load balancer configuration
-----------------------------------------------------

Retrieve, create, update and delete a monitor in a load balancer
specified by a monitor id.

::

    DELETE /monitors/{monitorId}

DELETE Monitor response
^^^^^^^^^^^^^^^^^^^^^^^

Delete monitor from the load balancer configuration.

::

    {
      "data": {
        "eventId": "<eventId:str>",
        "status": "PROCESSING",
        "resource": "<monitorId>",
        "timestamp": "2016-03-24T10:41:08.6194067Z",
        "eventRef": "/events/<eventId:str>"
      }
    }

Retrieve all events
-------------------

Retrieve all events.

::

    GET /events

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns information about events logged in the system log files.

::

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

Retrieve event by event id.
---------------------------

Retrieve event information by event ID.

::

    GET /events/{eventId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns information about the event with the specified ID.

::

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
