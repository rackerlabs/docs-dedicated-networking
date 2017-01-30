**Endpoint:** https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant_id}/loadbalancers


		
            
                
## Retrieve device information
				
                
Using the device resource will allow you to retrieve information for the given device. 

The resource also allows you to create, update, retrieve and delete on several of the
device's sub-resources for the device you selected. You will be able to make these actions
on the following sub-resources - configuration, ha, vips, nodes, and events.

                
```
GET /{device_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
{
  "load_balancer_data": {
    "customer": "1234567",
    "uptime": "unimplemented",
    "hostname": "adx1000-examplehost.iad3.netdev.net",
    "links": {
      "device": {
        "href": "https://api-qual.netsec.rackspace.net/devices/1234567",
        "rel": "alternate"
      },
      "lb": {
        "href": "https://api-qual.netsec.rackspace.net/loadbalancers",
        "rel": "up"
      },
      "self": {
        "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567",
        "rel": "self"
      },
      "vips": {
        "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/vips",
        "rel": "related"
      },
      "nodes": {
        "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/nodes",
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

```
							
						
					
				
					
					
						
							
								
                                
#### GET 404 response
							

							
Not found.

```
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
```
							
						
					
				
			
        
    

		
            
                
## Retrieve load balancer configuration details
				
                
Retrieves the load balancer configuration information for the specified
device ID.

                
```
GET /{device_id}/configuration
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
{
  "load_balancer_data": {
    "b64": "key"
  }
}

```
							
						
					
				
			
        
    

		
            
                
## Show high availability configuration
				
                
Retrieves the high availability configuration for
the specified device ID.

                
```
GET /{device_id}/ha
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
{
  "message": "This is a test template for High Availability"
}

```
							
						
					
				
			
        
    

		
            
                
## Retrieve virtual IPs configuration
				
                
Load balancers must have at least one virtual IP address that clients
can use to balance traffic across nodes. You can use the manage virtual IPs
operations to configure and manage the virtual IP addresses for the load
balancer using the specified device ID.

An IP can be passed into the `add Virtual IP` call as part of the request body,
only if the IP exists within an existing Virtual.

*When adding a Virtual IP, these fields are required: account_number, label, protocol,
port, algorithm, persistence, admin_state, comment*

                
```
GET /{device_id}/vips
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
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

```
							
						
					
				
					
					
						
							
								
                                
#### GET 404 response
							

							
Not found.

```
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
```
							
						
					
				
			
        
                
## Add a Virtual IP
				
                
Load balancers must have at least one virtual IP address that clients
can use to balance traffic across nodes. You can use the manage virtual IPs
operations to configure and manage the virtual IP addresses for the load
balancer using the specified device ID.

An IP can be passed into the `add Virtual IP` call as part of the request body,
only if the IP exists within an existing Virtual.

*When adding a Virtual IP, these fields are required: account_number, label, protocol,
port, algorithm, persistence, admin_state, comment*

                
```
POST /{device_id}/vips
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
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

```
					
                
					
					
						
							
								
									
#### POST Manage Virtual IPs 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    

		
            
                
## Retrieve Virtual IP information
				
                
Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

*When deleting, these fields are required: account_number, comment*

                
```
GET /{device_id}/vips/{vip_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
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

```
							
						
					
				
					
					
						
							
								
                                
#### GET 404 response
							

							
Not found.

```
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
```
							
						
					
				
			
        
                
## Update Virtual IP information
				
                
Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

*When deleting, these fields are required: account_number, comment*

                
```
PUT /{device_id}/vips/{vip_id}
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
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

```
					
                
					
					
						
							
								
									
#### PUT Virtual IP 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
                
## Delete a Virtual IP
				
                
Use the virtual IPs information operations to retrieve and update
information for a virtual IP configured for the specified device ID.

Use the delete operation to remove a virtual IP from the device
configuration.

If you don't know the ID for a specified virtual IP, use the retrieve
virtual IPs operation to find it.

*When deleting, these fields are required: account_number, comment*

                
```
DELETE /{device_id}/vips/{vip_id}
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
{
  "account_number": "<Account Number> (required)",
  "comment": "<comment> (required)"
}

```
					
                
					
					
						
							
								
									
#### DELETE Virtual IP 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    

		
            
                
## List nodes for the specified Virtual IP.
				
                
Retrieve information about the nodes associated with the
specified Virtual IP.

                
```
GET /{device_id}/vips/{vip_id}/nodes
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
{
  "load_balancer_data": [
    {
      "links": {
        "self": {
          "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/nodes/Node-Test-32fce25d%3A29.181.84.2%3A80",
          "rel": "self"
        },
        "rel": {
          "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/nodes",
          "rel": "up"
        }
      },
      "label": "Node-Test-32fce25d",
      "port_name": "HTTP",
      "address": "127.0.0.1",
      "port_number": 80,
      "id": "Node-Test-32fce25d:29.181.84.2:80"
    }
  ]
}

```
							
						
					
				
			
        
    

		
            
                
## Assign node to Virtual IP
				
                
Use the Virtual IP node configuration operations to add or
remove a specified node from the Virtual IP configuration.

*When assigning a node to a virtual, this field is required: account_number*

                
```
POST /{device_id}/vips/{vip_id}/nodes/{node_id}
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
{
  "account_number": "<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### POST Manage Virtual IP node configuration 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
                
## Remove node from Virtual IP configuration
				
                
Use the Virtual IP node configuration operations to add or
remove a specified node from the Virtual IP configuration.

*When assigning a node to a virtual, this field is required: account_number*

                
```
DELETE /{device_id}/vips/{vip_id}/nodes/{node_id}
```


			
				
            
                
					
					
						
							
								
									
#### DELETE Manage Virtual IP node configuration 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    

		
            
                
## Activate the Virtual IP.
				
                
Use the Virtual IP configuration operations to enable or
disable a Virtual IP configured for a specified device.

                
```
POST /{device_id}/vips/{vip_id}/configuration
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
{
  "account_number": "<Account Number> (required)"
}

