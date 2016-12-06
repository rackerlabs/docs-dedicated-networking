Retrieve device information
---------------------------

Use the device ID operation to get complete information about the device
with the specified ID including associated customer, usage statistics,
and configuration details for nodes, virtual IPs, and high availability.

::

    GET /{device_id}

*This operation does not accept a request body.*

Response
^^^^^^^^^

::

    {
      "load_balancer_data": {
        "customer": "2222222",
        "uptime": "unimplemented",
        "hostname": "adx1000-cyberdyne.iad3.netdev.net",
        "links": {
          "device": {
            "href": "https://api-qual.netsec.rackspace.net/devices/111111",
            "rel": "alternate"
          },
          "lb": {
            "href": "https://api-qual.netsec.rackspace.net/loadbalancers",
            "rel": "up"
          },
          "self": {
            "href": "https://api-qual.netsec.rackspace.net/loadbalancers/111111",
            "rel": "self"
          },
          "vips": {
            "href": "https://api-qual.netsec.rackspace.net/loadbalancers/111111/vips",
            "rel": "related"
          },
          "nodes": {
            "href": "https://api-qual.netsec.rackspace.net/loadbalancers/111111/nodes",
            "rel": "related"
          }
        },
        "ha_role": "high",
        "ram_mem": [
          {
            "total_kbytes": "2097152",
            "free_kbytes": "1339548",
            "name": "MP",
            "used_kbytes": "757604"
          },
          {
            "total_kbytes": "458752",
            "free_kbytes": "348964",
            "name": "BP1",
            "used_kbytes": "109788"
          }
        ],
        "id": "111111",
        "os_version": "12.4.00sT403",
        "management_ip": "10.17.25.108",
        "role": "unimplemented",
        "cpu_load": [
          {
            "mod_name": "MASTER_CPU",
            "load_5_sec_avg": {
              "percent_load": 1,
              "seconds_since": 5
            }
          },
          {
            "mod_name": "ASB1/1",
            "load_5_sec_avg": {
              "percent_load": 1,
              "seconds_since": 5
            }
          },
          {
            "mod_name": "ASB1/2",
            "load_5_sec_avg": {
              "percent_load": 1,
              "seconds_since": 5
            }
          },
          {
            "mod_name": "ASB1/3",
            "load_5_sec_avg": {
              "percent_load": 1,
              "seconds_since": 5
            }
          },
          {
            "mod_name": "ASB1/4",
            "load_5_sec_avg": {
              "percent_load": 1,
              "seconds_since": 5
            }
          }
        ],
        "ha_status": "none",
        "model_name": "SI-1216-4-PREM"
      }
    }


Retrieve load balancer configuration details
--------------------------------------------

Retrieves the load balancer configuration information for the specified
device ID.

::

    GET /{device_id}/configuration

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

::

    {
      "load_balancer_data": {
        "b64": "key"
      }
    }

Show high availability template
-------------------------------

Retrieves the high availability configuration template for a device with
the specified ID.

::

    GET /{device_id}/ha

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

::

    {
      "message": "This is a test template for High Availability"
    }

Retrieve virtual IPs configuration
----------------------------------

Load balancers must have at least one virtual IP address that clients
can use to balance traffic across nodes. You can use the manage virtual
IPs operations to configure and manage the virtual IP addresses for the
load balancer with the specified device ID.

An IP can be passed into the add Virtual IP call as part of the request
body, only if the IP exists within an existing Virtual.

*When adding a Virtual IP, these fields are required: account\_number,
label, protocol, port, algorithm, persistence, admin\_state, comment*

::

    GET /{device_id}/vips

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

::

    {
      "vips": [
        {
          "protocol": "TCP",
          "description": "",
          "algorithm": {
            "name": "LEAST_CONNECTION",
            "persistence": null
          },
          "ip": "152.181.84.2",
          "runtime_state": "UNHEALTHY",
          "label": "Vip-Test-32fce25d",
          "port_number": 80,
          "port_name": "HTTP",
          "admin_state": "ENABLED",
          "stats": {
            "conn_max": -1,
            "pkts_out": -1,
            "bytes_in": -1,
            "pkts_in": 0,
            "conn_tot": 0,
            "conn_cur": 0,
            "bytes_out": -1
          },
          "nodes": [
            {
              "label": "Node-Test-32fce25d",
              "port_name": "HTTP",
              "address": "29.181.84.2",
              "port_number": 80,
              "id": "Node-Test-32fce25d:29.181.84.2:80"
            },
            {
              "label": "Node-Test-8df4d3b7",
              "port_name": "HTTP",
              "address": "29.181.84.3",
              "port_number": 80,
              "id": "Node-Test-8df4d3b7:29.181.84.3:80"
            }
          ],
          "id": "Vip-Test-32fce25d:152.181.84.2:80",
          "vendor_extensions": {
            "none": "none"
          }
        }
      ]
    }


