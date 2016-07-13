**Endpoint:**
https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant\_id}/f5loadbalancers/{core\_id}

/
-

Retrieve device details like the model number, OS version, cpu stats,
etc...

::

    GET /

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of details.

::

    {
      "data": [{
        "customer": "990036",
        "uptime": "396 days,  9:22",
        "ha_role": "true",
        "links": {
          "vips": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/535908/vips",
            "rel": "related"
          },
          "self": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/535908",
            "rel": "self"
          },
          "device": {
            "href": "https://fe-staging.netsec.rackspace.net/devices/535908",
            "rel": "alternate"
          },
          "lb": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers",
            "rel": "up"
          },
          "nodes": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/535908/nodes",
            "rel": "related"
          },
          "availability": {
            "href": "https://fe-staging.netsec.rackspace.net/loadbalancers/535908/availability",
            "rel": "related"
          }
        },
        "hostname": "535908-lb1.fdaat.rackspace.com",
        "ram_mem": [{
          "total_kbytes": "4158218",
          "free_kbytes": "162846",
          "name": "TMM",
          "used_kbytes": "2860515"
        }],
        "model_name": "BIG-IP 1600",
        "os_version": "11.5.1, build: 3.0.131, edition: Hotfix HF3",
        "management_ip": "10.10.37.142",
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
        "id": "535908"
      }]
    }

GET / 501 response
^^^^^^^^^^^^^^^^^^

Retrieving a list of details is not supported and/or not implemented.

GET / 510 response
^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve all Nodes in the load balancer
---------------------------------------

Nodes are a combination of an IP and a port that process requests
directed from a Pool in a Virtual Server. Nodes can be bound to one or
more Pools.

::

    GET /nodes

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of Nodes

::

    {
        "data": [
            {
                "id": "10.1.2.3",
                "address": "10.1.2.3",
                "appService": "none",
                "connectionLimit": 0,
                "description": "a node",
                "dynamicRatio": 1,
                "logging": "disabled",
                    "metadata": {
                        "href": "https://localhost/f5/10.1.2.3/metadata"
                    },
                "monitors": {
                    "href": "https://localhost/f5/23232/nodes/10.1.2.3/monitors"
                },
                "partition": "Common",
                "rateLimit": "disabled",
                "ratio": 1,
                "session": "user-enabled",
                "state": "unchecked",
                "links": [
                    {
                        "rel": "self",
                        "href": "https://localhost/f5/23232/nodes/10.1.2.3"
                    }
                ]
            }
        ]
    }

GET Nodes 401 response
^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Nodes 501 response
^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of nodes is not supported and/or not implemented.

GET Nodes 510 response
^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Create a Node specified by a Nodes
----------------------------------

Nodes are a combination of an IP and a port that process requests
directed from a Pool in a Virtual Server. Nodes can be bound to one or
more Pools.

::

    POST /nodes

*This operation accepts a request body:*

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

POST Nodes 200 response
^^^^^^^^^^^^^^^^^^^^^^^

Node was created successfully

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

POST Nodes 400 response
^^^^^^^^^^^^^^^^^^^^^^^

Bad request

POST Nodes 401 response
^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST Nodes 403 response
^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST Nodes 500 response
^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Retrieve a list of Node stats in the load balancer
--------------------------------------------------

Retrieve stats for all Nodes in the Node pool.

::

    GET /nodes/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve stats for nodes inside virtual pool.

