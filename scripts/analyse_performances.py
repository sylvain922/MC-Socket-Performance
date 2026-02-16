import pandas as pd
import matplotlib.pyplot as plt

# SCALABILITÉ FORTE
strong_data = {
    'workers': [1, 2, 4, 8],
    'totalCount_per_worker': [16000000, 8000000, 4000000, 2000000],
    'ntot_total': [16000000, 16000000, 16000000, 16000000],
    'temps_ms': [540, 290, 168, 103]
}

# SCALABILITÉ FAIBLE
weak_data = {
    'workers': [1, 2, 4, 8],
    'totalCount_per_worker': [16000000, 16000000, 16000000, 16000000],
    'ntot_total': [16000000, 32000000, 64000000, 128000000],
    'temps_ms': [540, 586, 672, 776]
}

# ===== SCALABILITÉ FORTE =====
df_strong = pd.DataFrame(strong_data)
df_strong['speedup'] = df_strong['temps_ms'].iloc[0] / df_strong['temps_ms']

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle('Scalabilité Forte (Ntot Total = 16M)', fontsize=16, fontweight='bold')

# Speedup
axes[0].plot(df_strong['workers'], df_strong['speedup'], 'o-',
             label='Speedup mesuré', linewidth=2, markersize=8, color='#2E86AB')
axes[0].plot(df_strong['workers'], df_strong['workers'], '--',
             label='Speedup linéaire idéal', linewidth=2, color='#A23B72')
axes[0].set_xlabel('Nombre de workers', fontsize=12)
axes[0].set_ylabel('Speedup S(p)', fontsize=12)
axes[0].set_title('Speed up')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Temps
axes[1].plot(df_strong['workers'], df_strong['temps_ms'], 'o-',
             linewidth=2, markersize=8, color='#06A77D')
axes[1].set_xlabel('Nombre de workers', fontsize=12)
axes[1].set_ylabel('Temps (ms)', fontsize=12)
axes[1].set_title('Temps d\'exécution')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('scalabilite_forte.png', dpi=300, bbox_inches='tight')
plt.show()

print("="*70)
print("SCALABILITÉ FORTE")
print("="*70)
print(df_strong.to_string(index=False))
print("\n")

# ===== SCALABILITÉ FAIBLE =====
df_weak = pd.DataFrame(weak_data)
df_weak['speedup'] = df_weak['temps_ms'].iloc[0] / df_weak['temps_ms']  # ← AJOUT

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # ← 2 graphiques au lieu de 1
fig.suptitle('Scalabilité Faible (16M points/worker)', fontsize=16, fontweight='bold')

# Speedup
axes[0].plot(df_weak['workers'], df_weak['speedup'], 'o-',
             label='Speedup mesuré', linewidth=2, markersize=8, color='#9B59B6')
axes[0].axhline(y=1.0, color='red', linestyle='--',
                label='Speedup idéal (1.0)', linewidth=1.5)
axes[0].set_xlabel('Nombre de workers', fontsize=12)
axes[0].set_ylabel('Speedup S(p)', fontsize=12)
axes[0].set_title('Speed up')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Temps d'exécution
axes[1].plot(df_weak['workers'], df_weak['temps_ms'], 'o-',
             linewidth=2, markersize=8, color='#F39C12', label='Temps mesuré')
axes[1].axhline(y=df_weak['temps_ms'].iloc[0], color='red',
                linestyle='--', label='Temps idéal constant', linewidth=1.5)
axes[1].set_xlabel('Nombre de workers', fontsize=12)
axes[1].set_ylabel('Temps (ms)', fontsize=12)
axes[1].set_title('Temps d\'exécution')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('scalabilite_faible.png', dpi=300, bbox_inches='tight')
plt.show()

print("="*70)
print("SCALABILITÉ FAIBLE")
print("="*70)
print(df_weak.to_string(index=False))


# Sauvegarder
df_strong.to_csv('resultats_scalabilite_forte.csv', index=False)
df_weak.to_csv('resultats_scalabilite_faible.csv', index=False)

