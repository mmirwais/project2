from locust import HttpLocust, TaskSet, task, between


class TestingTasks(TaskSet):
    # Testing Users
    @task(100)
    def register_user(self):
        self.client.post("/register", {"user_name": "Johnny Test", "email": "thisisatest@gmail.com",
                                       "password": "password"})

    @task(1)
    def increment_karma(self):
        self.client.put("/increment_karma")

    @task(1)
    def decrement_karma(self):
        self.client.put("/decrement_karma")

    @task(1)
    def deactivate_account(self):
        self.client.delete("/deactivate_account/Johhny Test")

    @task(1)
    def update_email(self):
        self.client.put("/update_email")

    # Testing Posts
    @task(1)
    def create_post(self):
        self.client.post("/create_post")

    @task(1)
    def retrieve_post(self):
        self.client.get("/retrieve_post")

    @task(1)
    def retrieve_post_list(self):
        self.client.get("/list_posts/")

    @task(1)
    def delete_post(self):
        self.client.delete("/delete_post/")

    # Testing Votes
    @task(1)
    def up_vote_posts(self):
        self.client.put("/up_vote_post")

    @task(1)
    def down_vote_posts(self):
        self.client.put("/down_vote_post")

    @task(1)
    def list_post_votes(self):
        self.client.get("/list_post_votes/Test")

    @task(1)
    def list_n_post_votes(self):
        self.client.get("/list_n_post_votes/5")

    @task(1)
    def list_post_votes_in_list(self):
        self.client.get("/list_post_votes_in_list/Test")

    # Testing Messages
    @task(1)
    def send_message(self):
        self.client.post("/send_message")

    @task(1)
    def delete_message(self):
        self.client.delete("/delete_message/5")

    @task(1)
    def list_favorite_messsage(self):
        self.client.get("/list_favorite_messages")


class WebsiteWeeb(HttpLocust):
    task_set = TestingTasks
    wait_time = between(1, 2)
