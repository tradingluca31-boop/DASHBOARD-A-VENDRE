# 🚀 Quick Start Guide - Trading Dashboard Pro

**Get your professional trading dashboard running in 5 minutes!**

---

## ⚡ Installation rapide

### Étape 1: Setup automatique

Double-cliquez sur **`SETUP.bat`** dans le dossier TradingDashboardPro

Cela va:
- ✅ Vérifier Python
- ✅ Créer l'environnement virtuel `venv_dashboard`
- ✅ Installer toutes les dépendances
- ✅ Créer le fichier `.env` de configuration

### Étape 2: Lancer le dashboard

Double-cliquez sur **`START_DASHBOARD.bat`**

Le dashboard s'ouvrira automatiquement à: **http://localhost:8050**

---

## 📋 Installation manuelle (alternative)

Si les fichiers .bat ne fonctionnent pas, suivez ces étapes:

### Windows

```bash
# 1. Créer environnement virtuel
cd C:\Users\lbye3\Desktop\TradingDashboardPro
python -m venv venv_dashboard

# 2. Activer l'environnement
venv_dashboard\Scripts\activate

# 3. Installer dépendances
pip install -r requirements.txt

# 4. Lancer le dashboard
python app.py
```

### Linux/Mac

```bash
# 1. Créer environnement virtuel
cd ~/TradingDashboardPro
python3 -m venv venv_dashboard

# 2. Activer l'environnement
source venv_dashboard/bin/activate

# 3. Installer dépendances
pip install -r requirements.txt

# 4. Lancer le dashboard
python app.py
```

---

## 🎯 Premiers pas

### 1. Accéder au dashboard

Ouvrir votre navigateur: **http://localhost:8050**

### 2. Uploader des données

Dans la page d'accueil:

1. Cliquez sur la zone "Drag & Drop or Click to Upload"
2. Sélectionnez un fichier:
   - **ZIP** contenant `training_stats.json`
   - **JSON** direct avec données de checkpoints
   - **CSV/Excel** avec données tabulaires

### 3. Exemple de format JSON

```json
[
  {
    "timestep": 50000,
    "balance": 10500,
    "roi": 5.0,
    "total_pnl": 500,
    "total_trades": 25,
    "win_rate": 60.0,
    "profit_factor": 1.8,
    "sharpe_ratio": 1.2,
    "max_drawdown_pct": -4.5
  }
]
```

### 4. Explorer les pages

- **Home**: Vue d'ensemble des performances
- **Analytics**: Métriques avancées (Sharpe, Sortino, VaR)
- **Comparison**: Comparer plusieurs agents
- **Settings**: Préférences et export

---

## ⚙️ Configuration

### Fichier `.env`

Le fichier `.env` contient toute la configuration. Éditez-le pour:

**Mode développement** (par défaut):
```env
DEBUG_MODE=True
ENABLE_AUTH=False
PORT=8050
```

**Mode production** (pour vendre):
```env
DEBUG_MODE=False
ENABLE_AUTH=True
PORT=8050
APP_SECRET_KEY=votre-clé-secrète-forte
```

### Générer une clé secrète

```python
import secrets
print(secrets.token_urlsafe(32))
```

Copiez le résultat dans `APP_SECRET_KEY` dans `.env`

---

## 🔐 Activer l'authentification (pour vendre)

### 1. Générer un hash de mot de passe

```python
# Activez l'environnement virtuel d'abord!
python

>>> from utils.auth import AuthManager
>>> auth = AuthManager()
>>> hashed = auth.hash_password("votre-mot-de-passe")
>>> print(hashed)
```

### 2. Copier le hash dans `.env`

```env
ENABLE_AUTH=True
ADMIN_USERNAME=admin
ADMIN_PASSWORD_HASH=le-hash-copié-ci-dessus
```

### 3. Redémarrer le dashboard

Les utilisateurs devront maintenant se connecter!

---

## 🌐 Déployer en production

Voir le guide complet: **[DEPLOYMENT.md](DEPLOYMENT.md)**

### Option recommandée: Render.com (GRATUIT)

1. Push votre code sur GitHub
2. Créer un compte sur [render.com](https://render.com)
3. Créer un "Web Service"
4. Connecter votre repo GitHub
5. Render détecte automatiquement Python et déploie!

**Live en 5 minutes** 🚀

---

## 🐛 Problèmes courants

### "Python not found"

**Solution**: Installez Python 3.8+ depuis [python.org](https://python.org)

Cochez "Add Python to PATH" pendant l'installation!

### "Module not found: dash"

**Solution**: Activez d'abord l'environnement virtuel:

```bash
venv_dashboard\Scripts\activate  # Windows
source venv_dashboard/bin/activate  # Linux/Mac

# Puis réinstallez
pip install -r requirements.txt
```

### "Port 8050 already in use"

**Solution 1**: Fermez les autres dashboards

**Solution 2**: Changez le port dans `.env`:
```env
PORT=8051
```

### Dashboard lent

**Solution**:
1. Limitez la taille des fichiers uploadés (< 50 MB)
2. Utilisez un fichier CSV au lieu de JSON pour gros datasets
3. Activez le caching (voir README.md)

---

## 📊 Utiliser vos données GoldRL

Pour visualiser vos agents RL:

### Option 1: ZIP complet

1. Aller dans `C:\Users\lbye3\Desktop\GoldRL\AGENT\AGENT 7\`
2. Créer un ZIP contenant:
   ```
   training_stats.json
   ```
3. Uploader ce ZIP dans le dashboard

### Option 2: JSON direct

1. Copier `training_stats.json` depuis le dossier agent
2. Uploader directement dans le dashboard

### Option 3: Comparer tous les agents

1. Aller dans la page "Comparison"
2. Uploader les ZIPs des 4 agents (7, 8, 9, 11)
3. Voir la comparaison côte à côte!

---

## 💰 Vendre votre dashboard

### 1. Système de licences intégré

Le dashboard inclut déjà un système de gestion de licences dans `utils/auth.py`

**Générer une licence pour un client**:

```python
from utils.auth import AuthManager

auth = AuthManager()
license_key = auth.generate_license_key("client@email.com", "PRO")
print(license_key)  # PRO-XXXX-XXXX-XXXX-XXXX
```

### 2. Le client active

Le client entre la clé dans Settings → License Information

### 3. Intégration paiement (optionnel)

Ajoutez Stripe, PayPal, ou Gumroad pour automatiser:

- Génération de licences
- Validation par API
- Renouvellement automatique

Voir `utils/auth.py` pour les hooks d'intégration.

---

## 📚 Ressources

- **README.md**: Documentation complète
- **DEPLOYMENT.md**: Guide de déploiement détaillé
- **Dash Docs**: [dash.plotly.com](https://dash.plotly.com)
- **Dash Bootstrap**: [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/)

---

## 🎉 C'est parti!

Vous avez maintenant un dashboard professionnel prêt pour:

✅ Analyser vos performances de trading
✅ Comparer plusieurs stratégies
✅ Exporter des rapports PDF/Excel
✅ Déployer en production
✅ **Vendre comme produit commercial** 💰

**Bon trading! 📈**

---

**Questions?** Consultez README.md ou DEPLOYMENT.md pour plus de détails.