Add a Virtual IP
----------------

Load balancers must have at least one virtual IP address that clients
can use to balance traffic across nodes. You can use the manage virtual
IPs operations to configure and manage the virtual IP addresses for the
load balancer with the specified device ID.

An IP can be passed into the add Virtual IP call as part of the request
body, only if the IP exists within an existing virtual.

When adding a virtual IP, the following fields are required:
``account\_number``,
``label``, ``protocol``, ``port``, ``algorithm``, ``persistence``,
``admin\_state``, ``comment\*``

::

    POST /{device_id}/vips

*This operation accepts a request body:*

**Request**

::

    {
      "account_number": req"<Account Number>",
      "label": req"<Label>",
      "description": "<description>",
      "ip": "<ip>",
      "protocol": req"<protocol>",
      "port": req"<port>",
      "algorithm": req{},
      "persistence": req{},
      "nodes": {},
      "admin_state": req"<enabled|disabled>",
      "comment": req"comment"
    }

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Retrieve virtual IP information
-------------------------------

Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

*When deleting, these fields are required: account\_number, comment*

::

    GET /{device_id}/vips/{vip_id}

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
      "load_balancer_data": {
        "protocol": "TCP",
        "description": "Some description",
        "algorithm": {
          "persistence_method": "client_ip",
          "name": "LEAST_CONNECTION",
          "persistence": "ENABLED",
          "subnet_prefix_length": 0
        },
        "ip": "152.181.84.2",
        "runtime_state": "UNHEALTHY",
        "label": "Vip-Test-32fce25d",
        "port_number": 80,
        "port_name": "HTTP",
        "admin_state": "ENABLED",
        "stats": {
          "conn_max": -1,
          "pkts_out": -1,
          "bytes_in": -1,
          "pkts_in": 0,
          "conn_tot": 0,
          "conn_cur": 0,
          "bytes_out": -1
        },
        "nodes": [
          {
            "label": "Node-Test-32fce25d",
            "port_name": "HTTP",
            "address": "29.181.84.2",
            "port_number": 80,
            "id": "Node-Test-32fce25d:29.181.84.2:80"
          }
        ],
        "id": "Vip-Test-32fce25d:152.181.84.2:80",
        "vendor_extensions": {
          "none": "none"
        }
      }
    }

Update virtual IP information
-----------------------------

Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

*When deleting, these fields are required: account\_number, comment*

::

    PUT /{device_id}/vips/{vip_id}

*This operation accepts a request body:*

**Request**

::

    {
      "account_number": req"<Account Number>",
      "label": req"<Label>",
      "description": "<description>",
      "ip": "<ip>",
      "protocol": req"<protocol>",
      "port": req"<port>",
      "algorithm": req{},
      "persistence": req{},
      "nodes": {},
      "admin_state": req"<enabled|disabled>",
      "comment": req"comment"
    }

PUT Virtual IPs information 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Delete a virtual IP
-------------------

Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

The following fields are required for the delete operation:
``account\_number``, ``comment*``.

::

    DELETE /{device_id}/vips/{vip_id}

*This operation accepts a request body:*

Request body
^^^^^^^^^^^^
::

    {
      "account_number": "<Account Number>",
      "comment": "<comment>"
    }

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

List nodes for the specified virtual IP
----------------------------------------

Retrieve information about the nodes associated with a specified virtual
IP.

::

    GET /{device_id}/vips/{vip_id}/nodes

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
      "load_balancer_data": [
        {
          "links": {
            "self": {
              "href": "https://api-qual.netsec.rackspace.net/loadbalancers/534583/nodes/Node-Test-32fce25d%3A29.181.84.2%3A80",
              "rel": "self"
            },
            "rel": {
              "href": "https://api-qual.netsec.rackspace.net/loadbalancers/534583/nodes",
              "rel": "up"
            }
          },
          "label": "Node-Test-32fce25d",
          "port_name": "HTTP",
          "address": "29.181.84.2",
          "port_number": 80,
          "id": "Node-Test-32fce25d:29.181.84.2:80"
        }
      ]
    }

