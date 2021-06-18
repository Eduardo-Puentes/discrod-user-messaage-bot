import requests
import time

# Importing the values of the authorization key and the channel server id from other file
import config

# Start counter
base = 16000

# Initialaze loop to increase by 1 the counter and divide it in sets of 100 numbers, and repeat he sets by 40 times
for j in range(40):
    for i in range(100):
        base = base + 1
        # Setting the content of the message
        payload = {
            'content': base
        }

        # Setting the authorization values to send the message
        header = {
            'authorization': config.authKey
        }

        # Execute the post via request to send the message with the header and payload
        r = requests.post(config.serverChannelId,
                          data=payload, headers=header)

        # Wait 1 second before executing again
        time.sleep(1)

    # Wait 1 second before executing again
    time.sleep(5)
