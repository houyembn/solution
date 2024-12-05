from cassandra.cluster import Cluster
def create_keyspace():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    create_keyspace_query = """
    CREATE KEYSPACE IF NOT EXISTS livraison
    WITH replication = {
        'class': 'SimpleStrategy', 
        'replication_factor': 1
    };
    """
    session.execute(create_keyspace_query)
    print("Keyspace 'livraison' créé avec succès.")

    session.set_keyspace('livraison')
    print("Keyspace 'livraison' sélectionné.")

    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    create_keyspace()