Assign node to virtual IP
-------------------------

Use the virtual IP node configuration operations to add or remove a
specified node from the virtual IP configuration.

*When assigning a node to a virtual, this field is required:
account\_number*

::

    POST /{device_id}/vips/{vip_id}/nodes/{node_id}

*This operation accepts a request body:*

**Request**

::

    {
      "account_number": "<Account Number>"
    }

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Remove node from virtual IP configuration
-----------------------------------------

Use the virtual IP node configuration operations to add or remove a
specified node from the virtual IP configuration.


::

    DELETE /{device_id}/vips/{vip_id}/nodes/{node_id}

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Enable a virtual IP
-------------------

Use the virtual IP configuration operations to enable or disable a
virtual IP configured for a specified device.

::

    POST /{device_id}/vips/{vip_id}/configuration

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Disable a virtual IP
--------------------

Use the virtual IP configuration operations to enable or disable a
virtual IP configured for a specified device.

::

    DELETE /{device_id}/vips/{vip_id}/configuration

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Show virtual IP statistics
--------------------------

Retrieves usage data for the specified virtual IP.

::

    GET /{device_id}/vips/{vip_id}/stats

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
        "load_balancer_data": {
            "conn_max": -1,
            "pkts_out": -1,
            "bytes_in": -1,
            "pkts_in": 0,
            "conn_tot": 0,
            "conn_cur": 0,
            "bytes_out": -1
        }
    }


Nodes in a device for the given device id
-----------------------------------------

A node is a back-end device providing a service on a specified IP and
port.

Use the nodes operations to get information about the nodes configured
for a specified device and to add a node.

After a node has been defined, use the virtual IP nodes configuration
operations to assign the node to one or more virtual IPs.

*When adding a node to a device, these fields are rquired:
account\_number, label, ip, port, admin\_state, health\_strategy,
vendor\_extensions, comment*

::

    GET /{device_id}/nodes

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
      "load_balancer_data": [
        {
          "stats": {
            "conn_max": 0,
            "pkts_out": 0,
            "bytes_in": 0,
            "pkts_in": 0,
            "conn_tot": 0,
            "conn_cur": 0,
            "bytes_out": 0
          },
          "links": {
            "self": {
              "href": "https://api-qual.netsec.rackspace.net/loadbalancers/534583/nodes/Node-Test-c4b3b8a5%3A29.235.243.3%3A12345",
              "rel": "self"
            },
            "rel": {
              "href": "https://api-qual.netsec.rackspace.net/loadbalancers/534583/nodes",
              "rel": "up"
            }
          },
          "runtime_state": "UNHEALTHY",
          "label": "Node-Test-c4b3b8a5",
          "port_name": "12345",
          "admin_state": "ENABLED",
          "address": "29.235.243.3",
          "port_number": 12345,
          "id": "Node-Test-c4b3b8a5:29.235.243.3:12345"
        }
      ]
    }


Add a node to a device
----------------------

A node is a back-end device providing a service on a specified IP and
port.

Use the nodes operations to get information about the nodes configured
for a specified device and to add a node.

After a node has been defined, use the virtual IP nodes configuration
operations to assign the node to one or more virtual IPs.

When adding a node to a device, the following fields are required:
``account\_number``, ``label``, ``ip``, ``port``, ``admin\_state``,
``health\_strategy``, ``vendor\_extensions``, ``comment*``

::

    POST /{device_id}/nodes

*This operation accepts a request body:*

**Request**

::

    {
      "account_number": "<Account Number> (required)",
      "label": "<Node Label> (required)",
      "description": "<description>",
      "ip": "<ip> (required)",
      "port": "<port> (required)",
      "admin_state": "<enabled|disabled> (required)",
      "health_strategy": "<health_strategy JSON Object> (required)",
      "vendor_extensions": "<vendor_extension JSON object> (required)",
      "comment": "comment (required)"
    }

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Retrieve node information
-------------------------

Use the node operations to view, update, or remove a specified node.