::

    {
        "data": [
            {
                "id": "my-special-node",
                "address": "11",
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

GET All Nodes Stats 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

Retrieve a Node specified by a Node id
--------------------------------------

Retrieve, update and delete an existing Node specified by a Node id.

::

    GET /nodes/{nodeId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a Node specified by a Node id

::

    {
        "data": [  
            {
                "id": "10.1.2.3",
                "address": "10.1.2.3",
                "appService": "none",
                "connectionLimit": 0,
                "description": "a node",
                "dynamicRatio": 1,
                "logging": "disabled",
                "monitors": {
                  "href": "https://localhost/f5/23232/nodes/10.1.2.3/monitors"
                },
                "metadata": {
                  "href": "https://localhost/f5/23232/nodes/10.1.2.3/metadata"
                },
                "partition": "Common",
                "rateLimit": "disabled",
                "session": "user-enabled",
                "state": "unchecked"
            }
        ]
    }

GET Single Node 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Single Node 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The node requested was not found.

GET Single Node 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific node is not supported and/or not implemented.

GET Single Node 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a Node specified by a Node id
------------------------------------

Retrieve, update and delete an existing Node specified by a Node id.

::

    PUT /nodes/{nodeId}

*This operation accepts a request body:*

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

PUT Single Node 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Node was successfully updated.

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

PUT Single Node 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT Single Node 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT Single Node 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Delete a Node in the load balancer specified by a Node id.
----------------------------------------------------------

Retrieve, update and delete an existing Node specified by a Node id.

::

    DELETE /nodes/{nodeId}

DELETE Single Node 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Node was successfully deleted.

::

    {
      "data": {
        "eventId": "<eventId:str>",
        "resource": "<nodeId:str>",
        "timestamp": "2016-03-08T17:22:33.6349648Z",
        "eventRef": "/events/<eventId:str>"
      }
    }

DELETE Single Node 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE Single Node 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE Single Node 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Retrieve a stats for a Node.
----------------------------

Retrieve stats for a Node.

::

    GET /nodes/{nodeId}/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns stats for the specified Node.

::

    {
        "data": [
            {
                "id": "my-special-node",
                "address": "11",
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

GET Single Node Stats 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Single Node Stats 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of stats is not supported and/or not implemented.

GET Single Node Stats 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve monitor rule associated to a Node.
-------------------------------------------

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    GET /nodes/{nodeId}/monitor-rule

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of what is being monitored for the specified Node.

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

GET Node Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Node Monitor Rule 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The monitor rule requested was not found.

GET Node Monitor Rule 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific monitor rule is not supported and/or not
implemented.

GET Node Monitor Rule 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a Monitor Rule for the specified Node.
---------------------------------------------

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    PUT /nodes/{nodeId}/monitor-rule

*This operation accepts a request body:*

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

PUT Node Monitor Rule 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

PUT Node Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT Node Monitor Rule 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT Node Monitor Rule 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Create monitor rule information for the specified Node.
-------------------------------------------------------

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    POST /nodes/{nodeId}/monitor-rule

*This operation accepts a request body:*

**Request**

::

    {
        "names": [
            "https_443"
        ],
        "minimum": 1
    }

POST Node Monitor Rule 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create monitor rule specified by the node id.

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

POST Node Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST Node Monitor Rule 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST Node Monitor Rule 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Delete Node Monitor Rule
------------------------

Retrieve, update and delete actions on a Node monitor rule specified by
a Node id.

::

    DELETE /nodes/{nodeId}/monitor-rule

DELETE Node Monitor Rule 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete node monitor rule specified by node id

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

DELETE Node Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE Node Monitor Rule 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE Node Monitor Rule 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Retrieve all Pools that have been created in the current Load Balancer.
-----------------------------------------------------------------------

Pools are customizable containers that exist on Load Balancers. Pools
may contain zero or more Nodes. Pools can be bound to one or more
virtuals

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
                "id": "POOL-162.242.187.83-80",
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
                    "href": "http://localhost:8000/f5/535908/pools/POOL-162.242.187.83-80/members"
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
                    "href": "http://localhost:8000/f5/535908/pools/POOL-162.242.187.83-80/members"
                },
                "monitors": {
                    "href": "http://localhost:8000/f5/535908/monitors"
                },
                "links": [
                    {
                        "rel": "self",
                        "href": "https://localhost/f5/232323/pools/test1/POOL-162.242.187.83-80"
                    }
                ]
            }
        ]
    }

GET Pools 401 response
^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Pools 501 response
^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of pools is not supported and/or not implemented.

GET Pools 510 response
^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a list of all stats associated with all Pools in a Load Balancer.
--------------------------------------------------------------------------

Retrieve all stats associated to all Pools that have been created in a
Load Balancer.

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
          "id": "POOL-162.242.187.83-80",
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
          "name": "POOL-162.242.187.83-80",
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
              "href": "https://localhost/f5/232323/pools/POOL-162.242.187.83-80/stats"
            },
            {
              "rel": "pool",
              "href": "https://localhost/f5/232323/pools/POOL-162.242.187.83-80"
            }
          ]
        }
      ]
    }

