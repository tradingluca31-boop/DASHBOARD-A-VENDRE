# 🚀 Deployment Guide - Trading Dashboard Pro

Complete guide to deploy your dashboard for production use.

---

## 🎯 Deployment Options

### 1️⃣ Render.com (RECOMMENDED - FREE)

**Pros**:
- ✅ Free tier available
- ✅ Automatic deployments from Git
- ✅ Built-in SSL certificates
- ✅ Easy setup (5 minutes)

**Steps**:

1. **Create Render Account**: [render.com](https://render.com)

2. **Push to GitHub**:
```bash
cd C:\Users\lbye3\Desktop\TradingDashboardPro
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/trading-dashboard-pro.git
git push -u origin main
```

3. **Create Web Service on Render**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Settings:
     ```
     Name: trading-dashboard-pro
     Region: Oregon (US West)
     Branch: main
     Runtime: Python 3
     Build Command: pip install -r requirements.txt
     Start Command: gunicorn app:server --bind 0.0.0.0:$PORT
     ```

4. **Environment Variables**:
   Add in Render dashboard:
   ```
   APP_SECRET_KEY=your-secret-key-here
   DEBUG_MODE=False
   ENABLE_AUTH=True
   ```

5. **Deploy**: Click "Create Web Service"

**Live URL**: `https://trading-dashboard-pro.onrender.com`

---

### 2️⃣ Heroku

**Pros**:
- ✅ Very popular, well-documented
- ✅ Good free tier (with credit card)
- ✅ Easy scaling

**Steps**:

1. **Install Heroku CLI**: [heroku.com/cli](https://devcenter.heroku.com/articles/heroku-cli)

2. **Create Heroku App**:
```bash
heroku login
cd C:\Users\lbye3\Desktop\TradingDashboardPro
heroku create your-dashboard-name
```

3. **Add Procfile**:
Create `Procfile` (no extension):
```
web: gunicorn app:server
```

4. **Set Environment Variables**:
```bash
heroku config:set APP_SECRET_KEY=your-secret-key
heroku config:set DEBUG_MODE=False
```

5. **Deploy**:
```bash
git add .
git commit -m "Deploy to Heroku"
git push heroku main
```

6. **Open App**:
```bash
heroku open
```

---

### 3️⃣ AWS EC2 (Advanced)

**Pros**:
- ✅ Full control
- ✅ Scalable
- ✅ Professional

**Steps**:

1. **Launch EC2 Instance** (Ubuntu 22.04)

2. **SSH into instance**:
```bash
ssh -i your-key.pem ubuntu@your-ec2-ip
```

3. **Install Dependencies**:
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx -y
```

4. **Clone Your Code**:
```bash
git clone https://github.com/YOUR_USERNAME/trading-dashboard-pro.git
cd trading-dashboard-pro
```

5. **Setup Virtual Environment**:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

6. **Configure Gunicorn**:
```bash
gunicorn --workers 3 --bind 0.0.0.0:8000 app:server &
```

7. **Setup Nginx** (reverse proxy):

Create `/etc/nginx/sites-available/dashboard`:
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/dashboard /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

8. **Setup SSL (Let's Encrypt)**:
```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

---

### 4️⃣ DigitalOcean App Platform

**Pros**:
- ✅ Similar to Heroku
- ✅ $5/month starter tier
- ✅ Easy setup

**Steps**:

1. **Create DigitalOcean Account**: [digitalocean.com](https://digitalocean.com)

2. **Create App**:
   - Go to Apps → Create App
   - Connect GitHub repo
   - Choose branch: `main`
   - Detect Python automatically

3. **Configure**:
   ```
   Build Command: pip install -r requirements.txt
   Run Command: gunicorn app:server
   HTTP Port: 8080 (auto-detected)
   ```

4. **Environment Variables**:
   Add in App settings

5. **Deploy**: Click "Create Resources"

---

## 🔒 Security Best Practices

### 1. Environment Variables

**NEVER commit .env to Git**:

```bash
# Already in .gitignore
.env
```

### 2. Secret Key

Generate strong secret:

```python
import secrets
print(secrets.token_urlsafe(32))
# Use this as APP_SECRET_KEY
```

### 3. HTTPS Only

Force HTTPS in production:

```python
# In app.py
if not app.debug:
    from werkzeug.middleware.proxy_fix import ProxyFix
    app.server.wsgi_app = ProxyFix(app.server.wsgi_app)
```

### 4. Rate Limiting

Prevent abuse:

```python
from flask_limiter import Limiter

limiter = Limiter(
    app.server,
    key_func=lambda: request.remote_addr,
    default_limits=["200 per day", "50 per hour"]
)
```

---

## 📊 Monitoring & Analytics

### 1. Application Monitoring

**Sentry** (error tracking):

```bash
pip install sentry-sdk[flask]
```

```python
# In app.py
import sentry_sdk
sentry_sdk.init(dsn="your-sentry-dsn")
```

### 2. Performance Monitoring

**New Relic** (free tier available):

```bash
pip install newrelic
newrelic-admin generate-config YOUR_LICENSE_KEY newrelic.ini
```

Run with:
```bash
newrelic-admin run-program gunicorn app:server
```

### 3. Logging

Configure production logging:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

---

## 💾 Database Setup (Optional)

### PostgreSQL (for multi-user)

**Render.com**:
- Create PostgreSQL database (free)
- Copy `DATABASE_URL`
- Add to environment variables

**Local PostgreSQL**:

```bash
# Install PostgreSQL
# Create database
createdb dashboard_db

# Update .env
DATABASE_URL=postgresql://user:password@localhost/dashboard_db
```

**SQLAlchemy setup**:

```python
from sqlalchemy import create_engine
import os

engine = create_engine(os.getenv('DATABASE_URL'))
```

---

## 🔄 CI/CD Pipeline

### GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest

      - name: Deploy to Render
        run: |
          # Trigger Render deployment
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

---

## 📈 Scaling

### Horizontal Scaling

**Gunicorn workers**:

```bash
# Formula: (2 x CPU cores) + 1
gunicorn --workers 5 app:server
```

### Caching

**Redis caching**:

```bash
pip install redis flask-caching
```

```python
from flask_caching import Cache

cache = Cache(app.server, config={
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': os.getenv('REDIS_URL')
})

@cache.memoize(timeout=300)
def expensive_calculation():
    # ...
```

---

## 🧪 Pre-Deployment Checklist

- [ ] All environment variables set
- [ ] DEBUG_MODE=False
- [ ] Strong SECRET_KEY generated
- [ ] Database migrations run (if applicable)
- [ ] SSL certificate configured
- [ ] Error monitoring setup (Sentry)
- [ ] Backups configured
- [ ] Rate limiting enabled
- [ ] CORS configured (if needed)
- [ ] Static files optimized
- [ ] Tests passing
- [ ] Documentation updated

---

## 🆘 Troubleshooting

### "Application Error" on Render/Heroku

**Check logs**:

```bash
# Render
# View in dashboard under "Logs"

# Heroku
heroku logs --tail
```

### Database Connection Issues

```python
# Test connection
from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)
conn = engine.connect()
print("Connected!")
```

### Slow Performance

1. **Enable caching** (Redis)
2. **Optimize queries**
3. **Add CDN** for static assets
4. **Scale workers**

---

## 📞 Support

If you need help deploying:

- Check logs first
- Google the exact error message
- Stack Overflow
- Render/Heroku docs
- Contact your hosting support

---

**Happy Deploying! 🚀**
