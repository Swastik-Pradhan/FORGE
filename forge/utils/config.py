"""
Global configuration for Forge.

This module stores application-wide constants and default settings.
"""

# --------------------------------------------------
# Application Information
# --------------------------------------------------

APP_NAME = "Forge"
VERSION = "0.2.0"

# --------------------------------------------------
# AI Configuration
# --------------------------------------------------

DEFAULT_MODEL = "deepseek-coder"
DEFAULT_ENCODING = "utf-8"

# Future AI settings
TEMPERATURE = 0.2
MAX_CONTEXT_TOKENS = 4096

# --------------------------------------------------
# Database Configuration
# --------------------------------------------------

SUPPORTED_DATABASES = [
    "sqlite",
    "mysql",
    "postgresql",
]

# --------------------------------------------------
# Logging
# --------------------------------------------------

LOG_LEVEL = "INFO"
LOG_FILE = "forge.log"

# --------------------------------------------------
# Project
# --------------------------------------------------

SUPPORTED_CODE_EXTENSIONS = [
    ".py",
    ".cpp",
    ".c",
    ".java",
    ".js",
    ".ts",
    ".go",
    ".rs",
]