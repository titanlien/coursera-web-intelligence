#!/usr/bin/env python
import mincemeat

client = mincemeat.Client()
client.password = "titan"
client.conn("localhost", mincemeat.DEFAULT_PORT)
