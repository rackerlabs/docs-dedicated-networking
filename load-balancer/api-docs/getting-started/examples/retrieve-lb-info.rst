Retrieve load balancer details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can get detailed information about a load balancer associated
with your account by submitting a GET request to the
:ref:`base URL <baseurlf5>`. Information includes
customer account associated with the load balancer, hardware and software
specifications, network configuration, high availability status,
uptime, CPU status and other information about the device.

The following examples show the cURL request and response.

**Example: cURL Retrieve load balancer information request**

.. code::

   curl $BASE_URL \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" | python -m json.tool

.. note::

   This request does not accept a request body.

If the request is successful, you see an HTTP 200 response header
followed a listing of the load balancer information.

The response includes an array of links that you can use to retrieve
additional information about the load balancer configuration and other
details. For example, use the nodes link to retrieve information about
all the nodes configured in the load balancer.

**Example: cURL Retrieve details response**

.. code::

   {
       "data": [
           {
               "cpu_load": [
                   {
                       "average": {
                           "percent_load": 10,
                           "seconds_since": 0
                       },
                       "last_peak_load": {
                           "percent_load": 49,
                           "seconds_since": 0
                       },
                       "load_1_sec_avg": {
                           "percent_load": 9,
                           "seconds_since": 0
                       },
                       "load_300_sec_avg": {
                           "percent_load": -1,
                           "seconds_since": -1
                       },
                       "load_5_sec_avg": {
                           "percent_load": -1,
                           "seconds_since": -1
                       },
                       "load_60_sec_avg": {
                           "percent_load": -1,
                           "seconds_since": -1
                       },
                       "mod_name": "System CPU"
                   }
               ],
               "customer": "990037",
               "firmware_version": "",
               "ha_role": "true",
               "ha_status": "active",
               "hostname": "tlb1-example-1600.rackspace.com",
               "id": "349737",
               "links": [
                   {
                       "availability": {
                           "href": "https://fe.netsec.rackspace.net/loadbalancers/127.0.0.1/availability",
                           "rel": "related"
                       },
                       "config": {
                           "href": "https://localhost/f5/127.0.0.1/config",
                           "rel": "related"
                       },
                       "device": {
                           "href": "https://fe.netsec.rackspace.net/devices/127.0.0.1",
                           "rel": "alternate"
                       },
                       "lb": {
                           "href": "https://fe.netsec.rackspace.net/f5",
                           "rel": "up"
                       },
                       "monitors": {
                           "href": "https://localhost/f5/127.0.0.1/monitors",
                           "rel": "related"
                       },
                       "nodes": {
                           "href": "https://localhost/f5/127.0.0.1/nodes",
                           "rel": "related"
                       },
                       "pools": {
                           "href": "https://localhost/f5/127.0.0.1/pools",
                           "rel": "related"
                       },
                       "self": {
                           "href": "https://localhost/f5/127.0.0.1",
                           "rel": "self"
                       },
                       "virtuals": {
                           "href": "https://localhost/f5/127.0.0.1/virtuals",
                           "rel": "related"
                       }
                   }
               ],
               "management_ip": "10.12.144.24",
               "model_name": "BIG-IP 1600",
               "os_version": "11.5.4, build: 2.0.291, edition: Hotfix HF2",
               "ram_mem": [
                   {
                       "free_kbytes": "164334",
                       "name": "TMM",
                       "total_kbytes": "4158235",
                       "used_kbytes": "1874854"
                   }
               ],
               "role": "unimplemented",
               "uptime": "23 days,  6:01"
           }
       ]
   }
