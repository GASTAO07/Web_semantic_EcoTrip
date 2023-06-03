from rdflib import Graph
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from style import apply_style

# Charger l'image du logo
def load_logo(window):
    # Charger l'image à partir d'un fichier local
    # Pour charger à partir d'une URL, vous devez télécharger d'abord l'image
    image = Image.open('bus.jpg')  # Remplacez 'car_logo.png' par le nom du fichier ou l'URL de votre image

    # Réduire la taille de l'image si nécessaire
    image = image.resize((100, 100), Image.ANTIALIAS)

    # Convertir l'image en image Tkinter
    logo = ImageTk.PhotoImage(image)

    # Créer un label pour l'image
    logo_label = tk.Label(window, image=logo)
    logo_label.image = logo  # Conserver une référence à l'image
    logo_label.pack(pady=10)  # Afficher l'image

# Fonction pour exécuter une requête SPARQL et retourner les résultats sous forme de liste
def execute_sparql_query(g, query):
    results = g.query(query)
    return list(results)

def display_category():
    query = """
    SELECT DISTINCT ?category ?individual WHERE {
        ?individual a ?category .
    }
    """
    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Toutes les catégories")
    window.geometry("800x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("individual", "category")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("individual", anchor=tk.W, width=200)
    table.column("category", anchor=tk.W, width=150)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("individual", text="Individual", anchor=tk.W)
    table.heading("category", text="Category", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        individual = str(result.individual).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        category = str(result.category).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        table.insert("", tk.END, text=str(i+1), values=(individual, category))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

def display_transport_prices():
    query = """
    SELECT ?journey ?transportMode ?price ?duration ?distance ?carbonEmission WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:cost ?price .
      ?journey transport:duration ?duration .
      ?journey transport:distance ?distance .
      ?journey transport:carbonEmission ?carbonEmission .
    }
    """
    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Prix Transports")
    window.geometry("800x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("journey", "transportMode", "price", "duration", "distance", "carbonEmission")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("journey", anchor=tk.W, width=200)
    table.column("transportMode", anchor=tk.W, width=150)
    table.column("price", anchor=tk.W, width=100)
    table.column("duration", anchor=tk.W, width=100)
    table.column("distance", anchor=tk.W, width=100)
    table.column("carbonEmission", anchor=tk.W, width=100)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("journey", text="Journey", anchor=tk.W)
    table.heading("transportMode", text="Transport Mode", anchor=tk.W)
    table.heading("price", text="Price", anchor=tk.W)
    table.heading("duration", text="Duration", anchor=tk.W)
    table.heading("distance", text="Distance", anchor=tk.W)
    table.heading("carbonEmission", text="Carbon Emission", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        journey = str(result.journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        transport_mode = str(result.transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(result.price)
        duration = str(result.duration)
        distance = str(result.distance)
        carbon_emission = str(result.carbonEmission)
        table.insert("", tk.END, text=str(i+1), values=(journey, transport_mode, price, duration, distance, carbon_emission))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)
    
def display_cheapest_transport_prices():
    # Requête SPARQL pour récupérer les trajets avec les prix les moins chers
    query = """
    SELECT ?journey ?transportMode ?price WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:cost ?price .
      FILTER NOT EXISTS {
        ?journey transport:cost ?cheaperPrice .
        ?cheaperJourney rdf:type transport:Journey .
        ?cheaperJourney transport:hasTransportMode ?transportMode .
        ?cheaperJourney transport:cost ?cheaperPrice .
        FILTER (?cheaperPrice < ?price)
      }
    }
    """

    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Création de la fenêtre Tkinter
    window = tk.Toplevel()
    window.title("Le transport le moins cher")
    window.geometry("600x400")

    # Création du widget de tableau pour afficher les résultats
    table = ttk.Treeview(window)
    table["columns"] = ("journey", "transportMode", "price")
    table.column("#0", width=0, stretch=tk.NO)
    table.column("journey", anchor=tk.W, width=200)
    table.column("transportMode", anchor=tk.W, width=200)
    table.column("price", anchor=tk.W, width=100)
    table.heading("#0", text="", anchor=tk.W)
    table.heading("journey", text="Journey", anchor=tk.W)
    table.heading("transportMode", text="Transport Mode", anchor=tk.W)
    table.heading("price", text="Price", anchor=tk.W)

    # Ajout des résultats au tableau
    for i, result in enumerate(results):
        journey = str(result.journey).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        transport_mode = str(result.transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        price = str(result.price)
        table.insert("", tk.END, text=str(i+1), values=(journey, transport_mode, price))

    # Affichage du tableau
    table.pack(fill=tk.BOTH, expand=True)

    # Fonction de fermeture de la fenêtre
    def close_window():
        window.destroy()

    # Bouton de fermeture
    close_button = ttk.Button(window, text="Close", command=close_window)
    close_button.pack(pady=10)

def display_least_polluting_transport():
    # Requête SPARQL pour récupérer le moyen de transport le moins polluant avec son prix
    query = """
    SELECT ?transportMode ?carbonEmission ?price WHERE {
      ?journey rdf:type transport:Journey .
      ?journey transport:hasTransportMode ?transportMode .
      ?journey transport:carbonEmission ?carbonEmission .
      ?journey transport:cost ?price .
    }
    GROUP BY ?transportMode ?carbonEmission ?price
    ORDER BY ASC(?carbonEmission)
    LIMIT 1
    """

    # Exécution de la requête SPARQL
    results = execute_sparql_query(g, query)

    # Récupération du résultat
    if results:
        transport_mode = str(results[0].transportMode).replace("http://www.semanticweb.org/mael2/ontologies/2023/4/transport#", "")
        carbon_emission = str(results[0].carbonEmission)
        price = str(results[0].price)
        message = f"Le transport le moins polluant est le(a) {transport_mode} avec une emission carbonne de {carbon_emission} et un prix de {price}. Valider."

        # Affichage du message dans une boîte de dialogue
        messagebox.showinfo("Transport moins polluant", message)
    else:
        # Affichage d'un message d'erreur si aucun résultat n'est trouvé
        messagebox.showerror("Error", "No data found.")


# Chargement des données RDF
g = Graph()
g.parse("transport.rdf", format="xml")

# Création de la fenêtre principale
window = tk.Tk()
window.title("EcoTrip")
window.geometry("400x300")
window.configure(background='white')

# Charger le logo
load_logo(window)

# Création du conteneur principal
container = ttk.Frame(window)
container.pack(fill=tk.BOTH, expand=True)

# Appliquer le style
apply_style()

# Création des boutons pour afficher les tables
transport_prices_button = ttk.Button(container, text="Prix transports", command=display_transport_prices)
transport_prices_button.pack(pady=10)

least_polluting_transport_button = ttk.Button(container, text="Moins polluant", command=display_least_polluting_transport)
least_polluting_transport_button.pack(pady=10)

transport_categories_button = ttk.Button(container, text="Categories", command=display_category)
transport_categories_button.pack(pady=10)

# Boucle principale de l'interface graphique
window.mainloop()
