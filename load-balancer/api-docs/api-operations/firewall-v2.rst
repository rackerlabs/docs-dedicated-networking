**Endpoint**:
https://bpi.rackspacecloud.com/2.0/{tenant\_id}/firewalls/{device\_id}

ACLS
----

Firewall can contain many access control list. Each list can contain
one/many entries.

.. code:: javascript

        GET /acls

The collection of Access Control Lists

*This operation does not accept a request body.*

GET ACLS 200 Response
~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "description": "A list of aliases on the firewall",
      "properties": {
        "items": {
          "type": "array",
          "items": {
            "$ref": "#/schemas/alias.json"
          }
        }
      },
      "required": [
        "items"
      ]
    }

**Example**

.. code:: javascript

    [
      "101",
      "101",
      "myacl"
    ]

Smart ACL
---------

Smart ACL

.. code:: javascript

        POST /acls/smartacl

Creates ACL in the best matched interaface based on Source/Type

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "properties": {
      "source_type": "single/group",
      "Source": "IP Block/Group Name",
        "create": {
          "type": "array",
          "items": {
            "$ref": "alias.json"
          }
        },
        "delete": {
          "type": "array",
          "items": {
            "$ref": "alias.json"
          }
        }
      },
      "minProperties": 1,
      "additionalProperties": false
    }

POST Smart ACL 202 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request has been accepted for processing, but the processing has not
been completed.

**Example**

.. code:: javascript

    {
        "id": "cac06496-583f-11e5-885d-feff819cdc9f",
        "ref": "/acls/events/cac06496-583f-11e5-885d-feff819cdc9f",
        "type": "Creating Smart ACls",
        "resource": "Smart ACLs",
        "status": "PROCESSING",
        "message": "Creating Smart Acls",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      }

ACL Access Control
------------------

Access control List contains one or many access control entries

.. code:: javascript

        GET /acls/{acl_name}

**Uri Parameters:**

acl\_name

.. code:: javascript

    {
        required: true,
        type: string
    }

The collection of Access Control Entries

*This operation does not accept a request body.*

GET ACL Access Control 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "title": "ace",
      "type": "object",
      "properties": {
        "action": {
          "type": "string",
          "enum": [
            "permit",
            "deny"
          ]
        },
        "line": {
          "type": "integer",
          "minimum": 1,
          "maximum": 25000
        },
        "protocol": {
          "$ref": "protocol.json"
        },
        "source": {
          "$ref": "ace-target.json"
        },
        "destination": {
          "$ref": "ace-target.json"
        },
        "icmp" : {
          "type" : "object",
          "properties" : {
            "type": {
              "enum": [
                "single",
                "group"
              ]
            },
            "value": {
              "type": "string"
            }
          }
        }
      },
      "required": [
        "action",
        "protocol",
        "source",
        "destination"
      ]
    }

**Example**

.. code:: javascript

    [
      {
        "line": 1,
        "active": true,
        "hitCount": 5,
        "action": "permit",
        "protocol": {
          "type": "single",
          "value": "ip"
        },
        "source": {
          "type": "single",
          "value": "10.1.5.4/32",
          "port": {
            "type": "any",
            "value": "any"
          }
        },
        "destination": {
          "type": "any",
          "value": "any",
          "port": {
            "type": "any",
            "value": "any"
          }
        }
      },
      {
        "line": 2,
        "active": true,
        "hitCount": 5,
        "action": "deny",
        "protocol": {
          "type": "group",
          "value": "smtp-group"
        },
        "source": {
          "type": "any",
          "value": "any",
          "port": {
            "type": "single",
            "value": 25
          }
        },
        "destination": {
          "type": "any",
          "value": "any",
          "port": {
            "type": "single",
            "value": 25
          }
        }
      },
      {
        "line": 2,
        "active": true,
        "hitCount": 5,
        "action": "deny",
        "protocol": {
          "type": "group",
          "value": "smtp-group"
        },
        "source": {
          "type": "any",
          "value": "any",
          "port": {
            "type": "single",
            "value": 25
          }
        },
        "destination": {
          "type": "any",
          "value": "any",
          "port": {
            "type": "single",
            "value": 25
          }
        }
      }
    ]

ACL Access Control
------------------

Access control List contains one or many access control entries

.. code:: javascript

        POST /acls/{acl_name}

**Uri Parameters:**

acl\_name

.. code:: javascript

    {
        required: true,
        type: string
    }

