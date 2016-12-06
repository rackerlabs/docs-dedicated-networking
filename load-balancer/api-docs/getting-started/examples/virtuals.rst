
Manage virtual servers
~~~~~~~~~~~~~~~~~~~~~~

A virtual server is an IP address and service port combination that exists on
the load balancer to handle content for a website. A virtual server's main
function is to distribute traffic loads to a group of internal, back-end
servers. A Virtual IP, or VIP, is the IP address that is associated with a
virtual server.


Retrieve details for all virtual servers
----------------------------------------

**Example: Retrieve virtual servers cURL request**

.. code::

   curl $BASE_URL/virtuals \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool


**Example: Retrieve virtual servers response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80"
                   }
               },
               "address": "192.168.19.43",
               "addressStatus": "yes",
               "appService": null,
               "auth": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/auth"
               },
               "autoLasthop": "default",
               "bwcPolicy": null,
               "clonePools": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/clone-pools"
               },
               "cmpEnabled": "yes",
               "connectionLimit": 0,
               "description": null,
               "fallbackPersistence": null,
               "gtmScore": 0,
               "id": "VS-50.56.8.43-80",
               "ipForward": "disabled",
               "ipProtocol": "tcp",
               "lastHopPool": null,
               "mask": "255.255.255.255",
               "metadata": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/metadata"
               },
               "mirror": "disabled",
               "mobileAppTunnel": "disabled",
               "nat64": "disabled",
               "partition": "Common",
               "persist": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/persist"
               },
               "policies": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/policies"
               },
               "pool": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/pool"
               },
               "port": {
                   "type": "equal",
                   "value": 80
               },
               "profiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/profiles"
               },
               "rateClass": null,
               "rateLimit": "disabled",
               "rateLimitDstMask": 0,
               "rateLimitMode": "object",
               "rateLimitSrcMask": 0,
               "relatedRules": null,
               "rules": {
                   "RULE_TCL": "RULE_TCL"
               },
               "securityLogProfiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/security-log-profiles"
               },
               "source": "0.0.0.0/0",
               "sourceAddressTranslation": {
                   "pool": "none",
                   "type": "none"
               },
               "sourcePort": "preserve",
               "synCookieStatus": "not-activated",
               "trafficClasses": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/traffic-classes"
               },
               "translateAddress": "enabled",
               "translatePort": "enabled",
               "vlans": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-80/vlans"
               },
               "vsIndex": 23
           },
           {
               "_links": {
                   "self": {
                       "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443"
                   }
               },
               "address": "192.168.19.43",
               "addressStatus": "yes",
               "appService": null,
               "auth": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/auth"
               },
               "autoLasthop": "default",
               "bwcPolicy": null,
               "clonePools": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/clone-pools"
               },
               "cmpEnabled": "yes",
               "connectionLimit": 0,
               "description": null,
               "fallbackPersistence": null,
               "gtmScore": 0,
               "id": "VS-50.56.8.43-443",
               "ipForward": "disabled",
               "ipProtocol": "tcp",
               "lastHopPool": null,
               "mask": "255.255.255.255",
               "metadata": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/metadata"
               },
               "mirror": "disabled",
               "mobileAppTunnel": "disabled",
               "nat64": "disabled",
               "partition": "Common",
               "persist": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/persist"
               },
               "policies": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/policies"
               },
               "pool": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/pool"
               },
               "port": {
                   "type": "equal",
                   "value": 443
               },
               "profiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/profiles"
               },
               "rateClass": null,
               "rateLimit": "disabled",
               "rateLimitDstMask": 0,
               "rateLimitMode": "object",
               "rateLimitSrcMask": 0,
               "relatedRules": null,
               "rules": {
                   "IRULECOASTAL": "IRULE-COASTAL",
                   "IRULEHAWAIIANAIR.COM": "IRULE-HAWAIIANAIR.COM"
               },
               "securityLogProfiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/security-log-profiles"
               },
               "source": "0.0.0.0/0",
               "sourceAddressTranslation": {
                   "pool": "none",
                   "type": "none"
               },
               "sourcePort": "preserve",
               "synCookieStatus": "not-activated",
               "trafficClasses": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/traffic-classes"
               },
               "translateAddress": "enabled",
               "translatePort": "enabled",
               "vlans": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/vlans"
               },
               "vsIndex": 25
           },
           {
               "_links": {
                   "self": {
                       "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP"
                   }
               },
               "address": "0.0.0.0",
               "addressStatus": "yes",
               "appService": null,
               "auth": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/auth"
               },
               "autoLasthop": "default",
               "bwcPolicy": null,
               "clonePools": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/clone-pools"
               },
               "cmpEnabled": "yes",
               "connectionLimit": 0,
               "description": null,
               "fallbackPersistence": null,
               "gtmScore": 0,
               "id": "VS-FORWARDING-ALL-UDP",
               "ipForward": "enabled",
               "ipProtocol": "udp",
               "lastHopPool": null,
               "mask": "any",
               "metadata": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/metadata"
               },
               "mirror": "disabled",
               "mobileAppTunnel": "disabled",
               "nat64": "disabled",
               "partition": "Common",
               "persist": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/persist"
               },
               "policies": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/policies"
               },
               "pool": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/pool"
               },
               "port": {
                   "type": "equal",
                   "value": 0
               },
               "profiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/profiles"
               },
               "rateClass": null,
               "rateLimit": "disabled",
               "rateLimitDstMask": 0,
               "rateLimitMode": "object",
               "rateLimitSrcMask": 0,
               "relatedRules": null,
               "rules": null,
               "securityLogProfiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/security-log-profiles"
               },
               "source": "0.0.0.0/0",
               "sourceAddressTranslation": {
                   "pool": "none",
                   "type": "none"
               },
               "sourcePort": "preserve",
               "synCookieStatus": "not-activated",
               "trafficClasses": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/traffic-classes"
               },
               "translateAddress": "disabled",
               "translatePort": "disabled",
               "vlans": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL-UDP/vlans"
               },
               "vsIndex": 27
           },
           {
               "_links": {
                   "self": {
                       "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL"
                   }
               },
               "address": "0.0.0.0",
               "addressStatus": "yes",
               "appService": null,
               "auth": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/auth"
               },
               "autoLasthop": "default",
               "bwcPolicy": null,
               "clonePools": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/clone-pools"
               },
               "cmpEnabled": "yes",
               "connectionLimit": 0,
               "description": null,
               "fallbackPersistence": null,
               "gtmScore": 0,
               "id": "VS-FORWARDING-ALL",
               "ipForward": "enabled",
               "ipProtocol": "any",
               "lastHopPool": null,
               "mask": "any",
               "metadata": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/metadata"
               },
               "mirror": "enabled",
               "mobileAppTunnel": "disabled",
               "nat64": "disabled",
               "partition": "Common",
               "persist": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/persist"
               },
               "policies": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/policies"
               },
               "pool": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/pool"
               },
               "port": {
                   "type": "equal",
                   "value": 0
               },
               "profiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/profiles"
               },
               "rateClass": null,
               "rateLimit": "disabled",
               "rateLimitDstMask": 0,
               "rateLimitMode": "object",
               "rateLimitSrcMask": 0,
               "relatedRules": null,
               "rules": null,
               "securityLogProfiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/security-log-profiles"
               },
               "source": "0.0.0.0/0",
               "sourceAddressTranslation": {
                   "pool": "none",
                   "type": "none"
               },
               "sourcePort": "preserve",
               "synCookieStatus": "not-activated",
               "trafficClasses": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/traffic-classes"
               },
               "translateAddress": "disabled",
               "translatePort": "disabled",
               "vlans": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-FORWARDING-ALL/vlans"
               },
               "vsIndex": 26
           }
       ]
   }


Create a virtual server
-----------------------

You do not have to specify an IP address when you create a new virtual server.
If you do supply one, the create operation updates an existing virtual. If you
want to create a virtual server specify a different port number.


Th following example creates a server

**Example: Create a virtual server cURL request**

.. code::

   curl $BASE_URL/virtuals \
      -X POST \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
          "ipProtocol": "tcp",
          "description": "Test VIP for LBS",
          "port": {
          "value": 80,
          "type": "equal"
          }
         }' \
      | python -m json.tool

**Example: Create a virtual server response**

.. code::

   {
      "data": {
          "eventId": "fecd23b0-9c7d-4258-8154-d1f4ac80ddeb",
          "eventRef": "/events/fecd23b0-9c7d-4258-8154-d1f4ac80ddeb",
          "resource": "Virtuals",
          "status": "PROCESSING",
          "timestamp": "2016-10-20T15:57:46.0011332Z"
      }
   }

Check the operation results by submitting an event request with the event ID
included in the response.

**Example: Retrieve event information for create virtual server request**

.. code::

   curl $BASE_URL/events/fecd23b0-9c7d-4258-8154-d1f4ac80ddeb \
      -H "X-Auth-Token: $TOKEN" -H "Content-type: application/json" \
      | python -m json.tool

**Example: cURL Retrieve event information response**

.. code::

   {
       "data": [
           {
               "entrytimestamp": "2016-10-20T15:57:46",
               "event_id": "fecd23b0-9c7d-4258-8154-d1f4ac80ddeb",
               "message": "COMPLETED",
               "modifiedtimestamp": "2016-10-20T15:58:00",
               "output": "{\"virtualId\":VS-192.168.19.43-8080,\"poolId\":POOL-192.168.19.43-8080}",
               "status": "200"
           }
       ]
   }


Retrieve details for a virtual server
--------------------------------------

**Example: Retrieve virtual server details cURL request**

.. code::

   curl $BASE_URL/virtuals/VS-50.56.8.43-443 \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool

**Example: Retrieve virtual server details response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443"
                   }
               },
               "address": "192.168.19.43",
               "addressStatus": "yes",
               "appService": null,
               "auth": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/auth"
               },
               "autoLasthop": "default",
               "bwcPolicy": null,
               "cmpEnabled": "yes",
               "connectionLimit": 0,
               "description": null,
               "fallbackPersistence": null,
               "gtmScore": 0,
               "id": "VS-50.56.8.43-443",
               "ipForward": "disabled",
               "ipProtocol": "tcp",
               "lastHopPool": null,
               "mask": "255.255.255.255",
               "mirror": "disabled",
               "mobileAppTunnel": "disabled",
               "nat64": "disabled",
               "partition": "Common",
               "persist": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/persist"
               },
               "policies": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/policies"
               },
               "pool": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/pool"
               },
               "port": {
                   "type": "equal",
                   "value": 443
               },
               "profiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/profiles"
               },
               "rateClass": null,
               "rateLimit": "disabled",
               "rateLimitDstMask": 0,
               "rateLimitMode": "object",
               "rateLimitSrcMask": 0,
               "relatedRules": null,
               "rules": {
                   "IRULECOASTAL": "IRULE-COASTAL",
                   "IRULEHAWAIIANAIR.COM": "IRULE-HAWAIIANAIR.COM"
               },
               "securityLogProfiles": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/security-log-profiles"
               },
               "source": "0.0.0.0/0",
               "sourceAddressTranslation": {
                   "pool": "none",
                   "type": "none"
               },
               "sourcePort": "preserve",
               "synCookieStatus": "not-activated",
               "trafficClasses": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/traffic-classes"
               },
               "translateAddress": "enabled",
               "translatePort": "enabled",
               "vlans": {
                   "href": "https://localhost/f5/127.0.0.1/virtuals/VS-50.56.8.43-443/vlans"
               },
               "vsIndex": 25
           }
       ]
   }


Update an existing virtual server
---------------------------------

When you update an existing virtual server, you must specify the IP address
and port that is associated with the virtual server ID.

**Example: Update an existing virtual server cURL request**

.. code::

   curl $BASE_URL/virtuals/VS-50.56.8.43-443 \
      -X PUT \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
            "address": "192.168.19.43",
            "description": "Super Important HTTPS VIP",
            "port": {
                     "value": 443,
                     "type": "equal"
            },
            "connectionLimit": 99
         }' \
      | python -m json.tool


**Example: Update an existing virtual server cURL response**

.. code::

   {
       "data": {
           "eventId": "12fb38d7-08f6-4ef0-8283-53e908e9f1b6",
           "eventRef": "/events/12fb38d7-08f6-4ef0-8283-53e908e9f1b6",
           "resource": "VS-50.56.8.43-443",
           "status": "PROCESSING",
           "timestamp": "2016-10-20T17:26:22.2531622Z"
       }
   }

Check the operation results by submitting an event request with the event ID
included in the response for update server operation.

**Example: cURL Retrieve event information request**

.. code::

   curl $BASE_URL/events/12fb38d7-08f6-4ef0-8283-53e908e9f1b6 \
      -H "X-Auth-Token: $TOKEN"
      -H "Content-type: application/json" \
      | python -m json.tool

**Example: cURL Retrieve event information response**

.. code::

   {
       "data": [
           {
               "entrytimestamp": "2016-10-20T17:26:22",
               "event_id": "12fb38d7-08f6-4ef0-8283-53e908e9f1b6",
               "message": "COMPLETED",
               "modifiedtimestamp": "2016-10-20T17:26:27",
               "output": "{\"virtualId\":\"VS-50.56.8.43-443\",\"ip\":\"192.168.19.43\"}",
               "status": "200"
           }
       ]
   }
