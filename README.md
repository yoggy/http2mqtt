http2mqtt.cgi
====
a mqtt bridge program for Webhook.

How to
----
    $ sudo gem install mqtt
    $ cd /var/www/
    $ git clone https://github.com/yoggy/http2mqtt.git
    $ cd http2mqtt
    $ cp config.yaml.sample config.yaml
    $ vi config.yaml
 
        mqtt_host:      iot.eclipse.org
        mqtt_port:      1883
        mqtt_use_auth:  false
        mqtt_username:  username
        mqtt_password:  password
  
POST data
----

    $ curl -H 'Content-Type:application/json' -d '{"topic":"test/topic/name","message":"12345678"}' https://www.example.com/http2mqtt.cgi

github
----

    https://github.com/yoggy/http2mqtt.cgi

Copyright and license
----
Copyright (c) 2017 yoggy

Released under the [MIT license](LICENSE.txt)
