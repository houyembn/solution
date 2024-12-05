from cassandra.cluster import Cluster
def create_tables():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.set_keyspace('livraison')

    create_clients = """
    CREATE TABLE IF NOT EXISTS clients (
        id_client UUID PRIMARY KEY,
        nom TEXT,
        email TEXT,
        adresse TEXT
    );
    """
    session.execute(create_clients)

    create_commandes = """
    CREATE TABLE IF NOT EXISTS commandes (
        id_commande UUID PRIMARY KEY,
        id_client UUID,
        id_livreur UUID,
        statut TEXT,
        date TIMESTAMP
    );
    """
    session.execute(create_commandes)

    create_livreurs = """
    CREATE TABLE IF NOT EXISTS livreurs (
        id_livreur UUID PRIMARY KEY,
        nom TEXT,
        vehicule TEXT,
        disponibilite BOOLEAN
    );
    """
    session.execute(create_livreurs)

    print("Tables créées avec succès.")

if __name__ == "__main__":
    create_tables()
