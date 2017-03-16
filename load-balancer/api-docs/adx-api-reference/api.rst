**Endpoint**:
https://bpi.automation.api.rackspacecloud.com/2.0/{tenant\_id}/loadbalancers

Retrieve device information

.. code:: javascript

    GET /{device_id}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "load_balancer_data": {
        "customer": "1234567",
        "uptime": "unimplemented",
        "hostname": "adx1000-examplehost.iad3.netdev.net",
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
        "id": "1234567",
        "os_version": "127.0.00sT403",
        "management_ip": "127..0.0.1",
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
        "model_name": "SI-1216-4-EXAMPLE"
      }
    }

Show high availability configuration

.. code:: javascript

    GET /{device_id}/ha

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "message": "This is a test template for High Availability"
    }

Retrieve virtual IPs configuration

.. code:: javascript

    GET /{device_id}/vips

*Resource does not require a body*

Response:
^^^^^^^^^

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
          "ip": "127.0.0.1",
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
              "address": "127.0.0.1",
              "port_number": 80,
              "id": "Node-Test-32fce25d:127.0.0.1:80"
            },
            {
              "label": "Node-Test-8df4d3b7",
              "port_name": "HTTP",
              "address": "127.0.0.1",
              "port_number": 80,
              "id": "Node-Test-8df4d3b7:127.0.0.1:80"
            }
          ],
          "id": "Vip-Test-32fce25d:127.0.0.1:80",
          "vendor_extensions": {
            "none": "none"
          }
        }
      ]
    }

Add a Virtual IP

.. code:: javascript

    POST /{device_id}/vips

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)",
      "label": "<Label> (required)",
      "description": "<description>",
      "ip": "<ip>",
      "protocol": "<protocol> (required)",
      "port": "<port> (required)",
      "algorithm": {} (required),
      "persistence": {} (required),
      "nodes": {},
      "admin_state": "<enabled|disabled> (required)",
      "comment": "comment (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Retrieve Virtual IP information

.. code:: javascript

    GET /{device_id}/vips/{vip_id}

*Resource does not require a body*

Response:
^^^^^^^^^

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
        "ip": "127.0.0.1",
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
            "address": "127.0.0.1",
            "port_number": 80,
            "id": "Node-Test-32fce25d:127.0.0.1:80"
          }
        ],
        "id": "Vip-Test-32fce25d:127.0.0.1:80",
        "vendor_extensions": {
          "none": "none"
        }
      }
    }

Update Virtual IP information

.. code:: javascript

    PUT /{device_id}/vips/{vip_id}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)",
      "label": "<Label> (required)",
      "description": "<description>",
      "ip": "<ip>",
      "protocol": "<protocol> (required)",
      "port": "<port> (required)",
      "algorithm": {} (required),
      "persistence": {} (required),
      "nodes": {},
      "admin_state": "<enabled|disabled> (required)",
      "comment": "comment (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Delete a Virtual IP

.. code:: javascript

    DELETE /{device_id}/vips/{vip_id}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)",
      "comment": "<comment> (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

List nodes for the specified Virtual IP.

.. code:: javascript

    GET /{device_id}/vips/{vip_id}/nodes

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "load_balancer_data": [
        {
          "label": "Node-Test-32fce25d",
          "port_name": "HTTP",
          "address": "127.0.0.1",
          "port_number": 80,
          "id": "Node-Test-32fce25d:29.181.84.2:80"
        }
      ]
    }

Assign node to Virtual IP

.. code:: javascript

    POST /{device_id}/vips/{vip_id}/nodes/{node_id}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number>"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Remove node from Virtual IP configuration

.. code:: javascript

    DELETE /{device_id}/vips/{vip_id}/nodes/{node_id}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Activate the Virtual IP.

.. code:: javascript

    POST /{device_id}/vips/{vip_id}/configuration

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Deactivate the Virtual IP.

.. code:: javascript

    DELETE /{device_id}/vips/{vip_id}/configuration

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Show Virtual IP statistics

.. code:: javascript

    GET /{device_id}/vips/{vip_id}/stats

*Resource does not require a body*

Response:
^^^^^^^^^

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

Nodes in a device for the given device id

.. code:: javascript

    GET /{device_id}/nodes

*Resource does not require a body*

Response:
^^^^^^^^^

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
          "runtime_state": "UNHEALTHY",
          "label": "Node-Test-c4b3b8a5",
          "port_name": "12345",
          "admin_state": "ENABLED",
          "address": "127.0.0.1",
          "port_number": 12345,
          "id": "Node-Test-c4b3b8a5:29.235.243.3:12345"
        }
      ]
    }

Add a Node to a device

.. code:: javascript

    POST /{device_id}/nodes

Request body:
^^^^^^^^^^^^^

.. code:: javascript

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

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Retrieve Node information

.. code:: javascript

    GET /{device_id}/nodes/{node_id}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


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
        "address": "127.0.0.1",
        "stats": {
          "conn_max": 0,
          "pkts_out": 0,
          "bytes_in": 0,
          "pkts_in": 0,
          "conn_tot": 0,
          "conn_cur": 0,
          "bytes_out": 0
        },
        "id": "Node-Test-c4b3b8a5:127.0.0.1.3:12345",
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

.. code:: javascript

    PUT /{device_id}/nodes/{node_id}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

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

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Delete the Node.

.. code:: javascript

    DELETE /{device_id}/nodes/{node_id}

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Activate the Node.

.. code:: javascript

    POST /{device_id}/nodes/{node_id}/configuration

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Deactivate the Node.

.. code:: javascript

    DELETE /{device_id}/nodes/{node_id}/configuration

Request body:
^^^^^^^^^^^^^

.. code:: javascript

    {
      "account_number": "<Account Number> (required)"
    }

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

Show Node statistics

.. code:: javascript

    GET /{device_id}/nodes/{node_id}/stats

*Resource does not require a body*

Response:
^^^^^^^^^

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

List Events

.. code:: javascript

    GET /{device_id}/events

*Resource does not require a body*

Response:
^^^^^^^^^

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

Retrieves Event information using the specified event ID.

.. code:: javascript

    GET /{device_id}/events/{event_id}

*Resource does not require a body*

Response:
^^^^^^^^^

.. code:: javascript


    {
      "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "@type": "Event",
      "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
      "status": "200",
      "message": "Processing",
      "timestamp": "2015-04-01T10:05:01.55Z",
    }