GET Pools Stats 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Pools Stats 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of stats is not supported and/or not implemented.

GET Pools Stats 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a Pool specified by a Pool id.
---------------------------------------

Retrieve, update and delete on a specified Pool.

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
                "id": "POOL-162.242.187.83-80",
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
                    "href": "https://fe.netsec.rackspace.net/f5/535908/pools/POOL-162.242.187.83-80/metadata"
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
                    "href": "https://fe.netsec.rackspace.net/f5/535908/pools/POOL-162.242.187.83-80/members"
                },
                "monitors": {
                    "href": "http://fe.netsec.rackspace.net/f5/535908/healthmonitors/MON-TCP-80"
                }
            }
        ]
    }

GET Single Pool 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Single Pool 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The pool requested was not found.

GET Single Pool 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific pool is not supported and/or not implemented.

GET Single Pool 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a Pool specified by a Pool id.
-------------------------------------

Retrieve, update and delete on a specified Pool.

::

    PUT /pools/{poolId}

*This operation accepts a request body:*

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

PUT Single Pool 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

PUT Single Pool 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT Single Pool 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT Single Pool 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Delete a Pool specified by a Pool id.
-------------------------------------

Retrieve, update and delete on a specified Pool.

::

    DELETE /pools/{poolId}

DELETE Single Pool 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a Pool specified by a Pool id

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

DELETE Single Pool 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE Single Pool 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE Single Pool 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Retrieve stats for a Pool specified by a Pool id.
-------------------------------------------------

Retrieve all stats associated to this specific Pool.

::

    GET /pools/{poolId}/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of stats.

::

    {
        "data": [
            {
                "id": "POOL-162.242.187.83-80",
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
                "name": "POOL-162.242.187.83-80",
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

GET A Pool Stats 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET A Pool Stats 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of stats is not supported and/or not implemented.

GET A Pool Stats 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a monitor rule for the specified Pool.
-----------------------------------------------

Retrieve a monitor rule associated with this Pool.

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

GET A Pool's Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET A Pool's Monitor Rule 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The monitor-rule requested was not found.

GET A Pool's Monitor Rule 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific monitor-rule is not supported and/or not
implemented.

GET A Pool's Monitor Rule 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a Monitor Rule for the specified Pool.
---------------------------------------------

Retrieve a monitor rule associated with this Pool.

::

    PUT /pools/{poolId}/monitor-rule

*This operation accepts a request body:*

**Request**

::

    {
        "names": [
            "tcp"
        ],
        "minimum": "all"
    }

PUT A Pool's Monitor Rule 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a Monitor Rule for the specified Pool.

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

PUT A Pool's Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT A Pool's Monitor Rule 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT A Pool's Monitor Rule 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Create a Monitor Rule for the specified Pool.
---------------------------------------------

Retrieve a monitor rule associated with this Pool.

::

    POST /pools/{poolId}/monitor-rule

*This operation accepts a request body:*

**Request**

::

    {
        "names": [
            "tcp"
        ],
        "minimum": 1
    }

POST A Pool's Monitor Rule 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a Monitor Rule for the specified Pool.

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

POST A Pool's Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST A Pool's Monitor Rule 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST A Pool's Monitor Rule 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Delete a Monitor Rule for the specified Pool.
---------------------------------------------

Retrieve a monitor rule associated with this Pool.

::

    DELETE /pools/{poolId}/monitor-rule

DELETE A Pool's Monitor Rule 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a Monitor Rule for the specified Pool.

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

DELETE A Pool's Monitor Rule 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE A Pool's Monitor Rule 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE A Pool's Monitor Rule 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve Pool members for the specified Pool id.
------------------------------------------------

Retrieve and create Pool Members within a Pool.

::

    GET /pools/{poolId}/members

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of Pool members.

::

    {
      "data": [
        {
          "id": "162.242.206.181:80",
          "port": {
            "type": "equal",
            "value": 80
          },
          "monitors": {
            "href": "https://fe.netsec.rackspace.net/f5/535908/monitors"
          },
          "address": "162.242.206.181",
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
            "href": "https://fe.netsec.rackspace.net/f5/535908/metadata"
          },
          "profiles": [],
          "links": [
            {
              "rel": "self",
              "href": "https://fe.netsec.rackspace.net/f5/535908/pools/my-pool/members/162.242.206.181:80"
            }
          ]
        }
      ]
    }

GET Pool Members listed in a Pool 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Pool Members listed in a Pool 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

GET Pool Members listed in a Pool 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of members is not supported and/or not implemented.

GET Pool Members listed in a Pool 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Create a new pool member.
-------------------------

Retrieve and create Pool Members within a Pool.

::

    POST /pools/{poolId}/members

*This operation accepts a request body:*

**Request**

::

    {
        "nodeId": "<nodeId>",
        "port": {
            "type": "equal",
            "value": 80
        }
    }

POST Pool Members listed in a Pool 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new pool member by pool id.

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

POST Pool Members listed in a Pool 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST Pool Members listed in a Pool 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST Pool Members listed in a Pool 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a Pool members list of stats.
--------------------------------------

Retrieve a Pool members stats.

::

    GET /pools/{poolId}/members/stats

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a new pool member by pool id.

::

    {
      "data": [
        {
          "id": "test1:80",
          "address": "2.2.2.2",
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
              "href": "https://localhost/f5/232323/pools/test2/members/test1:80/stats"
            }
          ]
        }
      ]
    }

