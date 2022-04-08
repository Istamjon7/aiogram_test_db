import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC022a414e9daa617a405141603f0f3733'
auth_token = 'ef60c35a61e8b9ede46089e828b7ca9e'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='Test uchun sms. Wanted',
         from_='+998901321921',
         to='+998976705010'
     )

print(message.sid)