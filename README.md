# Whatsapp analysis

The scripts on this repository can be used to extract statistics from Whatsapp group chats. The main application was to analyze messages to celebrate our group chat's ("Tuuli Nousee") 4th anniversary. 

## Dataset

Data comprise of a CSV file of messages exported from Whatsapp. Each row represents one message.

The data contains the following fields:

Variable | Description
--- | ---
Datetime | Date and time in the following format: D.M.YYYY klo hh.mm
Author | The name of the author
Message | The contents of the message or the phrase "<Media jätettiin pois>" in case of a media message

The following variables were derived from the above source data:

Variable | Type | Description
--- | --- | ---
date | datetime | Message date
time | char | Message time
author | char | Message author
message | char | Message contents
message_count | num | Always 1 because each row contains one message. Used for aggregation.
media_count | num | Number of media attached to the message
letter_count | num | Number of letters in the message
word_count | num | Number of words in the message
message_with_emoji | bool | Indicator for messages with at least one emoji
link | list | List of links in the message
link_count | num | Number of links in the message
message_with_link | bool | Indicator for messages with at least one link
weekday | char | Weekday of the message in English
weekend | bool | Indicator for messages sent on a weekend
hour | num | Hour when the message was sent
hour_group | char | Hour group, split by 6 hours

## Analysis

The analysis contains the following sections:

- Messages by author
- Messages by date and time
- Emojis
- Links
- Message contents

## Sources

- https://github.com/MaartenGr/soan
- https://medium.com/towards-artificial-intelligence/whatsapp-group-chat-analysis-using-python-and-plotly-89bade2bc382