::

    GET /{device_id}/nodes/{node_id}

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
      "load_balancer_data": {
        "protocol": "TCP",
        "description": null,
        "links": {
          "self": {
            "href": "https://api-qual.netsec.rackspace.net/loadbalancers/534583/nodes/Node-Test-c4b3b8a5%3A29.235.243.3%3A12345",
            "rel": "self"
          },
          "rel": {
            "href": "https://api-qual.netsec.rackspace.net/loadbalancers/534583/nodes",
            "rel": "up"
          }
        },
        "runtime_state": "UNHEALTHY",
        "label": "Node-Test-c4b3b8a5",
        "port_name": "12345",
        "port_number": 12345,
        "limit": 1000,
        "admin_state": "ENABLED",
        "address": "29.235.243.3",
        "stats": {
          "conn_max": 0,
          "pkts_out": 0,
          "bytes_in": 0,
          "pkts_in": 0,
          "conn_tot": 0,
          "conn_cur": 0,
          "bytes_out": 0
        },
        "id": "Node-Test-c4b3b8a5:29.235.243.3:12345",
        "vendor_extensions": {
          "reassign_count": 0
        },
        "health_strategy": {
          "http_body_pattern": null,
          "http_codes_ok": [
            200,
            203
          ],
          "ssl": false,
          "port_number": 12345,
          "path": "/",
          "strategy": "HTTP_RES_CODE",
          "method": "GET"
        }
      }
    }


Update node information
-----------------------

Use the node operations to view, update, or remove a specified node.

::

    PUT /{device_id}/nodes/{node_id}

*This operation accepts a request body:*

**Request**

::

    {
      "account_number": "<Account Number> (required)",
      "ip": "<ip>",
      "port": "<port>",
      "label": "<Node Label>",
      "health_strategy": {},
      "admin_state": "<enabled|disabled>"
      "vendor_extensions": {},
      "comment": "<comment> (required)"
    }

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Delete node from the device configuration
-----------------------------------------

Use the node operations to view, update, or remove a specified node.

::

    DELETE /{device_id}/nodes/{node_id}

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Enable a node
-------------

Use the node status operations to enable or disable a specified node
included in the device configuration.

If you want to delete the node from the configuration file, use the
delete node operation.

::

    POST /{device_id}/nodes/{node_id}/configuration

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Disable a node
--------------

Use the node status operations to enable or disable a specified node
included in the device configuration.

If you want to delete the node from the configuration file, use the
delete node operation.

::

    DELETE /{device_id}/nodes/{node_id}/configuration

Response
^^^^^^^^

The request has been accepted for processing.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Show node statistics
--------------------

Retrieves usage data for a specified node ID.

::

    GET /{device_id}/nodes/{node_id}/stats

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
      "load_balancer_data": {
        "conn_max": 0,
        "pkts_out": 0,
        "bytes_in": 0,
        "pkts_in": 0,
        "conn_tot": 0,
        "conn_cur": 0,
        "bytes_out": 0
      }
    }

List events
-----------

Use the events operations to get information about requests to create or
modify load balancer resources.

::

    GET /{device_id}/events

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
      "data": [
        {
          "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
          "@type": "Event",
          "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
          "status": "200",
          "message": "Processing",
          "timestamp": "2015-04-01T10:05:01.55Z",
        },
        {
          "@id": "/loadbalancers/0a68f7c8-e2f9-11e4-8a00-1681e6b88ec1",
          "@type": "Event",
          "event_id": "0a68f7c8-e2f9-11e4-8a00-1681e6b88ec1",
          "status": "202",
          "message": "Accepted",
          "timestamp": "2015-04-01T11:17:05.45Z",
        },
        {
          "@id": "/loadbalancers/104e8b58-e2f9-11e4-8a00-1681e6b88ec1",
          "@type": "Event",
          "event_id": "104e8b58-e2f9-11e4-8a00-1681e6b88ec1",
          "status": "201",
          "message": "Created",
          "timestamp": "2015-04-01T19:15:01.3Z",
        }
      ]
    }

Retrieves event information by event ID.
----------------------------------------

Use the event ID details operation to get information about about a
specific event including event type, status, message, and timestamp.

::

    GET /{device_id}/events/{event_id}

*This operation does not accept a request body.*

Response
^^^^^^^^

Successfully processed the request.

::

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }
