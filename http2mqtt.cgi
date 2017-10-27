#!/usr/bin/ruby
# -*- coding: utf-8 -*-
# 
# http2mqtt.cgi - a mqtt bridge program for Webhook.
#
# how to:
#   $ sudo gem install mqtt
#   $ cd /var/www/
#   $ git clone https://github.com/yoggy/http2mqtt.git
#   $ cd http2mqtt
#   $ cp config.yaml.sample config.yaml
#   $ vi config.yaml
#
#       mqtt_host:      iot.eclipse.org
#       mqtt_port:      1883
#       mqtt_use_auth:  false
#       mqtt_username:  username
#       mqtt_password:  password
# 
# post data:
#   $ curl -H 'Content-Type:application/json' -d '{"topic":"test/topic/name","message":"12345678"}' https://www.example.com/http2mqtt.cgi
# 
# github:
#     https://github.com/yoggy/http2mqtt.cgi
#
# license:
#     Copyright (c) 2017 yoggy <yoggy0@gmail.com>
#     Released under the MIT license
#     http://opensource.org/licenses/mit-license.php;
#
require 'mqtt'
require 'json'
require 'yaml'
require 'ostruct'
require 'cgi'
require 'pp'

$stdout.sync = true
Dir.chdir(File.dirname($0))
$conf = OpenStruct.new(YAML.load_file("config.yaml"))

cgi = CGI.new
$json = OpenStruct.new(JSON.parse(cgi.params.keys.first)) # post body

conn_opts = {
  remote_host: $conf.mqtt_host
}

if !$conf.mqtt_port.nil? 
  conn_opts["remote_port"] = $conf.mqtt_port
end

if $conf.mqtt_use_auth == true
  conn_opts["username"] = $conf.mqtt_username
  conn_opts["password"] = $conf.mqtt_password
end

begin
  MQTT::Client.connect(conn_opts) do |c|
    c.publish($json.topic, $json.message)
  end
rescue Exception => e
end

cgi.out("status" => "OK", "type" => "text/plain", "connection" => "close") do
  CGI.escapeHTML($json.to_s)
end


