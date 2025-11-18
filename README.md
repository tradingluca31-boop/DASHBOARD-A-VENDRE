# 🏛️ Trading Dashboard Pro

**Professional-grade trading analytics dashboard built with Plotly Dash**

Perfect for selling as a commercial product with built-in license management and authentication.

---

## ✨ Features

### 📊 Core Analytics
- **Real-time Performance Monitoring**: Track equity, ROI, drawdown, and more
- **Institutional Metrics**: Sharpe, Sortino, Calmar ratios, VaR, CVaR
- **FTMO Compliance Checking**: Automatic validation against FTMO rules
- **Multi-Agent Comparison**: Compare multiple trading strategies side-by-side

### 🎨 Professional Design
- **Dark Theme**: Modern, professional Cyborg theme (Bootstrap)
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Interactive Charts**: Plotly graphs with zoom, pan, and export
- **Clean UI**: Font Awesome icons, smooth animations

### 🔐 Commercial Features
- **License Management**: Built-in license key validation system
- **Authentication**: Optional password protection
- **Trial Mode**: 14-day trial period tracking
- **Export Options**: PDF reports, Excel, CSV exports

### 🚀 Production-Ready
- **Multi-page App**: Home, Analytics, Comparison, Settings
- **Session Storage**: Persist data across page navigation
- **Auto-refresh**: Optional real-time updates
- **Error Handling**: Robust error handling and validation

---

## 🏗️ Project Structure

```
TradingDashboardPro/
├── app.py                  # Main application
├── requirements.txt        # Dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── README.md              # This file
│
├── pages/                 # Dashboard pages
│   ├── __init__.py
│   ├── home.py           # Main overview page
│   ├── analytics.py      # Advanced analytics
│   ├── comparison.py     # Multi-agent comparison
│   └── settings.py       # User settings
│
├── utils/                # Utility modules
│   ├── __init__.py
│   ├── data_loader.py    # Data parsing (ZIP, JSON, CSV)
│   ├── metrics.py        # Trading metrics calculator
│   └── auth.py           # Authentication & licensing
│
├── assets/               # Static files (CSS, images)
│   └── (custom styles)
│
└── data/                 # User data (gitignored)
    └── (uploaded files)
```

---

## 🚀 Quick Start

### 1. Clone or Extract

```bash
cd C:\Users\lbye3\Desktop\TradingDashboardPro
```

### 2. Create Virtual Environment

```bash
python -m venv venv_dashboard
venv_dashboard\Scripts\activate  # Windows
# OR
source venv_dashboard/bin/activate  # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment

```bash
# Copy example env file
copy .env.example .env  # Windows
# OR
cp .env.example .env    # Linux/Mac

# Edit .env with your settings
notepad .env  # Windows
```

### 5. Run Dashboard

```bash
python app.py
```

Visit: **http://localhost:8050**

---

## 🔧 Configuration

### Environment Variables (.env)

```env
# App Settings
APP_SECRET_KEY=your-secret-key-here
DEBUG_MODE=False
PORT=8050

# Authentication (optional)
ENABLE_AUTH=True
ADMIN_USERNAME=admin
ADMIN_PASSWORD_HASH=your-bcrypt-hash

# License Validation (for selling)
LICENSE_VALIDATION_URL=https://your-server.com/api/validate
STRIPE_API_KEY=sk_test_your_stripe_key

# Database (optional - for multi-user)
DATABASE_URL=postgresql://user:pass@localhost/db
```

### Generate Password Hash

```python
from utils.auth import AuthManager

auth = AuthManager()
hashed = auth.hash_password("your-password")
print(hashed)  # Put this in .env
```

---

## 📊 Usage

### Upload Data

1. **ZIP Files**: Must contain `training_stats.json`
2. **JSON Files**: Direct checkpoint data
3. **CSV/Excel**: Tabular trading data

### Supported Data Format

```json
[
  {
    "timestep": 50000,
    "balance": 10250.50,
    "roi": 2.50,
    "total_pnl": 250.50,
    "total_trades": 15,
    "win_rate": 60.0,
    "profit_factor": 1.8,
    "sharpe_ratio": 1.2,
    "max_drawdown_pct": -3.5
  },
  ...
]
```

---

## 🌐 Deployment

### Option 1: Render.com (FREE)

1. Create account at [render.com](https://render.com)
2. Connect GitHub repo
3. Create new **Web Service**
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:server`

### Option 2: Heroku

```bash
# Install Heroku CLI
heroku login
heroku create your-dashboard-name

# Deploy
git push heroku main
```

### Option 3: AWS/DigitalOcean

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed instructions.

---

## 💰 Selling Your Dashboard

### License Key System

1. **Generate License**:
```python
from utils.auth import AuthManager

auth = AuthManager()
license_key = auth.generate_license_key("customer@email.com", "PRO")
print(license_key)  # Give this to customer
```

2. **Customer Activates**:
   - Enter license key in Settings page
   - Validated against your server (optional)
   - Access granted for specified period

### Pricing Tiers

Example tiers you could offer:

- **Starter** ($29/month): Single agent monitoring
- **Pro** ($79/month): Multi-agent comparison, exports
- **Enterprise** ($199/month): Unlimited agents, API access

### Payment Integration

Add Stripe/PayPal in `utils/auth.py`:

```python
import stripe
stripe.api_key = os.getenv("STRIPE_API_KEY")

# Create checkout session
# (See Stripe docs)
```

---

## 🛠️ Customization

### Change Theme

In `app.py`:

```python
external_stylesheets = [
    dbc.themes.CYBORG,  # Change to: DARKLY, SLATE, SUPERHERO, etc.
    dbc.icons.FONT_AWESOME,
]
```

### Add Custom CSS

Create `assets/custom.css`:

```css
/* Your custom styles */
.navbar-brand {
    font-weight: bold;
    font-size: 1.5rem;
}
```

### Add New Page

1. Create `pages/your_page.py`
2. Define `layout()` function
3. Import in `app.py`
4. Add route in `display_page()` callback

---

## 📦 Updates & Maintenance

### Update Dependencies

```bash
pip install --upgrade -r requirements.txt
```

### Database Backups (if using)

```bash
# PostgreSQL
pg_dump dashboard_db > backup.sql

# Restore
psql dashboard_db < backup.sql
```

---

## 🐛 Troubleshooting

### "Module not found" Error

```bash
# Make sure virtual environment is activated
venv_dashboard\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use

Change port in `.env`:

```env
PORT=8051  # Or any other port
```

### Slow Performance

- Enable caching in `app.py`
- Use production server (gunicorn)
- Optimize database queries

---

## 📚 Documentation

- [Plotly Dash Docs](https://dash.plotly.com/)
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/)
- [Deployment Guide](DEPLOYMENT.md)

---

## 🤝 Support

For commercial support or custom development:

- Email: your-email@domain.com
- Website: your-website.com
- Discord: your-discord-server

---

## 📄 License

**Commercial License** - This software requires a valid license key for use.

For licensing inquiries, contact: your-email@domain.com

---

## 🎉 Credits

Built with:
- [Plotly Dash](https://plotly.com/dash/) - Framework
- [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) - UI
- [Font Awesome](https://fontawesome.com/) - Icons
- Love ❤️ and Python 🐍

---

**© 2025 Trading Dashboard Pro | All Rights Reserved**
