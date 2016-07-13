.. _cbd-dgv2-limits:

======
Limits
======

All accounts, by default, have a preconfigured set of thresholds (or limits) to manage capacity and prevent abuse of the system. The system recognizes *rate limits* and *absolute limits*. Rate limits are thresholds that are reset after a certain amount of time passes. Absolute limits are fixed.

.. _cbd-dgv2-limits-ratelimits:

Rate limits
~~~~~~~~~~~

Rate limits are specified in both a human-readable wildcard URI and a machine-processable regular expression. The regular expression boundary matcher ``^`` takes effect after the root URI path. For example, the regular expression ``^/v2/clusters`` would match the last portion of the following URI: ``https://dfw.bigdata.api.rackspacecloud.com/v2/clusters``.

The following table specifies the default rate limits for all **GET**, **PUT**,  **DELETE**, and **POST** API operations for clusters.

**Default rate limits**

+-----------------------+----------------+----------------------+--------------+
|         Verb          |      URI       |  Regular expression  |   Default    |
+=======================+================+======================+==============+
| **GET** changes-since | \*/clusters/\* | ^/vd+.d+/clusters.\* | 3 per minute |
+-----------------------+----------------+----------------------+--------------+
| **POST**              | \*/clusters/\* | ^/vd+.d+/clusters.\* | 2 per minute |
+-----------------------+----------------+----------------------+--------------+
| **POST** clusters     | \*/clusters/\* | ^/vd+.d+/clusters.\* | 50 per day   |
+-----------------------+----------------+----------------------+--------------+
| **PUT**               | \*/clusters/\* | ^/vd+.d+/clusters.\* | 2 per minute |
+-----------------------+----------------+----------------------+--------------+
| **DELETE**            | \*/clusters/\* | ^/vd+.d+/clusters.\* | 5 per minute |
+-----------------------+----------------+----------------------+--------------+

Rate limits are applied in order relative to the verb, going from least to most specific. For example, although the threshold for issuing a **POST** request to ``/v2/*`` is 2 per minute, you cannot issue a **POST** request to ``/v2/*`` more than 50 times within a single day.

If you exceed the thresholds established for your account, a 413 (OverLimit) HTTP response is returned with a ``Retry-After`` header to notify the client when it can attempt to try again.

.. _cbd-dgv2-limits-absolute:

Absolute limits
~~~~~~~~~~~~~~~

The following table provides the default values for the absolute limits.

**Absolute limits**

+------------+----------------------------------------------------------------+---------------+
|    Name    |                          Description                           | Default value |
+============+================================================================+===============+
| Node count | Maximum number of allowed data nodes                           |             3 |
+------------+----------------------------------------------------------------+---------------+
| Disk       | Maximum disk capacity across all data nodes, in gigabytes (GB) |          4500 |
+------------+----------------------------------------------------------------+---------------+
| RAM        | Maximum RAM across all data nodes, in gigabytes (GB)           |         23040 |
+------------+----------------------------------------------------------------+---------------+
| VCPUs      | Maximum virtual CPUs across all data nodes                     |             6 |
+------------+----------------------------------------------------------------+---------------+
