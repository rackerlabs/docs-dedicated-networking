.. cbd-dgv2-pagination:

==========
Pagination
==========

Pagination provides the ability to limit the size of the returned data in the response 
body as well as retrieve a specified subset of a large data set. Pagination has two 
key concepts: *limit* and *marker*.

-  ``limit`` is the restriction on the maximum number of items for that type that can be returned.

-  ``marker`` is the ID of the last item in the previous list returned.

   The ID is the respective ID for the last cluster, node, or flavor.
   For example, a query could request the next 10 nodes after the node
   “xyz” as follows: ``?limit=10&marker=xyz``. Items displayed are
   sorted by ID.

Pagination applies only to the operations listed in the following table:

+---------+---------------------------------------------+--------------------------------------------+
|  Verb   |                     URI                     |                Description                 |
+=========+=============================================+============================================+
| **GET** | /v2/{tenant\_id}/clusters                   | Lists all clusters for your account.       |
+---------+---------------------------------------------+--------------------------------------------+
| **GET** | /v2/{tenant\_id}/clusters/{clusterId}/nodes | Lists all nodes for the specified cluster. |
+---------+---------------------------------------------+--------------------------------------------+
| **GET** | /v2/{tenant\_id}/flavors                    | Lists all available flavors, including     |
|         |                                             | the drive size and the amount of RAM.      |
+---------+---------------------------------------------+--------------------------------------------+

The default paging limit for all calls is 25 with a maximum of 200.
Requests for more than 200 result in a 400 error.

See the following example of the operation to list paged nodes.

.. _cbd-dgv2-pagination-request:

**Example: List nodes paged request: JSON**

.. code::  

    GET /v2/yourAccountID/clusters/ac111111-2d86-4597-8010-cbe787bbbc41/nodes?limit=2
    X-Auth-Token: yourAuthToken
    Accept: application/json
    Content-Type: application/json

Notice that the preceding paged request example sets the limit to 2 (``?limit=2``), so the example response that follows shows 2 nodes.

.. _cbd-dgv2-pagination-response:

**Example: List nodes paged response: JSON**

.. code::  

    {
        "nodes": [
                  {
                  "id": "000",
                  "created": "2014-08-11T10:10:10Z",
                  "role": "NAMENODE",
                  "name": "NAMENODE-1",
                  "status": "ACTIVE",
                  "addresses": {
                  "public": [
                             {
                             "addr": "168.x.x.3",
                             "version": 4
                             }
                             ],
                  "private": [
                              {
                              "addr": "10.x.x.3",
                              "version": 4
                              }
                              ]
                  },
                  "services": [
                               {
                               "name": "namenode"
                               },
                               {
                               "name": "jobtracker"
                               },
                               {
                               "name": "ssh",
                               "uri": "ssh://user@168.x.x.3"
                               }
                               ],
                  "links": [
                            {
                            "rel": "self",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/000"
                            },
                            {
                            "rel": "bookmark",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/000"
                            }
                            ]
                  },
                  {
                  "id": "aaa",
                  "role": "GATEWAY",
                  "name": "GATEWAY-1",
                  "status": "ACTIVE",
                  "addresses": {
                  "public": [
                             {
                             "addr": "168.x.x.4",
                             "version": 4
                             }
                             ],
                  "private": [
                              {
                              "addr": "10.x.x.4",
                              "version": 4
                              }
                              ]
                  },
                  "services": [
                               {
                               "name": "pig"
                               },
                               {
                               "name": "hive"
                               },
                               {
                               "name": "ssh",
                               "uri": "ssh://user@168.x.x.4"
                               },
                               {
                               "name": "status",
                               "uri": "http://10.x.x.4"
                               },
                               {
                               "name": "hdfs-scp",
                               "uri": "scp://user@168.x.x.4:9022"
                               }
                               ],
                  "links": [
                            {
                            "rel": "self",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/aaa"
                            },
                            {
                            "rel": "bookmark",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/aaa"
                    }
                ]
            }
        ]
    }
     
