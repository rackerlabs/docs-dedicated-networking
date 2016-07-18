
/acls
-----

Firewall can contain many access control list. Each list can contain
one/many entries.

/acls
~~~~~

-  **get** *(secured)*: The collection of Access Control Lists


/acls/smartacl
~~~~~~~~~~~~~~

-  **post** *(secured)*: Creates ACL in the best matched interaface
   based on Source/Type
   

/acls/{acl\_name}
~~~~~~~~~~~~~~~~~

Access control List contains one or many access control entries

-  **get** *(secured)*: The collection of Access Control Entries
-  **post** *(secured)*: Applies the specified changes to the given
   Access Control Entries

/acls/events/{event\_id}
~~~~~~~~~~~~~~~~~~~~~~~~

-  **get** *(secured)*: The details of the ACL event specified.

/aliases
--------

Deals with naming/aliasing IP Addresses on a firewall. These are one to
one relationship. This will in turn be reflected in other configurations
across the device that may or may not have referenced the IP Address in
question.

/aliases
~~~~~~~~

-  **get** *(secured)*: The collection of Aliases
-  **post** *(secured)*: Applies the specified changes to the given
   Aliases

/aliases/events/{event\_id}
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **get** *(secured)*: The details of the ACL event specified.

/events
-------

Events are used to track asynchronous requests to the firewall. These
events provide status details during the processing of asynchronous
requests. Once an event is in a 'completed' state, the requested change
is effective and applied to the resource.

Events are resource specific.

/events
~~~~~~~

-  **get** *(secured)*: List of all device asynchronous events.

/events/acls
~~~~~~~~~~~~

-  **get** *(secured)*: List of ACL asynchronous events.

/events/aliases
~~~~~~~~~~~~~~~

-  **get** *(secured)*: List of ACL asynchronous events.

/events/groups
~~~~~~~~~~~~~~

-  **get** *(secured)*: List of ACL asynchronous events.

/groups
-------

Group Names

/groups
~~~~~~~

-  **get** *(secured)*: The collection of groups

/groups/events/{event\_id}
~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **get** *(secured)*: The details of the ACL event specified.

/groups/{group\_name}
~~~~~~~~~~~~~~~~~~~~~

-  **get** *(secured)*: The collection of values
-  **post** *(secured)*: Applies the specified changes to the given
   values

/groups/{group\_name}/description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **post** *(secured)*: updates Group description

/groups/{group\_name}/{values}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **get** *(secured)*: The collection of Group Values
-  **post** *(secured)*: Applies the specified changes to the given
   Group Values
