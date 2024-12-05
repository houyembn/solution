from cassandra.cluster import Cluster
import uuid

def update_commande_status():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('livraison')

    update_statut = """
    UPDATE commandes
    SET statut = 'Livré'
    WHERE id_commande = %s;
    """


    commande_id = uuid.UUID("123e4567-e89b-12d3-a456-426614174000") 

    session.execute(update_statut, [commande_id])
    print("Statut de la commande mis à jour.")

update_commande_status()
