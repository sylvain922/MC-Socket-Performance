# Évaluation de Performances - Monte Carlo Master-Worker Socket - Sylvain COUTURIER

## Description
Implémentation parallèle de l'algorithme Monte Carlo pour le calcul de π 
utilisant une architecture Master-Worker basée sur des sockets TCP/IP Java.

## Structure du Projet
- `src/` : Code source Java (Master et Worker)
- `scripts/` : Scripts d'automatisation des tests
- `data/` : Résultats expérimentaux bruts (CSV) + Graphiques et analyses

## Compilation

```bash
cd src/
javac MasterSocket.java WorkerSocket.java
```


## Utilisation des Scripts d'Automatisation

### Lancer N workers automatiquement

```bash
./scripts/launch_workers.sh 8    # Lance 8 workers (ports 25545-25552)
./scripts/launch_workers.sh 4    # Lance 4 workers
./scripts/launch_workers.sh      # Lance 8 workers par défaut
```


### Arrêter tous les workers

```bash
pkill -f WorkerSocket
```


### Exécuter les benchmarks complets

```bash
cd scripts/
./run_benchmarks.sh strong   # Tests scalabilité forte (Ntot = 16M fixe)
./run_benchmarks.sh weak     # Tests scalabilité faible (16M points/worker)
```

Les résultats sont automatiquement sauvegardés dans `data/scalabilite_forte.csv` et `data/scalabilite_faible.csv`.

### Générer les graphiques d'analyse

```bash
python3 scripts/analyse_performances.py
```

Génère automatiquement :

- `data/scalabilite_forte.png`
- `data/scalabilite_faible.png`
