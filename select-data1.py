from cassandra.cluster import Cluster


cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('livraison')

select_commandes = "SELECT * FROM commandes WHERE statut = 'En cours' ALLOW FILTERING;"
rows = session.execute(select_commandes)


for row in rows:
    print(f"Commande: {row.id_commande}, Statut: {row.statut}, Date: {row.date}, Client: {row.id_client}, Livreur: {row.id_livreur}")
