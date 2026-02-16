#!/bin/bash
# Script pour automatiser les benchmarks

TYPE=${1:-strong}  # strong ou weak

if [ "$TYPE" == "strong" ]; then
    echo "=== Tests Scalabilité Forte ==="
    echo "workers,ntot,temps_ms" > ../data/scalabilite_forte.csv
    
    for workers in 1 2 4 8; do
        echo "Test avec $workers workers..."
        # Lancer workers
        ./launch_workers.sh $workers
        sleep 2  # Attendre que les workers soient prêts
        
        pkill -f WorkerSocket  # Arrêter les workers
    done
    
elif [ "$TYPE" == "weak" ]; then
    echo "=== Tests Scalabilité Faible ==="
    echo "workers,ntot,temps_ms" > ../data/scalabilite_faible.csv
    
    for workers in 1 2 4 8; do
        ntot=$((workers * 16000000))
        echo "Test avec $workers workers, Ntot=$ntot..."
    done
fi

echo "Tests terminés. Résultats dans data/"
