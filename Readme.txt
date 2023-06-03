
```
# EcoTrip

EcoTrip est une application Python qui permet de consulter et d'afficher des informations sur les transports publics. 
L'application utilise les données RDF pour extraire les informations sur les prix des transports, les catégories de transports, les émissions de carbone, etc.

## Installation

### Prérequis

Avant d'installer EcoTrip, assurez-vous d'avoir les prérequis suivants installés sur votre système :

- Python 3.x : [Télécharger Python](https://www.python.org/downloads/)

### Étapes d'installation

1. Cloner le dépôt Git :

   ```shell
   $ git clone https://github.com/votre_utilisateur/EcoTrip.git
   ```

2. Accéder au répertoire du projet :

   ```shell
   $ cd EcoTrip
   ```

3. Installer les dépendances :

   ```shell
   $ pip install -r requirements.txt
   ```

   Les dépendances suivantes seront installées :
   
   - rdflib
   - tkinter
   - pillow (PIL)

## Utilisation

Pour exécuter l'application EcoTrip, exécutez la commande suivante depuis le répertoire du projet :

```shell
$ python main.py
```

L'application s'ouvrira avec une interface graphique où vous pourrez utiliser les différentes fonctionnalités pour consulter les prix des transports, les catégories de transports, etc.

## Licence

Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.
```

Assurez-vous de créer un fichier `requirements.txt` qui contient les dépendances nécessaires pour votre projet. Dans votre cas, le contenu du fichier `requirements.txt` serait :

```
rdflib
Pillow
```

J'ai ajouté `Pillow` car c'est la bibliothèque Python qui fournit le module `Image` et `ImageTk` nécessaires pour charger et afficher des images avec PIL.