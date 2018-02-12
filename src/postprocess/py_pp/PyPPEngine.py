"""
Python Postprocessing Engine:

The Python post process engine will receive as input: ID, location and the
status (open/closed) for each umbrella. The script itself will be implemented
in a MQTT fashion and it will act as a subscriber to receive the data. It will
then send notifications to the interested users based on the processed data.
Using the post process engine we can isolate the raw data that will be sent by
umbrellas and the gui on wich notifications will appear (Telegram). So, the
system is more flexible and new features (i.e. new interface for notifications)
can be added without modifying the entire platform. This will be the actor in
charge of sending rain warnings to the users.

"""