Applies the specified changes to the given Access Control Entries

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "Post ace",
      "type": "object",
      "properties": {
        "create": {
          "type": "array",
          "items": {
            "$ref": "ace.json"
          },
          "minLength": 1
        },
        "delete": {
          "type": "array",
          "items": {
            "$ref": "ace.json"
          },
          "minLength": 1
        }
      },
      "minProperties": 1,
      "additionalProperties": false
    }

POST ACL Access Control 202 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request has been accepted for processing, but the processing has not
been completed.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "Post ace",
      "type": "object",
      "properties": {
        "create": {
          "type": "array",
          "items": {
            "$ref": "ace.json"
          },
          "minLength": 1
        },
        "delete": {
          "type": "array",
          "items": {
            "$ref": "ace.json"
          },
          "minLength": 1
        }
      },
      "minProperties": 1,
      "additionalProperties": false
    }

**Example**

.. code:: javascript

    {
      "id": "64736cc8-5813-11e5-885d-feff819cdc9f",
      "ref": "/acls/events/4736cc8-5813-11e5-885d-feff819cdc9f",
      "type": "Create ACL",
      "resource": "101",
      "status": "PROCESSING",
      "message": "Updating the ACEs for the given ACL",
      "entry_timestamp": "2015-04-01T10:05:01.55Z",
      "completed_timestamp": ""
    }

Event Aliases
-------------

Events are used to track asynchronous requests to the firewall. These
events provide status details during the processing of asynchronous
requests. Once an event is in a 'completed' state, the requested change
is effective and applied to the resource.

Events are resource specific.

.. code:: javascript

        GET /events

List of all device asynchronous events.

*This operation does not accept a request body.*

GET Event Aliases 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "events",
      "type": "object",
      "description": "List of async events for the firewall device.",
      "properties": {
        "items": {
          "type": "array",
          "items": {
            "$ref": "event.json"
          }
        }
      },
      "required": [
        "items"
      ]
    }

**Example**

.. code:: javascript

    [
      {
        "event_id": "64736796-5813-11e5-885d-feff819cdc9f",
        "status": "200",
        "message": "Processing",
        "timestamp": "2015-04-01T10:05:01.55Z"
      },
      {
        "event_id": "64736bba-5813-11e5-885d-feff819cdc9f",
        "status": "200",
        "message": "Processing",
        "timestamp": "2015-04-01T10:05:01.55Z"
      },
      {
        "event_id": "64736cc8-5813-11e5-885d-feff819cdc9f",
        "status": "200",
        "message": "Processing",
        "timestamp": "2015-04-01T10:05:01.55Z"
      }
    ]

ACL Events
----------

.. code:: javascript

        GET /events/acls

List of ACL asynchronous events.

*This operation does not accept a request body.*

GET ACL Events 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "events",
      "type": "object",
      "description": "List of async events for the firewall device.",
      "properties": {
        "items": {
          "type": "array",
          "items": {
            "$ref": "event.json"
          }
        }
      },
      "required": [
        "items"
      ]
    }

**Example**

.. code:: javascript

    [
      {
        "id": "64736cc7-5813-11e5-885d-feff819cdc9f",
        "ref": "/acls/events/64736cc7-5813-11e5-885d-feff819cdc9f",
        "type": "EDIT ACL",
        "resource": "101",
        "status": "PROCESSING",
        "message": "Updating the ACEs for the given ACL",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "64736cc6-5813-11e5-885d-feff819cdc9f",
        "ref": "/acls/events/64736cc6-5813-11e5-885d-feff819cdc9f",
        "type": "GET ACL LIST",
        "resource": "",
        "status": "PROCESSING",
        "message": "Requesting all ACLs from the device",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "64736cc5-5813-11e5-885d-feff819cdc9f",
        "ref": "/acls/events/64736cc5-5813-11e5-885d-feff819cdc9f",
        "type": "EDIT ACL",
        "resource": "104",
        "status": "COMPLETED",
        "message": "ACL modification completed successfully",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": "2015-04-01T10:05:02.30Z"
      }
    ]

ACLS Event By Event ID
----------------------

Returns an event provided an event id.

.. code:: javascript

        GET /events/acls/{event_id}

**Uri Parameters:**

event\_id

.. code:: javascript

    {
        required: true,
        type: string
    }

The details of the ACL event specified.

*This operation does not accept a request body.*