```
					
                
					
					
						
							
								
									
#### POST Manage Virtual IP status 202 response
									
                                

							
```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
                
## Deactivate the Virtual IP.
				
                
Use the Virtual IP configuration operations to enable or
disable a Virtual IP configured for a specified device.

                
```
DELETE /{device_id}/vips/{vip_id}/configuration
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
{
  "account_number": "<Account Number> (required)"
}

```
					
                
					
					
						
							
								
									
#### DELETE Manage Virtual IP status 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    

		
            
                
## Show Virtual IP statistics
				
                
Retrieves usage data for the specified Virtual IP.
                
```
GET /{device_id}/vips/{vip_id}/stats
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
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
```
							
						
					
				
					
					
						
							
								
                                
#### GET 404 response
							

							
Not found.

```
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
```
							
						
					
				
			
        
    

		
            
                
## Nodes in a device for the given device id
				
                
A Node is a back-end device providing a service on a specified IP and port.

Use the nodes operations to get information about the nodes configured for
a specified device and to add a node.

After a node has been defined, use the Virtual IP nodes configuration
operations to assign the node to one or more Virtual IPs.

*When adding a node to a device, these fields are rquired: account_number, label,
ip, port, admin_state, health_strategy, vendor_extensions, comment*

                
```
GET /{device_id}/nodes
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
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
          "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/nodes/Node-Test-c4b3b8a5%3A29.235.243.3%3A12345",
          "rel": "self"
        },
        "rel": {
          "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/nodes",
          "rel": "up"
        }
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

```
							
						
					
				
					
					
						
							
								
                                
#### GET 404 response
							

							
```
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
```
							
						
					
				
			
        
                
## Add a Node to a device
				
                
A Node is a back-end device providing a service on a specified IP and port.

Use the nodes operations to get information about the nodes configured for
a specified device and to add a node.

After a node has been defined, use the Virtual IP nodes configuration
operations to assign the node to one or more Virtual IPs.

*When adding a node to a device, these fields are rquired: account_number, label,
ip, port, admin_state, health_strategy, vendor_extensions, comment*

                
```
POST /{device_id}/nodes
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
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
```
					
                
					
					
						
							
								
									
#### POST Nodes 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    

		
            
                
## Retrieve Node information
				
                
Use the node operations to view, update, or remove a
specified node.

                
```
GET /{device_id}/nodes/{node_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
{
  "load_balancer_data": {
    "protocol": "TCP",
    "description": null,
    "links": {
      "self": {
        "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/nodes/Node-Test-c4b3b8a5%3A29.235.243.3%3A12345",
        "rel": "self"
      },
      "rel": {
        "href": "https://api-qual.netsec.rackspace.net/loadbalancers/1234567/nodes",
        "rel": "up"
      }
    },
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

```
							
						
					
				
					
					
						
							
								
                                
#### GET 404 response
							

							
Not found.

```
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
```
							
						
					
				
			
        
                
## Update node information
				
                
Use the node operations to view, update, or remove a
specified node.

                
```
PUT /{device_id}/nodes/{node_id}
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
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
```
					
                
					
					
						
							
								
									
#### PUT Manage Node information 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
                
## Delete the Node.
				
                
Use the node operations to view, update, or remove a
specified node.

                
```
DELETE /{device_id}/nodes/{node_id}
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
{
  "account_number": "<Account Number> (required)"
}

```
					
                
					
					
						
							
								
									
#### DELETE Manage Node information 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    

		
            
                
## Activate the Node.
				
                
Use the node status operations to enable or disable a specified
Node included in the device configuration.

If you want to delete the node from the configuration file, use the
delete node operation.

                
```
POST /{device_id}/nodes/{node_id}/configuration
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
{
  "account_number": "<Account Number> (required)"
}

```
					
                
					
					
						
							
								
									
#### POST Manage Node status 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
                
## Deactivate the Node.
				
                
Use the node status operations to enable or disable a specified
Node included in the device configuration.

If you want to delete the node from the configuration file, use the
delete node operation.

                
```
DELETE /{device_id}/nodes/{node_id}/configuration
```


			
				
            
*This operation accepts a request body:*

**Request**
						

						
```
{
  "account_number": "<Account Number> (required)"
}

```
					
                
					
					
						
							
								
									
#### DELETE Manage Node status 202 response
									
                                

							
The request has been accepted for processing.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    

		
            
                
## Show Node statistics
				
                
Retrieves usage data for a specified Node ID.
                
```
GET /{device_id}/nodes/{node_id}/stats
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
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
```
							
						
					
				
					
					
						
							
								
                                
#### GET 404 response
							

							
Not found.

```
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
```
							
						
					
				
			
        
    

		
            
                
## List Events
				
                
Use the events operations to get information about requests to create or
modify load balancer resources.

                
```
GET /{device_id}/events
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
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

```
							
						
					
				
			
        
    

		
            
                
## Retrieves Event information using the specified event ID.
				
                
Use the event ID details operation to get information about
about a specific event including event type, status, message, and
timestamp.

                
```
GET /{device_id}/events/{event_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
Successfully processed the request.

```
{
  "@id": "/loadbalancers/0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "@type": "Event",
  "event_id": "0a68f566-e2f9-11e4-8a00-1681e6b88ec1",
  "status": "200",
  "message": "Processing",
  "timestamp": "2015-04-01T10:05:01.55Z",
}
```
							
						
					
				
			
        
    
