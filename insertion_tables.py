import uuid
from datetime import datetime
from cassandra.cluster import Cluster

cluster = Cluster(['127.0.0.1'])
session = cluster.connect()
session.set_keyspace('livraison')

insert_client = """
INSERT INTO clients (id_client, nom, email, adresse)
VALUES (%s, %s, %s, %s);
"""
clients = [
    (uuid.uuid4(), "Alice", "alice@example.com", "123 Rue Principale"),
    (uuid.uuid4(), "Bob", "bob@example.com", "456 Avenue Centrale")
]
for client in clients:
    session.execute(insert_client, client)

insert_livreur = """
INSERT INTO livreurs (id_livreur, nom, vehicule, disponibilite)
VALUES (%s, %s, %s, %s);
"""
livreurs = [
    (uuid.uuid4(), "Charlie", "Moto", True),
    (uuid.uuid4(), "Diane", "Voiture", False)
]
for livreur in livreurs:
    session.execute(insert_livreur, livreur)

insert_commande = """
INSERT INTO commandes (id_commande, id_client, id_livreur, statut, date)
VALUES (%s, %s, %s, %s, %s);
"""
commandes = [
    (uuid.uuid4(), clients[0][0], livreurs[0][0], "En cours", datetime.now()),
    (uuid.uuid4(), clients[1][0], livreurs[1][0], "Livré", datetime.now())
]
for commande in commandes:
    session.execute(insert_commande, commande)

print("Données insérées avec succès.")
