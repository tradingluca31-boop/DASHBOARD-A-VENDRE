# 🧪 Guide de Test - Dashboard Live

## ✅ Checklist de Vérification Post-Déploiement

### Étape 1 : Vérifier que le site est live (30 secondes)

1. Allez sur votre dashboard Render : https://dashboard.render.com
2. Cliquez sur votre service "DASHBOARD-A-VENDRE"
3. Vérifiez le statut : **"Live"** (vert)
4. Copiez l'URL de votre dashboard

**URL attendue** : `https://dashboard-a-vendre-XXXX.onrender.com`

---

### Étape 2 : Test de Chargement (10 secondes)

1. Ouvrez l'URL dans votre navigateur
2. Vous devez voir : **"Trading Dashboard Pro"**
3. Design : Thème sombre professionnel (CYBORG)
4. Navigation : Home, Analytics, Comparison, Settings

✅ **Si ça charge** → Tout est bon !
❌ **Si erreur 500** → Vérifiez les logs Render

---

### Étape 3 : Test Upload de Données (2 minutes)

#### Option A : Avec vos vraies données GoldRL

1. Allez dans : `C:\Users\lbye3\Desktop\GoldRL\output`
2. Trouvez un fichier `training_stats.json` récent
3. Créez un ZIP avec ce fichier
4. Uploadez sur le dashboard

#### Option B : Avec données de test

1. Allez dans : `C:\Users\lbye3\Desktop\TradingDashboardPro\data`
2. Utilisez `sample_data.json`
3. Créez un ZIP
4. Uploadez sur le dashboard

**Résultat attendu** :
- ✅ Graphique equity curve s'affiche
- ✅ Métriques calculées (ROI, Sharpe, Drawdown)
- ✅ Cartes colorées selon performance

---

### Étape 4 : Test des Pages (1 minute)

Naviguez dans toutes les pages :

**Page Home** :
- Upload zone fonctionne
- Equity curve s'affiche
- Métriques visibles

**Page Analytics** :
- Graphiques détaillés
- Distribution des trades
- Performance par mois

**Page Comparison** :
- Comparaison multi-agents
- Tableaux de métriques
- Graphiques comparatifs

**Page Settings** :
- Formulaire visible
- Boutons fonctionnels

---

### Étape 5 : Test Performance (30 secondes)

Vérifiez que le site est **rapide** :
- ✅ Chargement initial < 3 secondes
- ✅ Upload fichier < 2 secondes
- ✅ Changement de page < 1 seconde

**Note** : Premier chargement peut être lent (15-30 sec) si le service était en veille (free tier).

---

## 🐛 Résolution de Problèmes

### Problème : Site ne charge pas (erreur 503)

**Cause** : Service en veille (free tier Render)
**Solution** : Attendez 30 secondes, il redémarre automatiquement

### Problème : Erreur 500 au chargement

**Cause** : Bug dans app.py ou dépendances manquantes
**Solution** :
1. Allez dans Render → Logs
2. Cherchez l'erreur Python
3. Si "Module not found" → Vérifiez requirements.txt
4. Si autre erreur → Partagez les logs

### Problème : Upload ne fonctionne pas

**Cause** : Format de fichier incorrect
**Solution** :
- Fichier doit être : JSON ou ZIP contenant JSON
- Structure attendue : `{"episode": [...], "total_reward": [...], ...}`

### Problème : Graphiques ne s'affichent pas

**Cause** : Données manquantes ou format incorrect
**Solution** :
- Vérifiez que votre JSON contient : episode, total_reward, balance
- Vérifiez la structure dans data/sample_data.json

---

## 📊 Données de Test Recommandées

Pour tester avec vos **vrais agents GoldRL** :

```bash
# Agents entraînés
C:\Users\lbye3\Desktop\GoldRL\AGENT\AGENT 7\training_stats.json
C:\Users\lbye3\Desktop\GoldRL\AGENT\AGENT 8\training_stats.json
C:\Users\lbye3\Desktop\GoldRL\AGENT\AGENT 9\training_stats.json
C:\Users\lbye3\Desktop\GoldRL\AGENT\AGENT 11\training_stats.json
C:\Users\lbye3\Desktop\GoldRL\AGENT\META AGENT\training_stats.json
```

**Comment créer un ZIP pour test** :
1. Sélectionnez les 5 fichiers training_stats.json
2. Clic droit → "Compresser vers un fichier ZIP"
3. Nommez : `my_agents_stats.zip`
4. Uploadez sur le dashboard

---

## ✅ Checklist Finale

- [ ] Dashboard accessible en ligne
- [ ] Thème professionnel (sombre) s'affiche
- [ ] Upload fichier JSON fonctionne
- [ ] Equity curve s'affiche correctement
- [ ] Métriques calculées (ROI, Sharpe, DD)
- [ ] Navigation entre pages fonctionne
- [ ] Pas d'erreur console (F12)
- [ ] Performance acceptable (< 3s chargement)

---

## 🎯 Prêt pour la Vente !

Si tous les tests passent, votre dashboard est **prêt à être vendu** ! 🚀

**Prochaines étapes** :
1. Activer l'authentification (ENABLE_AUTH=True)
2. Créer des licences client
3. Définir les prix
4. Commencer le marketing !

**Voir** : [PRICING_STRATEGY.md](PRICING_STRATEGY.md) pour les recommandations de prix.

---

**Besoin d'aide ?** Consultez [DEPLOYMENT.md](DEPLOYMENT.md) ou [README.md](README.md)
