**Endpoint:** https://lb.dedicated.api.rackspacecloud.com/2.0/{tenant_id}/loadbalancers


		
            
                
## Returns a complete info about loadbalancer
				
                
```
GET /{device_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
    

		
            
                
## Config info for a given node.
				
                
```
GET /{device_id}/configuration
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
```
{
  "load_balancer_data": {
    "b64": "key"
  }
}

```
							
						
					
				
			
        
    

		
            
                
## High Availability template.
				
                
```
GET /{device_id}/ha
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
```
{
  "message": "This is a test template for High Availability"
}

```
							
						
					
				
			
        
    

		
            
                
## VIPs in a device for the given device id
				
                
```
GET /{device_id}/vips
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
                
## Create a new VIP.
				
                
```
POST /{device_id}/vips
```


			
				
            


**Request**
						

						

```
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
```
					
                
					
					
						
							
								
									
#### POST VIPs configured to devices response
									
                                

							
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
							
						
					
				
			
        
    

		
            
                
## Information about single VIP.
				
                
```
GET /{device_id}/vips/{vip_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
                
## Update VIP information.
				
                
```
PUT /{device_id}/vips/{vip_id}
```


			
				
            


**Request**
						

						

```
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
```
					
                
					
					
						
							
								
									
#### PUT VIP Information for given VIP id. response
									
                                

							
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
							
						
					
				
			
        
                
## Delete VIP.
				
                
```
DELETE /{device_id}/vips/{vip_id}
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>",
  "comment": req"comment"
}

```
					
                
					
					
						
							
								
									
#### DELETE VIP Information for given VIP id. response
									
                                

							
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
							
						
					
				
			
        
    

		
            
                
## List nodes for single VIP.
				
                
```
GET /{device_id}/vips/{vip_id}/nodes
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
    

		
            
                
## Bind given node_id with VIP.
				
                
```
POST /{device_id}/vips/{vip_id}/nodes/{node_id}
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### POST Bind/Unbind given node_id with vip. response
									
                                

							
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
							
						
					
				
			
        
                
## Unbind given node_id from VIP.
				
                
```
DELETE /{device_id}/vips/{vip_id}/nodes/{node_id}
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### DELETE Bind/Unbind given node_id with vip. response
									
                                

							
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
							
						
					
				
			
        
    

		
            
                
## Activate the VIP.
				
                
```
POST /{device_id}/vips/{vip_id}/configuration
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### POST Activate/Deactivate VIP. response
									
                                

							
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
							
						
					
				
			
        
                
## Deactivate the VIP.
				
                
```
DELETE /{device_id}/vips/{vip_id}/configuration
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### DELETE Activate/Deactivate VIP. response
									
                                

							
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
							
						
					
				
			
        
    

		
            
                
## Statistics for single VIP.
				
                
```
GET /{device_id}/vips/{vip_id}/stats
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
    

		
            
                
## Nodes in a device for the given device id
				
                
```
GET /{device_id}/nodes
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
                
## Create a new node.
				
                
```
POST /{device_id}/nodes
```


			
				
            


**Request**
						

						

```
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
```
					
                
					
					
						
							
								
									
#### POST Information about Nodes. response
									
                                

							
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
							
						
					
				
			
        
    

		
            
                
## Node Information
				
                
```
GET /{device_id}/nodes/{node_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
                
## Update node configuration.
				
                
```
PUT /{device_id}/nodes/{node_id}
```


			
				
            


**Request**
						

						

```
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
```
					
                
					
					
						
							
								
									
#### PUT Information about a particular node. response
									
                                

							
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
				
                
```
DELETE /{device_id}/nodes/{node_id}
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### DELETE Information about a particular node. response
									
                                

							
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
							
						
					
				
			
        
    

		
            
                
## Activate the node.
				
                
```
POST /{device_id}/nodes/{node_id}/configuration
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### POST Activate/Deactivate node. response
									
                                

							
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
							
						
					
				
			
        
                
## Deactivate the node.
				
                
```
DELETE /{device_id}/nodes/{node_id}/configuration
```


			
				
            


**Request**
						

						

```
{
  "account_number": req"<Account Number>"
}

```
					
                
					
					
						
							
								
									
#### DELETE Activate/Deactivate node. response
									
                                

							
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
							
						
					
				
			
        
    

		
            
                
## Display the stats for given node_id
				
                
```
GET /{device_id}/nodes/{node_id}/stats
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
    

		
            
                
## Returns a list of events.
				
                
```
GET /{device_id}/events
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
    

		
            
                
## Returns a specfic event info.
				
                
```
GET /{device_id}/events/{event_id}
```


			
				
*This operation does not accept a request body.*
            
            
                
					
					
						
							
								
                                
#### GET 200 response
							

							
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
							
						
					
				
			
        
    
