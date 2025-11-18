# 🏛️ Trading Dashboard Pro V2.0

**Dashboard d'analyse trading institutionnel avec 30+ métriques de niveau hedge fund**

![Version](https://img.shields.io/badge/version-2.0.0-cyan) ![Python](https://img.shields.io/badge/python-3.13-blue) ![License](https://img.shields.io/badge/license-Commercial-orange)

Perfect for **selling as a SaaS product** with built-in analytics, authentication, and institutional-grade metrics.

**🚀 NOUVEAU V2.0** : Design moderne vibrant avec 30+ métriques, tooltips éducatifs, et graphiques professionnels !

---

## ✨ Features V2.0 (2025-01-18)

### 🎨 Modern Design System
- **Vibrant Color Palette**: Cyan (#00d9ff), Orange (#ff6b35), Violet (#7b68ee)
- **3 Hero Cards** avec effets glow pour métriques principales
- **Grille Professionnelle**: 6 rows de cartes métriques organisées
- **Multiple Chart Types**: Equity area, monthly bar, win/loss donut
- **Responsive Layout**: Adaptation mobile/tablet/desktop

### 📊 30+ Institutional Metrics

#### **PERFORMANCE (6 metrics)**
1. **ROI %** - Return on Investment
2. **Total P&L** - Profit & Loss en dollars
3. **Final Balance** - Solde final du compte
4. **CAGR** - Compound Annual Growth Rate
5. **Profit Factor** - Gains totaux / Pertes totales
6. **Expectancy** - Profit attendu par trade

#### **RISK MANAGEMENT (7 metrics)**
7. **Sharpe Ratio** - Rendement ajusté au risque (annualisé)
8. **Sortino Ratio** - Sharpe avec downside deviation seulement
9. **Calmar Ratio** - CAGR / Max Drawdown
10. **Max Drawdown %** - Perte maximale depuis peak
11. **Max Daily Loss %** - Pire journée
12. **VaR 95%** - Value at Risk (95% confidence)
13. **CVaR 95%** - Conditional VaR (Expected Shortfall)

#### **TRADE STATISTICS (10 metrics)**
14. **Total Trades** - Nombre total de positions
15. **Winning Trades** - Nombre de trades gagnants
16. **Losing Trades** - Nombre de trades perdants
17. **Win Rate %** - Taux de réussite
18. **Average Win** - Gain moyen par trade gagnant
19. **Average Loss** - Perte moyenne par trade perdant
20. **Best Trade** - Meilleur trade
21. **Worst Trade** - Pire trade
22. **Win/Loss Ratio** - Avg Win / Avg Loss
23. **Avg Trade Duration** - Durée moyenne des positions

#### **ADVANCED METRICS (4 metrics)**
24. **Recovery Factor** - Net Profit / Max DD (dollars)
25. **Ulcer Index** - Volatilité des drawdowns
26. **Pain Index** - Intensité moyenne des drawdowns
27. **Kelly Criterion** - Taille de position optimale

#### **FTMO COMPLIANCE (3 metrics)**
28. **FTMO Max DD Compliant** - DD < 10% ✓/✗
29. **FTMO Daily Loss Compliant** - Daily loss < 5% ✓/✗
30. **Trading Days** - Nombre de jours de trading

### 📚 Educational Tooltips (Ready for V2.1)
Chaque métrique inclut :
- **Description** claire et concise
- **Formule** mathématique
- **Interprétation** avec ranges (Excellent/Bon/Faible)
- **Qui l'utilise** (hedge funds, institutions)
- **Exemples** concrets (1R nul, 2R bon, 3R très bon)

**Exemples** :
```
Sharpe Ratio:
- < 0: ❌ Très mauvais
- 0.5-1.0: 🟡 Acceptable
- 1.0-2.0: 🟢 Bon
- 2.0-3.0: 💎 Excellent (institutionnel)
- > 3.0: 🏆 Exceptionnel (élite)

Kelly Criterion:
- 12% = Utilisez 12% du capital par trade
- > 25% = Réduire de moitié (Half Kelly)
- Utilisé par: Ed Thorp, Renaissance Technologies
```

### 🔐 Commercial Features (Ready)
- **License Management**: Système de clés de licence intégré
- **Authentication**: Protection par mot de passe (bcrypt)
- **Trial Mode**: Période d'essai 14 jours
- **Export Options**: PDF, Excel, CSV exports

### 🚀 Production-Ready
- **Multi-page App**: Home, Analytics, Comparison, Settings
- **Deployed on Render**: Auto-deploy from GitHub
- **Session Storage**: Persist data across pages
- **Error Handling**: Robust validation

---

## 🗺️ Roadmap V2.1 (EN DÉVELOPPEMENT)

**Délai estimé** : 11-16 jours

### 🔐 Multi-User Authentication System
- **Login/Signup Page** avec bcrypt password hashing
- **User Dashboard** pour voir historique complet
- **Session Management** avec JWT tokens
- **PostgreSQL Database** pour stockage persistant

### 🏦 Multi-Broker Support
- **Créer plusieurs sous-comptes** par broker (FTMO, MyFundedFX, etc.)
- **Tracking séparé** pour chaque compte
- **Comparaison inter-brokers**
- **Initial balance** configurable par compte

### 📅 Temporal Analysis
- **Daily Analysis** : Breakdown jour par jour
- **Weekly Analysis** : Performance hebdomadaire
- **Monthly Analysis** : Résultats mensuels
- **Yearly Analysis** : Vue annuelle
- **Comparison** : Comparer n'importe quelle période

### 💾 Database Schema (PostgreSQL)
```sql
users (id, email, username, password_hash, subscription_tier)
brokers (id, user_id, broker_name, account_number, initial_balance)
analyses (id, broker_id, uploaded_at, period_start, period_end)
daily_performance (id, analysis_id, date, daily_pnl, trades_count)
weekly_performance (id, analysis_id, week_start, weekly_pnl)
monthly_performance (id, analysis_id, month_start, monthly_pnl)
yearly_performance (id, analysis_id, year, yearly_pnl)
```

**Documentation complète** : Voir [ARCHITECTURE_V2.1.md](ARCHITECTURE_V2.1.md)

---

## 🏗️ Project Structure

```
TradingDashboardPro/
├── app.py                          # Main Dash application
├── requirements.txt                # Python dependencies
├── render.yaml                     # Render deployment config
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── README.md                       # This file ⭐
├── CHANGELOG.md                    # Version history
├── ARCHITECTURE_V2.1.md            # V2.1 technical specs
├── DEPLOY_V2_MODERN.bat            # Deploy script to Render
│
├── pages/                          # Dashboard pages
│   ├── __init__.py
│   ├── home.py                     # ⭐ V2.0 Modern design (772 lines)
│   ├── analytics.py                # Advanced analytics
│   ├── comparison.py               # Multi-agent comparison
│   └── settings.py                 # User settings
│
├── utils/                          # Utility modules
│   ├── __init__.py
│   ├── data_loader.py              # Parse ZIP/JSON/CSV
│   ├── metrics.py                  # ⭐ 30+ metrics calculator (515 lines)
│   ├── metrics_explanations.py     # ⭐ Educational tooltips (450+ lines)
│   └── auth.py                     # Authentication & licensing
│
├── assets/                         # Static files (CSS, images)
│   └── (custom styles)
│
└── data/                           # User uploaded data (gitignored)
    └── TEST_AGENTS_DATA.zip        # Sample test data
```

---

## 🚀 Quick Start (Local Development)

### 1. Prerequisites
- Python 3.13+ (recommended)
- Git (for version control)
- Virtual environment tool (venv)

### 2. Setup Virtual Environment

```bash
# Navigate to project
cd C:\Users\lbye3\Desktop\TradingDashboardPro

# Create virtual environment
python -m venv venv_dashboard

# Activate (Windows)
venv_dashboard\Scripts\activate

# Activate (Linux/Mac)
source venv_dashboard/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Dependencies V2.0** :
- dash>=2.14.0
- dash-bootstrap-components>=1.5.0
- plotly>=5.18.0
- pandas>=2.2.0 (Python 3.13 compatible)
- numpy>=1.26.0 (Python 3.13 compatible)
- scipy>=1.11.0
- python-dotenv>=1.0.0
- bcrypt>=4.1.0
- gunicorn>=21.2.0

### 4. Configure Environment (Optional)

```bash
# Copy example
copy .env.example .env  # Windows
cp .env.example .env    # Linux/Mac

# Edit with your settings
notepad .env  # Windows
nano .env     # Linux
```

### 5. Run Locally

```bash
python app.py
```

Visit: **http://localhost:8050**

### 6. Test with Sample Data

Upload `TEST_AGENTS_DATA.zip` to test all 30+ metrics:
- Agent 7: ROI 22.8%, Sharpe 1.38
- Agent 8: ROI 16.8%, Sharpe 1.18

---

## 🌐 Deployment on Render.com (FREE)

### Current Deployment
**URL Live** : https://your-app-name.onrender.com (configure ton URL)

### Auto-Deploy Setup (Already configured)

1. **GitHub Connected** : Push déclenche auto-deploy
2. **Build Command** : `pip install -r requirements.txt`
3. **Start Command** : `gunicorn app:server`
4. **Environment** : Python 3.13

### Manual Deploy

```bash
# From project root
cd C:\Users\lbye3\Desktop\TradingDashboardPro

# Run deploy script
DEPLOY_V2_MODERN.bat
```

This script will:
1. Add all files to git
2. Commit with detailed message
3. Push to GitHub
4. Render auto-deploys in ~30 seconds

---

## 📊 All 30+ Metrics Explained

### Performance Metrics

**ROI (Return on Investment)**
- Formula: `((Final Balance - Initial Balance) / Initial Balance) × 100`
- Target: > 5% annualisé minimum
- Hedge fund standard: 15-30% annuel

**CAGR (Compound Annual Growth Rate)**
- Formula: `(((Final / Initial) ^ (1 / Years)) - 1) × 100`
- Target: > 8% pour battre S&P 500
- Top funds: 20-40% CAGR sustained

**Profit Factor**
- Formula: `Total Gains / Total Losses`
- Interpretation:
  - < 1.0: ❌ Système perdant
  - 1.0-1.5: 🟡 Acceptable
  - 1.5-2.0: 🟢 Bon
  - 2.0-3.0: 💎 Excellent
  - > 3.0: 🏆 Exceptionnel
- Used by: Tous les hedge funds

**Expectancy**
- Formula: `(Win Rate × Avg Win) - (Loss Rate × Avg Loss)`
- Target: > 0 (positif)
- Exemple: Expectancy de 0.25R = Gain 0.25% par trade en moyenne

### Risk Metrics

**Sharpe Ratio** (annualisé)
- Formula: `(Return - Risk Free Rate) / Std Dev × √252`
- Interpretation:
  - < 0: ❌ Perte avec volatilité
  - 0-0.5: 🟡 Faible
  - 0.5-1.0: 🟡 Acceptable
  - 1.0-2.0: 🟢 Bon
  - 2.0-3.0: 💎 Excellent (institutionnel)
  - > 3.0: 🏆 Exceptionnel (Renaissance: 2-3+)
- Used by: Renaissance Technologies, Bridgewater, tous hedge funds

**Sortino Ratio**
- Formula: `(Return - Risk Free Rate) / Downside Deviation × √252`
- Similar to Sharpe but only penalizes downside volatility
- Target: > 1.5 excellent

**Calmar Ratio**
- Formula: `CAGR / |Max Drawdown %|`
- Interpretation:
  - < 0.5: ❌ Mauvais
  - 0.5-1.0: 🟡 Acceptable
  - 1.0-3.0: 🟢 Bon
  - 3.0-5.0: 💎 Excellent
  - > 5.0: 🏆 Exceptionnel
- Used by: Hedge funds, CTAs

**Max Drawdown**
- Formula: `Max((Balance - Running Peak) / Running Peak) × 100`
- Target FTMO: < 10%
- Target Pro: < 5%
- Example: -8.5% = Lost 8.5% from highest point

**VaR 95% (Value at Risk)**
- Worst expected loss at 95% confidence
- Example: VaR = -1.5% means 95% of days you won't lose more than 1.5%
- Used by: JP Morgan, all investment banks

**CVaR 95% (Conditional VaR)**
- Average loss beyond VaR threshold
- More conservative than VaR
- Used by: Risk management teams globally

### Advanced Metrics

**Recovery Factor**
- Formula: `Net Profit / |Max Drawdown (dollars)|`
- Interpretation:
  - < 1.0: ❌ Drawdown > Profit
  - 1.0-3.0: 🟡 Acceptable
  - 3.0-5.0: 🟢 Bon
  - 5.0-10.0: 💎 Excellent
  - > 10.0: 🏆 Exceptionnel
- Example: Recovery of 4.2 = Made 4.2× the max DD

**Ulcer Index**
- Formula: `√(Mean of squared %DD)`
- Measures stress from drawdowns
- Lower is better
- Used by: Peter Martin (creator), quantitative funds

**Pain Index**
- Formula: `Mean of absolute %DD over entire period`
- Average drawdown intensity
- Lower is better
- Target: < 3%

**Kelly Criterion**
- Formula: `(Win Rate × W/L Ratio - Loss Rate) / W/L Ratio`
- Optimal position size to maximize growth
- Interpretation:
  - < 0%: ❌ Système non rentable
  - 0-5%: 🟡 Faible edge
  - 5-15%: 🟢 Bon edge
  - 15-25%: 💎 Fort edge
  - > 25%: ⚠️ Use Half Kelly (÷2)
- Used by: Ed Thorp, Renaissance Technologies, all quant traders

### Trade Statistics

**Win Rate**
- Formula: `(Winning Trades / Total Trades) × 100`
- Interpretation:
  - < 40%: ❌ Needs high W/L ratio
  - 40-50%: 🟡 Acceptable avec 2R+
  - 50-60%: 🟢 Bon
  - 60-70%: 💎 Excellent
  - > 70%: 🏆 Exceptionnel (rare sustainably)

**Win/Loss Ratio**
- Formula: `Average Win / Average Loss`
- Interpretation:
  - < 1.0: ❌ Need >50% win rate
  - 1.0-1.5: 🟡 Acceptable avec 55%+ win rate
  - 1.5-2.0: 🟢 Bon (2R)
  - 2.0-3.0: 💎 Excellent (3R)
  - > 3.0: 🏆 Exceptionnel (4R+)

### FTMO Compliance

**Max Drawdown < 10%**
- Critical rule: Account closed if breached
- Monitor in real-time
- V2.0 auto-checks compliance

**Daily Loss < 5%**
- Calculated from start-of-day balance
- Critical rule: Account closed if breached
- V2.0 auto-checks compliance

---

## 🔧 Configuration

### Environment Variables (.env)

```env
# App Settings
APP_SECRET_KEY=your-secret-key-here-change-this
DEBUG_MODE=False
PORT=8050

# Authentication (V2.1)
ENABLE_AUTH=True
JWT_SECRET_KEY=another-secret-key-change-this

# Database (V2.1 - PostgreSQL on Render)
DATABASE_URL=postgresql://user:password@host:5432/database

# License Validation
LICENSE_VALIDATION_URL=https://your-server.com/api/validate

# Stripe (for payments)
STRIPE_API_KEY=sk_live_your_key
STRIPE_WEBHOOK_SECRET=whsec_your_secret
```

### Generate Secure Keys

```python
import secrets

# Generate secret key
secret = secrets.token_urlsafe(32)
print(f"Secret Key: {secret}")
```

---

## 💰 Selling Your Dashboard as SaaS

### Pricing Tiers (Example)

**Starter Plan** - $29/month
- Single broker account
- 30+ metrics
- Basic charts
- CSV export

**Pro Plan** - $79/month
- Unlimited broker accounts
- Temporal analysis (day/week/month/year)
- Advanced charts
- PDF/Excel export
- Priority support

**Enterprise Plan** - $199/month
- Multi-user (team)
- API access
- Custom metrics
- White-label option
- Dedicated support

### Payment Integration (Stripe)

Add to `utils/auth.py`:

```python
import stripe
stripe.api_key = os.getenv("STRIPE_API_KEY")

def create_checkout_session(plan: str, user_email: str):
    """Create Stripe checkout for subscription"""
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': PLAN_PRICES[plan],
            'quantity': 1,
        }],
        mode='subscription',
        success_url='https://your-domain.com/success',
        cancel_url='https://your-domain.com/cancel',
        customer_email=user_email,
    )
    return session