GET Pool Members Stats 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Pool Members Stats 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of stats is not supported and/or not implemented.

GET Pool Members Stats 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a Pool Member from the Pool specified by the Pool id.
--------------------------------------------------------------

Retrieve, update and delete a Pool member specified by a member id.

::

    GET /pools/{poolId}/members/{memberId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

::

    {
        "data": [
            {
                "id": "162.242.206.181:80",
                "address": "162.242.206.181",
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
                    "href": "https://localhost/f5/232323/nodes/162.242.206.181/metadata"
                },
                "monitors": {
                    "href": "https://localhost/f5/232323/nodes/162.242.206.181/monitors"
                },
                "profiles": []
            }
        ]
    }

GET Pool Member 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Pool Member 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a new Pool Member
------------------------

Retrieve, update and delete a Pool member specified by a member id.

::

    PUT /pools/{poolId}/members/{memberId}

*This operation accepts a request body:*

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

PUT Pool Member 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a new pool member by pool id.

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

PUT Pool Member 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT Pool Member 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT Pool Member 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Delete a Pool Member
--------------------

Retrieve, update and delete a Pool member specified by a member id.

::

    DELETE /pools/{poolId}/members/{memberId}

DELETE Pool Member 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a new pool member by pool id.

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

DELETE Pool Member 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE Pool Member 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE Pool Member 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a Pool Member Monitor Rule.
------------------------------------

::

    GET /pools/{poolId}/members/{memberId}/monitor-rule

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a Pool Member Monitor Rule.

::

    {
      "data": [
        {
          "minimum": "all",
          "address": "2.2.2.2",
          "links": [
            {
              "rel": "self",
              "href": "https://fe-staging.netsec.net/f5/232323/pools/ppol1/members/test1:80"
            }
          ]
        }
      ]
    }

GET 401 response
^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET 500 response
^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a Pool Member Monitor Rule.
----------------------------------

::

    PUT /pools/{poolId}/members/{memberId}/monitor-rule

*This operation accepts a request body:*

**Request**

::

    {
        "names": [
            "tcp"
        ],
        "minimum": 1
    }

PUT 200 response
^^^^^^^^^^^^^^^^

Update a Pool Member Monitor Rule.

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

PUT 401 response
^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT 403 response
^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT 500 response
^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
creating a pool member monitor rule

Create a Pool Member Monitor Rule.
----------------------------------