GET ACLS Event By Event ID 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "event",
      "type": "object",
      "description": "An async event object on the firewall device.",
      "properties": {
        "id": {
          "type": "string"
        },
        "ref": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "resource": {
          "type": "string"
        },
        "status": {
          "type": "integer"
        },
        "message": {
          "type": "string"
        },
        "entry_timestamp": {
          "type": "string"
        },
        "completed_timestamp": {
          "type": "string"
        }
      }
    }

**Example**

.. code:: javascript

    [
      {
        "id": "64736cc7-5813-11e5-885d-feff819cdc9f",
        "ref": "/acls/events/64736cc7-5813-11e5-885d-feff819cdc9f",
        "type": "EDIT ACL",
        "resource": "101",
        "status": "PROCESSING",
        "message": "Updating the ACEs for the given ACL",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "64736cc6-5813-11e5-885d-feff819cdc9f",
        "ref": "/acls/events/64736cc6-5813-11e5-885d-feff819cdc9f",
        "type": "GET ACL LIST",
        "resource": "",
        "status": "PROCESSING",
        "message": "Requesting all ACLs from the device",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "64736cc5-5813-11e5-885d-feff819cdc9f",
        "ref": "/acls/events/64736cc5-5813-11e5-885d-feff819cdc9f",
        "type": "EDIT ACL",
        "resource": "104",
        "status": "COMPLETED",
        "message": "ACL modification completed successfully",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": "2015-04-01T10:05:02.30Z"
      }
    ]

Events Aliases
--------------

.. code:: javascript

        GET /events/aliases

List of ACL asynchronous events.

*This operation does not accept a request body.*

GET Events Aliases 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "events",
      "type": "object",
      "description": "List of async events for the firewall device.",
      "properties": {
        "items": {
          "type": "array",
          "items": {
            "$ref": "event.json"
          }
        }
      },
      "required": [
        "items"
      ]
    }

**Example**

.. code:: javascript

    [
      {
        "id": "8c8cc43e-5831-11e5-885d-feff819cdc9f",
        "ref": "/aliases/events/8c8cc43e-5831-11e5-885d-feff819cdc9f",
        "type": "Create Aliases",
        "resource": "TestAlias",
        "status": "PROCESSING",
        "message": "Creating new Aliases",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "8c8cc6be-5831-11e5-885d-feff819cdc9f",
        "ref": "/aliases/events/8c8cc6be-5831-11e5-885d-feff819cdc9f",
        "type": "GET Aliases",
        "resource": "",
        "status": "PROCESSING",
        "message": "Getting list of All Aliases",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "8c8cc9de-5831-11e5-885d-feff819cdc9f",
        "ref": "/aliases/events/8c8cc9de-5831-11e5-885d-feff819cdc9f",
        "type": "Create Aliases",
        "resource": "Test",
        "status": "COMPLETED",
        "message": "Creating New Aliases",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": "2015-04-01T10:05:02.30Z"
      }
    ]

Aliases Event
-------------

Returns an event provided an event id.

.. code:: javascript

        GET /events/aliases/{event_id}

**Uri Parameters:**

event\_id

.. code:: javascript

    {
        required: true,
        type: string
    }

The details of the ACL event specified.

*This operation does not accept a request body.*

GET Aliases Event 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "event",
      "type": "object",
      "description": "An async event object on the firewall device.",
      "properties": {
        "id": {
          "type": "string"
        },
        "ref": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "resource": {
          "type": "string"
        },
        "status": {
          "type": "integer"
        },
        "message": {
          "type": "string"
        },
        "entry_timestamp": {
          "type": "string"
        },
        "completed_timestamp": {
          "type": "string"
        }
      }
    }

**Example**

.. code:: javascript

    {
        "id": "8c8cc9de-5831-11e5-885d-feff819cdc9f",
        "ref": "/aliases/events/8c8cc9de-5831-11e5-885d-feff819cdc9f",
        "type": "Create ALiases",
        "resource": "Test",
        "status": "COMPLETED",
        "message": "Creating New Aliases",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": "2015-04-01T10:05:02.30Z"
      }

Group Events
------------

.. code:: javascript

        GET /events/groups

List of ACL asynchronous events.

*This operation does not accept a request body.*

GET Group Events 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "events",
      "type": "object",
      "description": "List of async events for the firewall device.",
      "properties": {
        "items": {
          "type": "array",
          "items": {
            "$ref": "event.json"
          }
        }
      },
      "required": [
        "items"
      ]
    }

**Example**

