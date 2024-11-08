# Database Transfer Project

## Overview
This project facilitates bidirectional data transfer between MySQL and Oracle databases. It includes a Flask web dashboard to monitor the transfer process.

## Directory Structure
- `config/`: Contains configuration files.
- `migrations/`: Scripts for database migration.
- `scripts/`: Main scripts for data transfer and logging.
- `web_dashboard/`: Flask web application for monitoring.
- `tests/`: Unit tests for the scripts.

## Installation
1. Install dependencies:
   ```bash
   pip install mysql-connector-python cx_Oracle Flask schedule
