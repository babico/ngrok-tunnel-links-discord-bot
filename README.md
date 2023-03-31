# ngrok-tunnel-links-discord-bot

this discord bot just sending messages your already running ngrok tunnels link to discord channels.

## using

1. Edit the Discord Bot Token, local ngrok API links, the text channels you want to send messages to, and the ngrok tunnels you want to share with these text channels with the sample format in the config.py file.
2. run `python main.py`

## requirements

- python 3

- compatible ngrok.yml file like below

```yml
version: "2"
...
tunnels:
  babico-http:
    proto: http
    addr: 80
  babico-ssh:
    proto: http
    addr: 80
  homeserver-ssh:
    proto: tcp
    addr: 192.168.2.100:22
```