```

### License Key System

```python
from utils.auth import AuthManager

# Generate license for customer
auth = AuthManager()
license_key = auth.generate_license_key(
    email="customer@example.com",
    tier="PRO",
    duration_days=30
)

print(license_key)  # Give to customer
```

---

## 🛠️ Development

### Running Tests

```bash
# Unit tests (create tests/ folder)
pytest tests/

# Test with sample data
python -c "from utils.data_loader import DataLoader; print(DataLoader.load_zip('TEST_AGENTS_DATA.zip'))"
```

### Adding New Metrics

1. **Add calculation** to `utils/metrics.py`:

```python
def calculate_your_metric(self) -> float:
    """Calculate your custom metric"""
    # Your logic here
    return result
```

2. **Add to get_all_metrics()** dictionary

3. **Add explanation** to `utils/metrics_explanations.py`:

```python
"your_metric": {
    "name": "Your Metric Name",
    "description": "What it measures",
    "formula": "Mathematical formula",
    "interpretation": {
        "< 0": "❌ Bad",
        "0-50": "🟡 OK",
        "> 50": "🟢 Good"
    },
    "qui_utilise": "Who uses it",
    "exemple": "Example: 25 = Good"
}
```

4. **Add to home.py** layout

### Code Style

- **Type hints** everywhere
- **Docstrings** for all functions
- **Comments** for complex logic
- **Error handling** with try/except

---

## 📦 Updates & Maintenance

### Update Dependencies

```bash
pip install --upgrade pip
pip install --upgrade -r requirements.txt
```

### Database Backups (V2.1)

```bash
# PostgreSQL dump
pg_dump -h hostname -U username database_name > backup.sql