.. code:: javascript

    [
      {
        "id": "cac06496-583f-11e5-885d-feff819cdc9f",
        "ref": "/groups/events/cac06496-583f-11e5-885d-feff819cdc9f",
        "type": "Create Group",
        "resource": "TestGroup",
        "status": "PROCESSING",
        "message": "Creating new group",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "cac06496-583f-11e5-885d-feff819cdc9f",
        "ref": "/groups/events/cac06496-583f-11e5-885d-feff819cdc9f",
        "type": "Creating Group Values",
        "resource": "Group Values",
        "status": "PROCESSING",
        "message": "Creating New Group Values",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      },
      {
        "id": "cac06874-583f-11e5-885d-feff819cdc9f",
        "ref": "/groups/events/cac06874-583f-11e5-885d-feff819cdc9f",
        "type": "Getting Group Values",
        "resource": "",
        "status": "COMPLETED",
        "message": "Getting Group Values",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": "2015-04-01T10:05:02.30Z"
      }
    ]

Groups Event
------------

Returns an event provided with an event id.

.. code:: javascript

        GET /events/groups/{event_id}

**Uri Parameters:**

event\_id

.. code:: javascript

    {
        required: true,
        type: string
    }

The details of the ACL event specified.

*This operation does not accept a request body.*

GET Groups Event 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "event",
      "type": "object",
      "description": "An async event object on the firewall device.",
      "properties": {
        "id": {
          "type": "string"
        },
        "ref": {
          "type": "string"
        },
        "type": {
          "type": "string"
        },
        "resource": {
          "type": "string"
        },
        "status": {
          "type": "integer"
        },
        "message": {
          "type": "string"
        },
        "entry_timestamp": {
          "type": "string"
        },
        "completed_timestamp": {
          "type": "string"
        }
      }
    }

**Example**

.. code:: javascript

    {
        "id": "cac06496-583f-11e5-885d-feff819cdc9f",
        "ref": "/groups/events/cac06496-583f-11e5-885d-feff819cdc9f",
        "type": "Create Group",
        "resource": "TestGroup",
        "status": "PROCESSING",
        "message": "Creating new group",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      }

Group Names
-----------

Group Names

.. code:: javascript

        GET /groups

The collection of groups

*This operation does not accept a request body.*

GET Group Names 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "description": "The named group properties",
      "properties": {
        "id": {
          "type": "string"
        },
        "type": {
          "type": "string",
          "enum": [
            "network",
            "icmp-type"
          ]
        },
        "description": {
          "type": "string"
        },
        "values": {
          "$ref": "link.json"
        }
      },
      "required": [
        "id",
        "type",
        "values"
      ]

**Example**

.. code:: javascript

    {
      "id": "icmp-allowed",
      "type": "icmp-type",
      "description": "\"These are the ICMP types Rackspace allows by default\"",
      "values": {
        "href": "http://localhost:8000/v2/firewalls/349764/groups/icmp-allowed/values"
      }
    }

Group Name
----------

.. code:: javascript

        GET /groups/{group_name}

**Uri Parameters:**

group\_name

.. code:: javascript

    {
        required: true,
        type: string
    }

The collection of values

*This operation does not accept a request body.*

GET Group Name 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "description": "The named group properties",
      "properties": {
        "id": {
          "type": "string"
        },
        "type": {
          "type": "string",
          "enum": [
            "network",
            "icmp-type"
          ]
        },
        "description": {
          "type": "string"
        },
        "values": {
          "$ref": "link.json"
        }
      },
      "required": [
        "id",
        "type",
        "values"
      ]
    }

**Example**

.. code:: javascript

    {
      "id": "icmp-allowed",
      "type": "icmp-type",
      "description": "\"These are the ICMP types Rackspace allows by default\"",
      "values": {
        "href": "http://localhost:8000/v2/firewalls/349764/groups/icmp-allowed/values"
      }
    }

Group Name
----------

.. code:: javascript

        POST /groups/{group_name}

**Uri Parameters:**

group\_name

.. code:: javascript

    {
        required: true,
        type: string
    }

Applies the specified changes to the given values

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "description": "The named group properties",
      "properties": {
        "name": {
          "type": "string"
        },
        "type": {
          "type": "string",
          "enum": [
            "network",
            "icmp-type"
          ]
        },
        "description": {
          "type": "string"
        },
        "values": {
          "type": "array",
          "items": {
            "$ref": "group-object.json"
          }
        }
      },
      "required": [
        "name",
        "type",
        "values"
      ]
    }

