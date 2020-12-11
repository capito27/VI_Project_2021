# Movies Statistics
Fortunato Filipe et Dévaud Guillaume

## Récupération des datasets

Avant de lancer le projet, il faut récurpérer les deux datasets utilisés dans le projet, disponibles à cette addresse [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/) :

1. Le dataset [MovieLens 25M](http://files.grouplens.org/datasets/movielens/ml-25m.zip), le contenu du sous-dossier "ml-25m" doit être décompressé dans le dossier `backend/static/dataset/big`
2. Le dataset [MovieLens Latest Small](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip), le contenu du sous-dossier "ml-latest-small" doit être décompressé dans le dossier `backend/static/dataset/small`

## Lancement

Pour démarrer le projet, il faut tout d'abord installer les dépendances du serveur backend, ent ensuite le démarrer avec les commandes suivantes:
```bash
cd ./backend
pip install -r requirements.txt
python app.py
```

Puis pour installer et démarrer la partie frontend les commandes suivantes. Si la page de l'application ne s'est pas ouverte automatiquement, ouvrez ce lien [http://localhost:8080](http://localhost:8080)
```bash
cd ./frontend
npm install
npm start
```