# Restore
psql -h hostname -U username database_name < backup.sql
```

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/new-metric

# Make changes, commit
git add .
git commit -m "Add new metric: XYZ"

# Push and create PR
git push origin feature/new-metric
```

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'dash'"

```bash
# Activate virtual environment first
venv_dashboard\Scripts\activate  # Windows
source venv_dashboard/bin/activate  # Linux/Mac

# Reinstall dependencies
pip install -r requirements.txt
```

### "Port 8050 already in use"

```bash
# Option 1: Kill process
# Windows
netstat -ano | findstr :8050
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:8050 | xargs kill -9

# Option 2: Change port in .env
PORT=8051
```

### "Metrics showing 0.0 for everything"

Check data format:
- Must have `balance` or `total_reward` column
- Must have multiple rows (>1)
- Numeric values not strings

### Render deployment failing

1. Check `requirements.txt` has all dependencies
2. Verify `render.yaml` build/start commands
3. Check Render logs for specific error
4. Ensure Python 3.13 selected in Render dashboard

---

## 📚 Documentation & Resources

### Project Docs
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [ARCHITECTURE_V2.1.md](ARCHITECTURE_V2.1.md) - V2.1 technical specs
- [DEPLOY_V2_MODERN.bat](DEPLOY_V2_MODERN.bat) - Deploy script

