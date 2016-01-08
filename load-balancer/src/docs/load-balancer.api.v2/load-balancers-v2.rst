**Endpoint:**
https://bpi.automation.api.rackspacecloud.com/2.0/{tenant\_id}

Device ID
---------

Use the Device ID operation to get complete information about the device
with the specified ID including associated customer, usage statistics,
and configuration details for nodes, virtual IPs, and high availability.

.. code:: javascript

    GET /loadbalancer/{device_id}

Retrieve device information

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

GET 404 response
^^^^^^^^^^^^^^^^

Not found.

.. code:: javascript

    {
      "status_code": 404,
      "response": {
        "transactionId": "456a50ccecc3da8fbc4b03ea3956bf40",
        "statusCode": 404,
        "details": "The requested resource was not found.",
        "title": "404 Not Found"
      },
      "source_of_error": "FIRE_ENGINE",
      "error": "404 Client Error: Object Not Found"
    }

Device configuration
--------------------

Retrieves the load balancer configuration information for the specified
device ID.

.. code:: javascript

    GET /loadbalancer/{device_id}/configuration

Retrieve load balancer configuration details

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

    {
      "load_balancer_data": {
        "b64": "key"
      }
    }

High Availability configuration template
----------------------------------------

Retrieves the high availability configuration template for a device with
the specified ID.

.. code:: javascript

    GET /loadbalancer/{device_id}/ha

Show high availability template

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

    {
      "message": "This is a test template for High Availability"
    }

Manage Virtual IPs
------------------

Load balancers must have at least one virtual IP address that clients
can use to access the device. You can use the manage virtual IPs
operations to configure and manage the virtual IP addresses for the load
balancer with the specified device ID.

After you update the device configuration, use the update virtual IP
node configuration operation to configure the services associated with
the specified virtual IP address. Then, use the enable virtual IP
operation to apply the changes to the device.

.. code:: javascript

    GET /loadbalancer/{device_id}/vips

Retrieve virtual IPs configuration

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

GET 404 response
^^^^^^^^^^^^^^^^

Not found.

.. code:: javascript

    {
      "status_code": 404,
      "response": {
        "transactionId": "456a50ccecc3da8fbc4b03ea3956bf40",
        "statusCode": 404,
        "details": "The requested resource was not found.",
        "title": "404 Not Found"
      },
      "source_of_error": "FIRE_ENGINE",
      "error": "404 Client Error: Object Not Found"
    }

Manage Virtual IPs
------------------

Load balancers must have at least one virtual IP address that clients
can use to access the device. You can use the manage virtual IPs
operations to configure and manage the virtual IP addresses for the load
balancer with the specified device ID.

After you update the device configuration, use the update virtual IP
node configuration operation to configure the services associated with
the specified virtual IP address. Then, use the enable virtual IP
operation to apply the changes to the device.

.. code:: javascript

    POST /loadbalancer/{device_id}/vips

Add a virtual IP

*This operation accepts a request body:*

**Request**

.. code:: javascript

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

POST Manage Virtual IPs 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Virtual IPs information
-----------------------

Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

.. code:: javascript

    GET /loadbalancer/{device_id}/vips/{vip_id}

Retrieve virtual IP information

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

GET 404 response
^^^^^^^^^^^^^^^^

Not found.

.. code:: javascript

    {
      "status_code": 404,
      "response": {
        "transactionId": "456a50ccecc3da8fbc4b03ea3956bf40",
        "statusCode": 404,
        "details": "The requested resource was not found.",
        "title": "404 Not Found"
      },
      "source_of_error": "FIRE_ENGINE",
      "error": "404 Client Error: Object Not Found"
    }

Virtual IPs information
-----------------------

Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

.. code:: javascript

    PUT /loadbalancer/{device_id}/vips/{vip_id}

Update virtual IP information

*This operation accepts a request body:*

**Request**

.. code:: javascript

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

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Virtual IPs information
-----------------------

Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

.. code:: javascript

    DELETE /loadbalancer/{device_id}/vips/{vip_id}

Delete a virtual IP

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>",
      "comment": req"comment"
    }

DELETE Virtual IPs information 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Virtual IP node configuration
-----------------------------

Retrieve information about the nodes associated with a specified virtual
IP.

.. code:: javascript

    GET /loadbalancer/{device_id}/vips/{vip_id}/nodes

List nodes for the specified virtual IP.

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

Manage virtual IP node configuration
------------------------------------

Use the virtual IP node configuration operations to add or remove a
specified node from the virtual IP configuration.

.. code:: javascript

    POST /loadbalancer/{device_id}/vips/{vip_id}/nodes/{node_id}

Assign node to virtual IP

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>"
    }

POST Manage virtual IP node configuration 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Manage virtual IP node configuration
------------------------------------

Use the virtual IP node configuration operations to add or remove a
specified node from the virtual IP configuration.

.. code:: javascript

    DELETE /loadbalancer/{device_id}/vips/{vip_id}/nodes/{node_id}

Remove node from virtual IP configuration

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>"
    }

DELETE Manage virtual IP node configuration 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Manage Virtual IP status
------------------------

Use the virtual IP configuration operations to enable or disable a
virtual IP configured for a specified device. post: description: \|
Enable a virtual IP body: application/json: example: \| {
"account\_number": req"" } responses: 202: description: The request has
been accepted for processing. body: application/json: example: !include
event.sample

.. code:: javascript

    DELETE /loadbalancer/{device_id}/vips/{vip_id}/configuration