::

    POST /pools/{poolId}/members/{memberId}/monitor-rule

*This operation accepts a request body:*

**Request**

::

    {
      "names": [
        "tcp",
        "https"
      ],
      "minimum": 1
    }

POST 200 response
^^^^^^^^^^^^^^^^^

Create a Pool Member Monitor Rule.

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

POST 401 response
^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST 403 response
^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST 500 response
^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
creating a pool member monitor rule.

Delete a Pool Member's Monitor Rule.
------------------------------------

::

    DELETE /pools/{poolId}/members/{memberId}/monitor-rule

DELETE 200 response
^^^^^^^^^^^^^^^^^^^

Delete a Pool Member Monitor Rule.

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

DELETE 401 response
^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE 403 response
^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE 500 response
^^^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
creating a pool member monitor rule

Retrieve a list of stats.
-------------------------

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
                "address": "2.2.2.2",
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

GET 401 response
^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET 501 response
^^^^^^^^^^^^^^^^

Retrieving a list of stats is not supported and/or not implemented.

GET 510 response
^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a list of all Virtuals in the Load Balancer.
-----------------------------------------------------

Virtuals are a combination of an ip and a port that distributes trafic
among Nodes in a Pool. Virtuals can contain one or more Pools.

::

    GET /virtuals

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve a list of virtuals.

