from cassandra.cluster import Cluster

# Connexion à Cassandra
cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('livraison')

def fetch_and_display(query):
    rows = session.execute(query)
    for row in rows:
        print(row)

print("Clients :")
fetch_and_display("SELECT * FROM clients;")


print("\nLivreurs :")
fetch_and_display("SELECT * FROM livreurs;")


print("\nCommandes :")
fetch_and_display("SELECT * FROM commandes;")