Disable a virtual IP

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>"
    }

DELETE Manage Virtual IP status 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Virtual IP statistics
---------------------

Retrieves usage data for the specified virtual IP.

.. code:: javascript

    GET /loadbalancer/{device_id}/vips/{vip_id}/stats

Show virtual IP statistics

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

GET 404 response
^^^^^^^^^^^^^^^^

Not found.

.. code:: javascript

    {
      "status_code": 404,
      "response": {
        "transactionId": "456a50ccecc3da8fbc4b03ea3956bf40",
        "statusCode": 404,
        "details": "The requested resource was not found.",
        "title": "404 Not Found"
      },
      "source_of_error": "FIRE_ENGINE",
      "error": "404 Client Error: Object Not Found"
    }

Nodes
-----

A node is a back-end device providing a service on a specified IP and
port.

| Use the nodes operations to get information about the nodes configured
  for
| a specified device and to add a node.

After a node has been defined, use the virtual IP nodes configuration
operations to assign the node to one or more virtual IPs.

.. code:: javascript

    GET /loadbalancer/{device_id}/nodes

Nodes in a device for the given device id

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

GET 404 response
^^^^^^^^^^^^^^^^

.. code:: javascript

    {
      "status_code": 404,
      "response": {
        "transactionId": "456a50ccecc3da8fbc4b03ea3956bf40",
        "statusCode": 404,
        "details": "The requested resource was not found.",
        "title": "404 Not Found"
      },
      "source_of_error": "FIRE_ENGINE",
      "error": "404 Client Error: Object Not Found"
    }

Nodes
-----

A node is a back-end device providing a service on a specified IP and
port.

| Use the nodes operations to get information about the nodes configured
  for
| a specified device and to add a node.

After a node has been defined, use the virtual IP nodes configuration
operations to assign the node to one or more virtual IPs.

.. code:: javascript

    POST /loadbalancer/{device_id}/nodes

Add a node to a device

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>",
      "label": req"<Node Label>",
      "description": "<description>",
      "ip": req"<ip>",
      "port": req"<port>",
      "admin_state": req"<enabled|disabled>",
      "health_strategy": req"<health_strategy JSON Object>",
      "vendor_extensions": req"<vendor_extension JSON object>",
      "comment": req"comment"
    }

POST Nodes 202 response
^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Manage node information
-----------------------

Use the node operations to view, update, or remove a specified node.

.. code:: javascript

    GET /loadbalancer/{device_id}/nodes/{node_id}

Retrieve node information

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

GET 404 response
^^^^^^^^^^^^^^^^

Not found.

.. code:: javascript

    {
      "status_code": 404,
      "response": {
        "transactionId": "456a50ccecc3da8fbc4b03ea3956bf40",
        "statusCode": 404,
        "details": "The requested resource was not found.",
        "title": "404 Not Found"
      },
      "source_of_error": "FIRE_ENGINE",
      "error": "404 Client Error: Object Not Found"
    }

Manage node information
-----------------------

Use the node operations to view, update, or remove a specified node.

.. code:: javascript

    PUT /loadbalancer/{device_id}/nodes/{node_id}

Update node information

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>",
      "ip": "<ip>",
      "port": "<port>",
      "label": "<Node Label>",
      "health_strategy": {},
      "admin_state": "<enabled|disabled>"
      "vendor_extensions": {},
      "comment": req"comment"
    }

PUT Manage node information 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Manage node information
-----------------------

Use the node operations to view, update, or remove a specified node.

.. code:: javascript

    DELETE /loadbalancer/{device_id}/nodes/{node_id}

Delete node from the device configuration

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>"
    }

DELETE Manage node information 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Manage node status
------------------

Use the node status operations to enable or disable a specified node
included in the device configuration.

If you want to delete the node from the configuration file, use the
delete node operation.

.. code:: javascript

    POST /loadbalancer/{device_id}/nodes/{node_id}/configuration

Enable a node

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>"
    }

POST Manage node status 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Manage node status
------------------

Use the node status operations to enable or disable a specified node
included in the device configuration.

If you want to delete the node from the configuration file, use the
delete node operation.

.. code:: javascript

    DELETE /loadbalancer/{device_id}/nodes/{node_id}/configuration

Disable a node

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "account_number": req"<Account Number>"
    }

DELETE Manage node status 202 response
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The request has been accepted for processing.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Node statistics
---------------

Retrieves usage data for a specified node ID.

.. code:: javascript

    GET /loadbalancer/{device_id}/nodes/{node_id}/stats

Show node statistics

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

GET 404 response
^^^^^^^^^^^^^^^^

Not found.

.. code:: javascript

    {
      "status_code": 404,
      "response": {
        "transactionId": "456a50ccecc3da8fbc4b03ea3956bf40",
        "statusCode": 404,
        "details": "The requested resource was not found.",
        "title": "404 Not Found"
      },
      "source_of_error": "FIRE_ENGINE",
      "error": "404 Client Error: Object Not Found"
    }

Events
------

Use the events operations to get information about requests to create or
modify load balancer resources.

.. code:: javascript

    GET /loadbalancer/{device_id}/events

List events

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

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

Event ID details
----------------

Use the event ID details operation to get information about about a
specific event including event type, status, message, and timestamp.

.. code:: javascript

    GET /loadbalancer/{device_id}/events/{event_id}

Retrieves event information by event ID.

*This operation does not accept a request body.*

GET 200 response
^^^^^^^^^^^^^^^^

Successfully processed the request.

.. code:: javascript

    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