::

    {
        "data": [
            {
                "id": "VIP-162.242.187.83-80",
                "address": "172.16.0.83",
                "addressStatus": "yes",
                "appService": "none",
                "auth": "none",
                "autoLasthop": "default",
                "bwcPolicy": "none",
                "clonePools": "none",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "description": "none",
                "destination": "172.16.0.83:http",
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
                "pools": [
                    {
                        "href": "https://fe.netsec.rackspace.net/f5/535908/pools/POOL-162.242.187.83-80",
                        "rel": "POOL-162.242.187.83-80"
                    }
                ],
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

GET Virtuals 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Virtuals 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of virtuals is not supported and/or not implemented.

GET Virtuals 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Create a new virtual in a load balancer
---------------------------------------

**``address`` is not required, however, if supplied, it will update an
existing Virtual. To create a new virtual, you must not provide an IP or
provide a different port number.**

Virtuals are a combination of an ip and a port that distributes trafic
among Nodes in a Pool. Virtuals can contain one or more Pools.

::

    POST /virtuals

*This operation accepts a request body:*

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

POST Virtuals 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new virtual in a load balancer.

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

POST Virtuals 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST Virtuals 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST Virtuals 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

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
                "destination": "172.16.0.83:80",
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
                "id": "VIP-162.242.187.83-80",
                "name": "VIP-162.242.187.83-80",
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
                "destination": "10.1.2.3:443",
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
                "destination": "172.16.0.83:443",
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
                "id": "VIP-162.242.187.83-443",
                "name": "VIP-162.242.187.83-443",
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

GET Virtual Stats 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Virtual Stats 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of virtuals stats is not supported and/or not
implemented.

GET Virtual Stats 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

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
                "id": "VIP-162.242.187.83-80",
                "address": "172.16.0.83",
                "addressStatus": "yes",
                "appService": "none",
                "auth": "none",
                "autoLasthop": "default",
                "bwcPolicy": "none",
                "clonePools": "none",
                "cmpEnabled": "yes",
                "connectionLimit": 0,
                "description": "none",
                "destination": "172.16.0.83:http",
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
                "pools": [
                    {
                        "href": "https://fe.netsec.rackspace.net/f5/535908/pools/POOL-162.242.187.83-80",
                        "rel": "POOL-162.242.187.83-80"
                    }
                ],
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

GET A Virtual 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET A Virtual 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

The virtual requested was not found.

GET A Virtual 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific virtual is not supported and/or not implemented.

GET A Virtual 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a virtual in a load balancer specified by virtual id
-----------------------------------------------------------

**``address`` is required in order to make an update on the existing
virtual.**

Retrieve, update and delete a Virtual in a Load Balancer specified by a
Virtual id.

::

    PUT /virtuals/{virtualId}

*This operation accepts a request body:*

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

PUT A Virtual 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a virtual in a load balancer specified by virtual id

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

PUT A Virtual 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT A Virtual 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT A Virtual 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Delete a virtual in a load balancer specified by virtual id.
------------------------------------------------------------

Retrieve, update and delete a Virtual in a Load Balancer specified by a
Virtual id.

::

    DELETE /virtuals/{virtualId}

DELETE A Virtual 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a virtual in a load balancer specified by virtual id.

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

DELETE A Virtual 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE A Virtual 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE A Virtual 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

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

GET Virtual Traffic Classes 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Virtual Traffic Classes 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The traffic classes requested was not found.

GET Virtual Traffic Classes 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific traffic classes is not supported and/or not
implemented.

GET Virtual Traffic Classes 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

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

GET Single Virtual Persists 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Single Virtual Persists 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The persists requested were not found.

GET Single Virtual Persists 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific persist is not supported and/or not implemented.

GET Single Virtual Persists 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a Virtual Persists.
--------------------------

Payload Properites

\| Attribute \| Type \| Possible Value(s) \| Required \| \| ----------
\| ---- \| --------------- \| -------- \| \| names \| String \| Any
valid string \| True \| *All string values are case sensitive*

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

::

    PUT /virtuals/{virtualId}/persists

*This operation accepts a request body:*

**Request**

::

    {
        "names": [
            "hash"
        ]
    }

PUT Single Virtual Persists 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

PUT Single Virtual Persists 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT Single Virtual Persists 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT Single Virtual Persists 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
updating a Virtual Persists.

Create a Virtual Persists in the F5 load balancer
-------------------------------------------------

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

::

    POST /virtuals/{virtualId}/persists

*This operation accepts a request body:*

**Request**

::

    {
        "names": [
            "source_addr",
            "dest_addr"
        ]
    }

POST Single Virtual Persists 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

POST Single Virtual Persists 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST Single Virtual Persists 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST Single Virtual Persists 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
creating a Virtual Persists

Delete a Virtual Persists in the F5 load balancer
-------------------------------------------------

Retrieve, update and delete a single Virtual's persists in the Load
Balancer.

::

    DELETE /virtuals/{virtualId}/persists

DELETE Single Virtual Persists 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

DELETE Single Virtual Persists 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE Single Virtual Persists 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE Single Virtual Persists 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
deleting a Virtual Persists.

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
                "destination": "172.16.0.83:80",
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
                "id": "VIP-162.242.187.83-80",
                "name": "VIP-162.242.187.83-80",
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
                "destination": "10.1.2.3:443",
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
                "destination": "172.16.0.83:443",
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
                "id": "VIP-162.242.187.83-443",
                "name": "VIP-162.242.187.83-443",
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

GET A Virtual's Stats 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET A Virtual's Stats 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of stats is not supported and/or not implemented.

GET A Virtual's Stats 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

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

GET Virtual Auth 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Virtual Auth 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The auth requested was not found.

GET Virtual Auth 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific auth is not supported and/or not implemented.

GET Virtual Auth 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve a Virtual's Vlans specified by a Virtual id.
-----------------------------------------------------

Retrieve, update and delete a Virtual's Vlans in the Load Balancer.

::

    GET /virtuals/{virtualId}/vlans

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the vlan specified.

::

    {
        "data": [
            {
                "names": [
                    "secure-vlan",
                    "read-vlan"
                ]
            }
        ]
    }

GET A Virtual's Vlans 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET A Virtual's Vlans 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The vlan requested was not found.

GET A Virtual's Vlans 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific vlan is not supported and/or not implemented.

GET A Virtual's Vlans 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a vlan specified by a Virtual id.
----------------------------------------

Retrieve, update and delete a Virtual's Vlans in the Load Balancer.

::

    PUT /virtuals/{virtualId}/vlans

*This operation accepts a request body:*

**Request**

::

    {
       "names": [
          "external"
        ]
    }

PUT A Virtual's Vlans 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a vlan specified by a Virtual id.

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

PUT A Virtual's Vlans 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT A Virtual's Vlans 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT A Virtual's Vlans 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
updating a specific vlan.

Create a vlan in the F5 load balancer.
--------------------------------------

Retrieve, update and delete a Virtual's Vlans in the Load Balancer.

::

    POST /virtuals/{virtualId}/vlans

*This operation accepts a request body:*

**Request**

::

    {
       "names": [
          "internal",
          "external"
        ]
    }

POST A Virtual's Vlans 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a vlan in the F5 load balancer.

::

    {
        "data": {
            "eventId": "e5f5a509-9466-4777-abf2-6fa909941223c",
            "status": "PROCESSING",
            "resource": "<virtualId:str>",
            "timestamp": "2016-03-08T17:22:33.6249648Z",
            "eventRef": "/events/<eventId:str>"
        }
    }

POST A Virtual's Vlans 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST A Virtual's Vlans 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST A Virtual's Vlans 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
creating a specific vlan.

Delete a vlan in the F5 load balancer specified by a Virtual id.
----------------------------------------------------------------

Retrieve, update and delete a Virtual's Vlans in the Load Balancer.

::

    DELETE /virtuals/{virtualId}/vlans

DELETE A Virtual's Vlans 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a vlan in the F5 load balancer specified by a Virtual id.

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

DELETE A Virtual's Vlans 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE A Virtual's Vlans 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE A Virtual's Vlans 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The server encountered an unexpected condition which prevented it from
deleting a specific vlan.

Retrieve a Virtual Pool specified by a Virtual id.
--------------------------------------------------

Retrieve an existing Virtual Pool specified by a Virtual id in the Load
Balancer.

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
                        "href": "http://localhost:8000/f5/535908/virtuals/VIP-162.242.187.83-80/pool/"
                    }
                }
            } 
        ]
    }

