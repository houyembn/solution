from cassandra.cluster import Cluster
import uuid

def delete_client():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('livraison')

    delete_client = "DELETE FROM clients WHERE id_client = %s;"

    client_id_to_delete = uuid.UUID("5b0e940b-c45b-4757-b285-df5f87f06f2b") 

    session.execute(delete_client, [client_id_to_delete])
    print("Client supprimé.")


delete_client()