POST Group Name 202 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request has been accepted for processing, but the processing has not
been completed.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "description": "The named group properties",
      "properties": {
        "name": {
          "type": "string"
        },
        "type": {
          "type": "string",
          "enum": [
            "network",
            "icmp-type"
          ]
        },
        "description": {
          "type": "string"
        },
        "values": {
          "type": "array",
          "items": {
            "$ref": "group-object.json"
          }
        }
      },
      "required": [
        "name",
        "type",
        "values"
      ]
    }

**Example**

.. code:: javascript

    {
        "id": "cac06496-583f-11e5-885d-feff819cdc9f",
        "ref": "/groups/events/cac06496-583f-11e5-885d-feff819cdc9f",
        "type": "Create Group",
        "resource": "TestGroup",
        "status": "PROCESSING",
        "message": "Creating new group",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      }

.. code:: javascript

        POST /groups/{group_name}/description

**Uri Parameters:**

group\_name

.. code:: javascript

    {
        required: true,
        type: string
    }

updates Group description

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "properties": {
        "description": {
          "type": "string"
        }
      },
      "minProperties": 1,
      "additionalProperties": false
    }

POST 202 Response
~~~~~~~~~~~~~~~~~

The request has been accepted for processing, but the processing has not
been completed.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "description": "The named group properties",
      "properties": {
        "description": {
          "type": "string"
        },
        "values": {
          "type": "array",
          "items": {
            "$ref": "group-object.json"
          }
        }
      },
      "required": [
        "name",
        "type",
        "values"
      ]
    }

**Example**

.. code:: javascript

    {
        "id": "cac06490-583f-11e5-885d-feff819cdc9ef",
        "ref": "/groups/events/cac06496-583f-11e5-885d-feff819cdc9f",
        "type": "Group Description",
        "resource": "TestGroup",
        "status": "PROCESSING",
        "message": "Update Group Description",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      }

Group Values
------------

.. code:: javascript

        GET /groups/{group_name}/{values}

**Uri Parameters:**

group\_name

.. code:: javascript

    {
        required: true,
        type: string
    }

values

.. code:: javascript

    {
        required: true,
        type: string
    }

The collection of Group Values

*This operation does not accept a request body.*

GET Group Values 200 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Successfully processed the request.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "type": "object",
      "description": "The Array of Values contained within the Group",
      "properties": {
        "items": {
          "type": "array",
          "items": {
            "$ref": "group-object.json"
          }
        }
      },
      "required": [
        "items"
      ]
    }

**Example**

.. code:: javascript

     [
        {
          "type": "network-object",
          "value": "64.39.0.0/23"
        },
        {
          "type": "group-object",
          "value": "MyOtherIcmp-Allowed"
        }
      ]

Group Values
------------

.. code:: javascript

        POST /groups/{group_name}/{values}

**Uri Parameters:**

group\_name

.. code:: javascript

    {
        required: true,
        type: string
    }

values

.. code:: javascript

    {
        required: true,
        type: string
    }

Applies the specified changes to the given Group Values

*This operation accepts a request body:*

**Request**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "Post ace",
      "type": "object",
      "properties": {
        "create": {
          "type": "array",
          "items": {
            "$ref": "ace.json"
          },
          "minLength": 1
        },
        "delete": {
          "type": "array",
          "items": {
            "$ref": "ace.json"
          },
          "minLength": 1
        }
      },
      "minProperties": 1,
      "additionalProperties": false
    }

POST Group Values 202 Response
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The request has been accepted for processing, but the processing has not
been completed.

**Schema**

.. code:: javascript

    {
      "$schema": "http://json-schema.org/draft-04/schema#",
      "id": "groupValuesPost",
      "type": "object",
      "properties": {
        "create": {
          "type": "array",
          "items": {
            "$ref": "group-object.json"
          },
          "minLength": 1
        },
        "delete": {
          "type": "array",
          "items": {
            "$ref": "group-object.json"
          },
          "minLength": 1
        }
      },
      "minProperties": 1,
      "additionalProperties": false
    }

**Example**

.. code:: javascript

    {
        "id": "cac06496-583f-11e5-885d-feff819cdc9f",
        "ref": "/groups/events/cac06496-583f-11e5-885d-feff819cdc9f",
        "type": "Creating Group Values",
        "resource": "Group Values",
        "status": "PROCESSING",
        "message": "Creating New Group Values",
        "entry_timestamp": "2015-04-01T10:05:01.55Z",
        "completed_timestamp": ""
      }

