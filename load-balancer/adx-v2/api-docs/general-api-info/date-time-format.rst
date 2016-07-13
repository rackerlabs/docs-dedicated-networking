.. _datetime-format:

====================
Date and time format
====================

For the display and consumption of date and time values, the |apiservice| uses 
a date format that complies with ISO 8601.

The system time is expressed as UTC.
 
**Example:** |product name| service date and time format

.. code::  

    yyyy-MM-dd'T'HH:mm:ss.SSSZ

For example, May 19, 2013 at 8:07:08 a.m., UTC-5 would have the following format:

``2013-05-19T08:07:08 -0500``

The following table describes the date and time format codes.

**Explanation of date and time format codes**

+------+----------------------------------------+
| Code | Description                            |
+======+========================================+
| yyyy | Four-digit year                        |
+------+----------------------------------------+
| MM   | Two-digit month                        |
+------+----------------------------------------+
| dd   | Two-digit day of the month             |
+------+----------------------------------------+
| T    | Separator for the date and time        |
+------+----------------------------------------+
| HH   | Two-digit hour of the day (00-23)      |
+------+----------------------------------------+
| mm   | Two-digit minutes of the hour          |
+------+----------------------------------------+
| ss   | Two-digit seconds of the minute        |
+------+----------------------------------------+
| SSS  | Three-digit milliseconds of the second |
+------+----------------------------------------+
| Z    | RFC 822 timezone                       |
+------+----------------------------------------+

