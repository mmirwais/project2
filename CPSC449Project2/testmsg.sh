# Send a message
curl	--header 'Content-type: application/json' \
	--data @testmsg.json \
	http://localhost:5000/send_message

# Delete a message
curl	--header 'Content-type: application/json' \
	--data @testmsg.json \
	http://localhost:5000/delete_message

# Show 'Favorite' messages
curl	--header 'Content-type: application/json' \
	--data @testmsg.json \
	http://localhost:5000/list_favorite_messages