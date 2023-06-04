import hazelcast


class ValidationRepositoryInMemory:
    def __init__(self):
        self.logged_users = None
        self.client = hazelcast.HazelcastClient(cluster_members=["hazelcast1"])

    def add_user_token(self, uid, token):
        self.logged_users.lock(uid)
        self.logged_users.put(uid, token).result()
        self.logged_users.unlock(uid)

    def add_map_name(self, map_name: str):
        self.logged_users = self.client.get_map(map_name)

    def get_user_token(self, uid):
        return self.logged_users.get(uid).result() if self.logged_users.contains_key(uid).result() else "none"
