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

Retrieve information about all virtual servers configured in the load balancer including configuration data and status information.

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
Add a virtual server configuration to the load balancer.

::

    POST /{device_id}/vips


Request
^^^^^^^

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

Use the virtual IPs information operations to retrieve 
information for a virtual IP configured for the specified device ID.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs configuration operation to find it.


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

Use the virtual IPs information operations to  update
information for a virtual IP configured for the specified device ID.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs configuration operation to find it.


::

    PUT /{device_id}/vips/{vip_id}


Request body
^^^^^^^^^^^^

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

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

The following fields are required for the delete operation:
``account_number``, ``comment*``.

::

    DELETE /{device_id}/vips/{vip_id}

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

Use the virtual IP node configuration operations to add 
specified node from the virtual IP configuration.

*When you assign a node to a virtual IP, the following field is required:
account\_number.*

::

    POST /{device_id}/vips/{vip_id}/nodes/{node_id}


Request body
^^^^^^^^^^^^
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

Use the virtual IP node configuration operations to remove a
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

Use the virtual IP configuration operations to enable a
virtual IP configured for a specified device.

::

    POST /{device_id}/vips/{vip_id}/configuration

Request body
^^^^^^^^^^^^
::

  {
    "account_number": "<Account Number> (required)"
  }

202 Response
^^^^^^^^^^^^

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

Use the virtual IP configuration operations to  disable a
virtual IP configured for a specified device.

::

    DELETE /{device_id}/vips/{vip_id}/configuration


Request body
^^^^^^^^^^^^
::

  {
    "account_number": "<Account Number> (required)"
  }

202 Response
^^^^^^^^^^^^

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


Show Nodes for the given device id
-----------------------------------

A node is a back-end device providing a service on a specified IP and
port.

Use the nodes operations to get information about the nodes configured
for a specified device


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

Use the nodes operations to add a node for a specified device

When adding a node to a device, the following fields are required:
``account_number``, ``label``, ``ip``, ``port``, ``admin_state``,
``health_strategy``, ``vendor_extensions``, ``comment*``

::

    POST /{device_id}/nodes

Request body
^^^^^^^^^^^^^

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

202 Response
^^^^^^^^^^^^

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

Use the node operations to view a specified node.

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

Use the node operations to  update a specified node.

::

    PUT /{device_id}/nodes/{node_id}


Request body
^^^^^^^^^^^^

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

202 Response
^^^^^^^^^^^^^

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

Use the node operations to remove a specified node.

::

    DELETE /{device_id}/nodes/{node_id}

Request body
^^^^^^^^^^^^

::

  {
    "account_number": "<Account Number> (required)"
  }

202 Response
^^^^^^^^^^^^

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

Use the node  operations to enable  specified node
included in the device configuration.


::

    POST /{device_id}/nodes/{node_id}/configuration

Request body
^^^^^^^^^^^^
::

{
  "account_number": "<Account Number> (required)"
}

202 Response
^^^^^^^^^^^^

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

Use the node status operations to   disable a specified node
included in the device configuration.

Request body
^^^^^^^^^^^^

::

  {
    "account_number": "<Account Number> (required)"
  }

::

    DELETE /{device_id}/nodes/{node_id}/configuration

*This operation does not accept a request body.*


202 Response
^^^^^^^^^^^^^

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

Retrieve all event information for a device

::

    GET /{device_id}/events

*This operation does not accept a request body.*

Response
^^^^^^^^^

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

Retrieve event information by event ID.

::

    GET /{device_id}/events/{event_id}

*This operation does not accept a request body.*

202 Response
^^^^^^^^^^^^

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
