Exercise - Webserver Log Parser
Write a pattern to capture the values in a log entry using named groups. Each entry consists of the IP address of the requester, the HTTP method, resource, number of bytes, and request duration

Use the following group names: ip, http, resource, bytes, duration

Sample Input:
192.168.0.20 GET /index.html 32504 1.030
192.168.0.55 GET /index.html 32504 0.500
Expected Output (first match shown below):
ip:192.168.0.20
http:GET
resource:/index.html
byteas:32504
duration:1.030


Solution:
(?m)^(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<http>\w+)\s+(?P<resource>/[\w.]+)\s+(?P<bytes>\d+)\s+(?P<duration>\d+\.\d+)$
ip:\g<ip>\nhttp:\g<http>\nresource:\g<resource>\nbyteas:\g<bytes>\nduration:\g<duration>