GET A Virtual Pool 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET A Virtual Pool 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of pools is not supported and/or not implemented.

GET A Virtual Pool 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve all Monitors in Load Balancer.
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
                "address" : "10.1.1.1",
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
                "address" : "10.1.1.2",
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
                "address" : "10.1.1.3",
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

GET Monitors 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Monitors 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a list of monitors is not supported and/or not implemented.

GET Monitors 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

A monitor
---------

Retrieve, create, update and delete a monitor in a Load Balancer
specified by a monitor id.

::

    GET /monitors/{monitorId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Retrieve the monitor specified.

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

GET A monitor 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET A monitor 404 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

The monitor requested was not found.

GET A monitor 501 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Retrieving a specific monitor is not supported and/or not implemented.

GET A monitor 510 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Update a Monitor in the Load Balancer.
--------------------------------------

Retrieve, create, update and delete a monitor in a Load Balancer
specified by a monitor id.

::

    PUT /monitors/{monitorId}

*This operation accepts a request body:*

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

PUT A monitor 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Update a new monitor in the load balancer.

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

PUT A monitor 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

PUT A monitor 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

PUT A monitor 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Create a new monitor in the load balancer.
------------------------------------------

Retrieve, create, update and delete a monitor in a Load Balancer
specified by a monitor id.

::

    POST /monitors/{monitorId}

*This operation accepts a request body:*

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

POST A monitor 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create a new monitor in the load balancer.

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

POST A monitor 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

POST A monitor 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

POST A monitor 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Delete a Monitor in load balancer
---------------------------------

Retrieve, create, update and delete a monitor in a Load Balancer
specified by a monitor id.

::

    DELETE /monitors/{monitorId}

DELETE A monitor 200 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete a new monitor in the load balancer.

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

DELETE A monitor 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

DELETE A monitor 403 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

User doesn't have the required role.

DELETE A monitor 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error.

Retrieve all events.
--------------------

Retrieve all events.

::

    GET /events

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns a list of events

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

GET Events 401 response
^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Events 500 response
^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error

Retrieve an Event with an event id.
-----------------------------------

Retrieve a single Event provided an event id

::

    GET /events/{eventId}

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Returns a single Event provided an event id

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

GET Single Event 401 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bad or expired token. To fix, you should re-authenticate the user.

GET Single Event 500 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An indeterminate error occurred. This is caused by an unexpected error
