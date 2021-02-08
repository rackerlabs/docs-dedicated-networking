Manage monitoring configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can define and manage monitors that verify the health and availability
of a node, pool, or group of nodes in a pool. You must add the monitor to
the load balancer configuration before you can apply it to a load balancer
component.

The following example retrieves the monitors configured in the load balancer.

**Example: Retrieve monitoring configuration cURL request**

.. code::

   curl $BASE_URL/monitors \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool

**Example: Retrieve monitoring configuration cURL response**

.. code::

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


Retrieve monitoring configuration by ID
---------------------------------------
To retrieve the configuration for a specific monitor, submit a request with
that includes the monitor ID as shown in the following example.

**Example: Retrieve list of monitors cURL request**

.. code::

   curl $BASE_URL/monitors/MON-TCP-80 \
       -H "X-Auth-Token: $TOKEN" \
       -H "Content-type: application/json" \
      | python -m json.tool

**Example: Retrieve list of monitors cURL response**

.. code::

   {
       "data": [
           {
               "_links": {
                   "self": {
                       "href": "https://localhost/f5/127.0.0.1/monitors/MON-TCP-80"
                   }
               },
               "address": "any",
               "appService": null,
               "defaultsFrom": "tcp",
               "description": null,
               "id": "MON-TCP-80",
               "interval": 5,
               "ipDscp": 0,
               "manualResume": "disabled",
               "port": {
                   "type": "equal",
                   "value": 80
               },
               "recv": null,
               "recvDisable": null,
               "reverse": "disabled",
               "send": null,
               "timeUntilUp": 0,
               "timeout": 16,
               "transparent": "disabled",
               "type": "tcp",
               "upInterval": 0
           }
       ]
   }

Create a monitor in the load balancer
-------------------------------------

When you add a monitor, include the monitor ID in the URI. Then, pass the
monitor parameter values in the body of the request as shown in the
following example.

**Example: Create a monitor cURL request**

.. code::

   curl $BASE_URL/monitors/MON-TCP-80-LBS_TEST \
      -X POST \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
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
         }' \

         | python -m json.tool


**Example: Create monitoring rule cURL response**

.. code::

   {
      "data": {
          "eventId": "1ced63ff-3a8a-49b4-b25c-70d61d1ed486",
          "eventRef": "/events/1ced63ff-3a8a-49b4-b25c-70d61d1ed486",
          "resource": "MON-TCP-80-LBS_TEST",
          "status": "PROCESSING",
          "timestamp": "2016-10-20T19:13:11.3163362Z"
      }
   }

To review the results,
:ref:`submit an event request <retrieve-event-info>` with the event ID
included in the response to the create monitor operation.

Update monitor
--------------

After you add a monitor to the load balancer, you can update the monitor
configuration as shown in the following example.

**Example: Update a monitor cURL request**

.. code::

   curl $BASE_URL/monitors/MAINTENANCE \
      -X PUT \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      -d '{
            "type": "http",
            "description": "Testing monitor for LBS",
            "interval": 5,
            "recv": "\\{\"deadlocks\":\\{\"healthy\":true\\},\"fileToggle\":\\{\"healthy\":true\\}\\}",
            "send": "GET /healthcheck \\r\\n"
            }' \
            | python -m json.tool

**Example: Update a monitor response**

.. code::

   {
      "data": {
         "eventId": "5e76ecd2-9bac-43ea-a684-172c67fd37e2",
         "eventRef": "/events/5e76ecd2-9bac-43ea-a684-172c67fd37e2",
         "resource": "MAINTENANCE",
         "status": "PROCESSING",
         "timestamp": "2016-10-20T19:25:16.9091902Z"
         }
   }

Check the operation results by submitting an event request with the event ID
included in the response.

**Example: Retrieve event information cURL request**

.. code::

   curl $BASE_URL/events/5e76ecd2-9bac-43ea-a684-172c67fd37e2 \
      -H "X-Auth-Token: $TOKEN"
      -H "Content-type: application/json" \
      | python -m json.tool


**Example: Retrieve event information response**

.. code::

   {
      "data": [
         {
            "entrytimestamp": "2016-10-20T19:25:17",
            "event_id": "5e76ecd2-9bac-43ea-a684-172c67fd37e2",
            "message": "COMPLETED",
            "modifiedtimestamp": "2016-10-20T19:25:25",
            "output": "{\"monitorId\":\"MAINTENANCE\"}",
            "status": "200"
         }
      ]
    }

Delete monitor by ID
--------------------

When you delete a monitor, it will be removed from the load balancer
configuration. If the monitor has been applied to a load balancer component,
it will also be removed from that component.

**Delete monitor rule cURL request**

   curl $BASE_URL/monitors/MAINTENANCE \
      -X DELETE \
      -H "X-Auth-Token: $TOKEN" \
      -H "Content-type: application/json" \
      | python -m json.tool

**Delete monitor rule response**

.. code::

   {
      "data": {
         "eventId": "03514a09-44be-4715-a919-e5494cc48e77",
         "eventRef": "/events/03514a09-44be-4715-a919-e5494cc48e77",
         "resource": "MAINTENANCE",
         "status": "PROCESSING",
         "timestamp": "2016-10-20T19:27:42.1142Z"
         }
   }

   To review the results,
   :ref:`submit an event request <retrieve-event-info>` with the event ID
   included in the response to the delete monitor operation.
