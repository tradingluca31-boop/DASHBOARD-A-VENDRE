"""
🔐 AUTHENTICATION - Trading Dashboard Pro
License validation and user management for commercial distribution
"""

import os
import hashlib
import secrets
from typing import Optional, Dict, Tuple
from datetime import datetime, timedelta
import bcrypt


class AuthManager:
    """
    Manage authentication and license validation.

    Features:
    - Password hashing (bcrypt)
    - License key validation
    - Session management
    - Trial period tracking
    """

    def __init__(self):
        self.secret_key = os.getenv("APP_SECRET_KEY", self._generate_secret_key())
        self.license_url = os.getenv("LICENSE_VALIDATION_URL", None)

    @staticmethod
    def _generate_secret_key() -> str:
        """Generate a random secret key."""
        return secrets.token_urlsafe(32)

    @staticmethod
    def hash_password(password: str) -> str:
        """
        Hash password using bcrypt.

        Args:
            password: Plain text password

        Returns:
            Hashed password
        """
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
        return hashed.decode("utf-8")

    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """
        Verify password against hash.

        Args:
            password: Plain text password
            hashed: Hashed password

        Returns:
            True if match, False otherwise
        """
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))

    def validate_license(self, license_key: str) -> Tuple[bool, Dict]:
        """
        Validate license key.

        Args:
            license_key: User's license key

        Returns:
            Tuple of (is_valid, license_info)
        """
        # TODO: Implement actual license validation
        # This could connect to your license server API

        # For now, simple hash-based validation (DEMO)
        if not license_key:
            return False, {"error": "No license key provided"}

        # Demo: Accept any key starting with "PRO-"
        if license_key.startswith("PRO-"):
            return True, {
                "valid": True,
                "type": "professional",
                "expires": (datetime.now() + timedelta(days=365)).isoformat(),
                "features": ["all"],
            }

        return False, {"error": "Invalid license key"}

    def generate_license_key(self, user_email: str, product_type: str = "PRO") -> str:
        """
        Generate a license key for a user.

        Args:
            user_email: User's email
            product_type: Product tier (PRO, ENTERPRISE, etc.)

        Returns:
            License key string
        """
        # Generate hash from email + timestamp + secret
        timestamp = datetime.now().isoformat()
        data = f"{user_email}:{timestamp}:{self.secret_key}"
        hash_obj = hashlib.sha256(data.encode())
        hash_hex = hash_obj.hexdigest()[:16].upper()

        # Format: PRO-XXXX-XXXX-XXXX-XXXX
        formatted = f"{product_type}-{hash_hex[0:4]}-{hash_hex[4:8]}-{hash_hex[8:12]}-{hash_hex[12:16]}"
        return formatted

    def check_trial_status(self, install_date: str) -> Dict:
        """
        Check if trial period is still valid.

        Args:
            install_date: ISO format installation date

        Returns:
            Trial status dictionary
        """
        try:
            installed = datetime.fromisoformat(install_date)
            now = datetime.now()
            days_elapsed = (now - installed).days
            trial_days = 14  # 14-day trial

            return {
                "is_trial": True,
                "days_remaining": max(0, trial_days - days_elapsed),
                "expired": days_elapsed >= trial_days,
                "install_date": install_date,
            }
        except Exception as e:
            return {"error": str(e), "expired": True}


class SessionManager:
    """Manage user sessions (for multi-user deployments)."""

    def __init__(self):
        self.sessions: Dict[str, Dict] = {}

    def create_session(self, user_id: str, user_data: Dict) -> str:
        """
        Create new user session.

        Args:
            user_id: Unique user identifier
            user_data: User information

        Returns:
            Session token
        """
        session_token = secrets.token_urlsafe(32)

        self.sessions[session_token] = {
            "user_id": user_id,
            "created_at": datetime.now(),
            "expires_at": datetime.now() + timedelta(hours=24),
            **user_data,
        }

        return session_token

    def validate_session(self, session_token: str) -> Optional[Dict]:
        """
        Validate and return session data.

        Args:
            session_token: Session token

        Returns:
            Session data or None if invalid
        """
        if session_token not in self.sessions:
            return None

        session = self.sessions[session_token]

        # Check expiration
        if datetime.now() > session["expires_at"]:
            del self.sessions[session_token]
            return None

        return session

    def destroy_session(self, session_token: str) -> bool:
        """
        Destroy a session (logout).

        Args:
            session_token: Session token

        Returns:
            True if successful
        """
        if session_token in self.sessions:
            del self.sessions[session_token]
            return True
        return False


# Example usage for generating license keys
if __name__ == "__main__":
    auth = AuthManager()

    # Generate demo license
    demo_license = auth.generate_license_key("demo@example.com", "PRO")
    print(f"Demo License Key: {demo_license}")

    # Validate
    is_valid, info = auth.validate_license(demo_license)
    print(f"Valid: {is_valid}")
    print(f"Info: {info}")
