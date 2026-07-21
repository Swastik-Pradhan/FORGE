# Forge CLI Command Reference

Current Version: **v0.2.0**

---

# General

## Show Help

```bash
python -m forge.main --help
```

## Show Version

```bash
python -m forge.main version
```

---

# AI Module

## Help

```bash
python -m forge.main ai --help
```

## Summarize a File

```bash
python -m forge.main ai summarize forge/main.py
```

---

# Git Module

## Help

```bash
python -m forge.main git --help
```

## Git Status

```bash
python -m forge.main git status
```

## AI Commit Message

```bash
python -m forge.main git commit-msg
```

---

# Dev Module

## Help

```bash
python -m forge.main dev --help
```

## Generate README

```bash
python -m forge.main dev readme MyProject
```

## Generate Dockerfile

```bash
python -m forge.main dev dockerize
```

## Generate .gitignore

```bash
python -m forge.main dev gitignore
```

---

# Database Module

## Help

```bash
python -m forge.main db --help
```

## Connect Database

```bash
python -m forge.main db connect-db sample.db
```

## List Tables

```bash
python -m forge.main db tables
```

## Show Table Schema

```bash
python -m forge.main db schema users
```

## Execute SQL Query

```bash
python -m forge.main db query "SELECT * FROM users"
```

---

# Security Module

## Help

```bash
python -m forge.main sec --help
```

## SHA-256 Hash

```bash
python -m forge.main sec hash README.md
```

## Scan Local Ports

```bash
python -m forge.main sec ports
```

---

# Quick Help

| Module | Command |
|---------|---------|
| Version | `version` |
| AI | `summarize` |
| Git | `status` |
| Git | `commit-msg` |
| Dev | `readme` |
| Dev | `dockerize` |
| Dev | `gitignore` |
| Database | `connect-db` |
| Database | `tables` |
| Database | `schema` |
| Database | `query` |
| Security | `hash` |
| Security | `ports` |