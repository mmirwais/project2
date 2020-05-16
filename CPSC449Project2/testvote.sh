# Upvote a post
curl	--header 'Content-type: application/json' \
	--data @testvote.json \
	http://localhost:5000/up_vote_post

# Downvote a post
curl	--header 'Content-type: application/json' \
	--data @testvote.json \
	http://localhost:5000/down_vote_post

# Report the number of up and down votes
curl	--header 'Content-type: application/json' \
	--data @testvote.json \
	http://localhost:5000/list_post_votes/Test

# List n top-scoring posts
curl	--header 'Content-type: application/json' \
	--data @testvote.json \
	http://localhost:5000/list_n_post_votes/5

# Post-identifying list
curl	--header 'Content-type: application/json' \
	--data @testvote.json \
	http://localhost:5000/list_post_votes_in_list/Test