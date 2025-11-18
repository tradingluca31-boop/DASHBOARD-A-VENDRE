"""
📥 DATA LOADER - Trading Dashboard Pro
Handles loading and parsing of trading data from various sources
"""

import base64
import io
import json
import zipfile
from pathlib import Path
from typing import Optional, List, Dict, Union

import pandas as pd


class DataLoader:
    """
    Universal data loader for trading dashboard.

    Supports:
    - ZIP files (with training_stats.json)
    - Direct JSON files
    - CSV files
    - Excel files
    """

    def __init__(self):
        self.supported_formats = [".zip", ".json", ".csv", ".xlsx"]

    def parse_upload(
        self, contents: str, filename: str
    ) -> Optional[Union[List[Dict], pd.DataFrame]]:
        """
        Parse uploaded file contents.

        Args:
            contents: Base64 encoded file contents
            filename: Original filename

        Returns:
            Parsed data or None if error
        """
        try:
            # Decode base64
            content_type, content_string = contents.split(",")
            decoded = base64.b64decode(content_string)

            # Get file extension
            file_ext = Path(filename).suffix.lower()

            if file_ext == ".zip":
                return self._parse_zip(decoded)
            elif file_ext == ".json":
                return self._parse_json(decoded)
            elif file_ext == ".csv":
                return self._parse_csv(decoded)
            elif file_ext == ".xlsx":
                return self._parse_excel(decoded)
            else:
                raise ValueError(f"Unsupported file format: {file_ext}")

        except Exception as e:
            print(f"Error parsing upload: {e}")
            return None

    def _parse_zip(self, data: bytes) -> Optional[List[Dict]]:
        """Parse ZIP file and extract JSON data (training_stats.json or any .json file)."""
        try:
            zip_bytes = io.BytesIO(data)

            with zipfile.ZipFile(zip_bytes, "r") as zip_ref:
                # First, try to find training_stats.json (preferred)
                stats_files = [
                    f for f in zip_ref.namelist() if "training_stats.json" in f.lower()
                ]

                # If not found, accept ANY .json file
                if not stats_files:
                    stats_files = [
                        f for f in zip_ref.namelist() if f.lower().endswith(".json")
                    ]

                if not stats_files:
                    raise ValueError("No JSON file found in ZIP. Please include a .json file with checkpoint data.")

                # If multiple JSON files, use the first one
                json_file_name = stats_files[0]
                print(f"Loading JSON file from ZIP: {json_file_name}")

                # Extract and parse
                with zip_ref.open(json_file_name) as json_file:
                    data = json.load(json_file)

                    if not isinstance(data, list):
                        raise ValueError("JSON must be a list of checkpoints")

                    return data

        except Exception as e:
            print(f"Error parsing ZIP: {e}")
            return None

    def _parse_json(self, data: bytes) -> Optional[List[Dict]]:
        """Parse JSON file."""
        try:
            json_data = json.loads(data.decode("utf-8"))
            return json_data
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            return None

    def _parse_csv(self, data: bytes) -> Optional[pd.DataFrame]:
        """Parse CSV file."""
        try:
            df = pd.read_csv(io.BytesIO(data))
            return df
        except Exception as e:
            print(f"Error parsing CSV: {e}")
            return None

    def _parse_excel(self, data: bytes) -> Optional[pd.DataFrame]:
        """Parse Excel file."""
        try:
            df = pd.read_excel(io.BytesIO(data))
            return df
        except Exception as e:
            print(f"Error parsing Excel: {e}")
            return None

    def load_local_file(self, filepath: Union[str, Path]) -> Optional[Union[List[Dict], pd.DataFrame]]:
        """
        Load data from local file.

        Args:
            filepath: Path to file

        Returns:
            Parsed data or None
        """
        filepath = Path(filepath)

        if not filepath.exists():
            print(f"File not found: {filepath}")
            return None

        try:
            if filepath.suffix == ".json":
                with open(filepath, "r", encoding="utf-8") as f:
                    return json.load(f)
            elif filepath.suffix == ".csv":
                return pd.read_csv(filepath)
            elif filepath.suffix == ".xlsx":
                return pd.read_excel(filepath)
            else:
                raise ValueError(f"Unsupported format: {filepath.suffix}")

        except Exception as e:
            print(f"Error loading file: {e}")
            return None


class DataValidator:
    """Validates trading data format and integrity."""

    @staticmethod
    def validate_checkpoint_data(data: List[Dict]) -> bool:
        """
        Validate checkpoint data structure.

        Args:
            data: List of checkpoint dictionaries

        Returns:
            True if valid, False otherwise
        """
        if not isinstance(data, list):
            return False

        if len(data) == 0:
            return False

        # Check required fields in first checkpoint
        required_fields = ["timestep", "balance"]
        sample = data[0]

        return all(field in sample for field in required_fields)

    @staticmethod
    def check_data_quality(data: List[Dict]) -> Dict[str, any]:
        """
        Check data quality and return report.

        Args:
            data: Checkpoint data

        Returns:
            Quality report dictionary
        """
        if not data:
            return {"valid": False, "errors": ["No data"]}

        df = pd.DataFrame(data)

        report = {
            "valid": True,
            "errors": [],
            "warnings": [],
            "stats": {
                "total_checkpoints": len(data),
                "date_range": f"{data[0].get('timestep', 'N/A')} - {data[-1].get('timestep', 'N/A')}",
                "missing_values": df.isnull().sum().to_dict(),
            },
        }

        # Check for missing critical fields
        critical_fields = ["timestep", "balance", "roi"]
        for field in critical_fields:
            if field not in df.columns:
                report["errors"].append(f"Missing critical field: {field}")
                report["valid"] = False

        # Check for duplicates
        if "timestep" in df.columns and df["timestep"].duplicated().any():
            report["warnings"].append("Duplicate timesteps found")

        return report