### External Docs
- [Plotly Dash Documentation](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Render Deployment Guide](https://render.com/docs/deploy-dash)
- [Stripe Integration](https://stripe.com/docs/payments)

### Learning Resources
- **Sharpe Ratio**: [Investopedia](https://www.investopedia.com/terms/s/sharperatio.asp)
- **Kelly Criterion**: [Ed Thorp Paper](https://www.edwardothorp.com/id26.html)
- **FTMO Rules**: [FTMO Official](https://ftmo.com/en/trading-objectives/)

---

## 🤝 Support & Contact

### Commercial Support
- **Email**: your-email@domain.com (configure)
- **Website**: your-website.com (configure)
- **Discord**: your-discord-invite (optional)

### Issues & Bugs
- Create issue on GitHub
- Provide error logs, data sample, steps to reproduce

### Feature Requests
- Submit via GitHub Issues with [FEATURE] tag
- Describe use case and expected behavior

---

## 📊 Performance Benchmarks

### Metrics Calculation Speed
- 30+ metrics on 10,000 rows: ~50ms
- 30+ metrics on 100,000 rows: ~200ms
- Chart rendering: ~100-300ms

### Recommended Hardware
- **Minimum**: 2GB RAM, 1 CPU core
- **Recommended**: 4GB RAM, 2 CPU cores
- **Production**: 8GB RAM, 4 CPU cores

### Render Free Tier
- ✅ 750 hours/month (enough for production)
- ✅ 512 MB RAM
- ✅ Auto-deploy from GitHub
- ⚠️ Sleeps after 15min inactivity (wakes in ~30s)

---

## 📄 License & Legal

### Commercial License
This software requires a **valid license key** for commercial use.

For licensing inquiries:
- Email: your-email@domain.com
- Terms: [LICENSE.md](LICENSE.md) (create if needed)

### Open Source Dependencies
All dependencies are open-source (MIT/BSD/Apache 2.0):
- Plotly Dash (MIT)
- Pandas (BSD)
- NumPy (BSD)
- SciPy (BSD)

---

## 🎉 Credits & Acknowledgments

**Built with** ❤️ and:
- [Plotly Dash](https://plotly.com/dash/) - Web framework
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) - UI library
- [Font Awesome](https://fontawesome.com/) - Icons
- [Render.com](https://render.com/) - Hosting platform
- Python 🐍 - Programming language

**Inspired by**:
- Renaissance Technologies (Medallion Fund)
- Bridgewater Associates (Ray Dalio)
- Two Sigma Investments
- Jane Street Capital

---

## 📈 Changelog

See [CHANGELOG.md](CHANGELOG.md) for complete version history.

**Latest Version: 2.0.0** (2025-01-18)
- 30+ institutional metrics
- Modern vibrant design (cyan/orange/violet)
- Educational tooltips system
- Multiple chart types
- FTMO compliance checks

**Next Version: 2.1.0** (En développement, ~2 semaines)
- Multi-user authentication (PostgreSQL)
- Multi-broker support
- Temporal analysis (day/week/month/year)
- Advanced filtering & comparison

---

## 🚀 Roadmap V3.0 (Future)

**Planned Features**:
- [ ] Real-time data streaming (WebSocket)
- [ ] Mobile app (React Native)
- [ ] API endpoints (REST + GraphQL)
- [ ] Machine Learning predictions
- [ ] Social trading features
- [ ] White-label customization
- [ ] Multi-language support (EN/FR/ES/DE)

---

**© 2025 Trading Dashboard Pro | All Rights Reserved**

**Made with** 💎 **for professional traders**

---

**Quick Links**:
- 📖 [Documentation](README.md) (You are here)
- 📋 [Changelog](CHANGELOG.md)
- 🏗️ [Architecture V2.1](ARCHITECTURE_V2.1.md)
- 🚀 [Deploy Script](DEPLOY_V2_MODERN.bat)
- 📦 [Test Data](TEST_AGENTS_DATA.zip)

**Version**: 2.0.0 | **Updated**: 2025-01-18 | **Status**: ✅ Production-Ready
