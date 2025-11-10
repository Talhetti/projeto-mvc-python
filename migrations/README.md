# Database Migrations Documentation

This directory contains the migration files for the database schema of the My Python MVC App. 

## Overview

Migrations are used to manage changes to the database schema over time. They allow you to apply and revert changes in a systematic way, ensuring that your database structure is in sync with your application models.

## Applying Migrations

To apply migrations, use the following command:

```
python -m migrate apply
```

This command will apply all pending migrations to the database.

## Creating Migrations

To create a new migration after making changes to your models, use the following command:

```
python -m migrate create <migration_name>
```

Replace `<migration_name>` with a descriptive name for the migration.

## Reverting Migrations

If you need to revert the last applied migration, you can use:

```
python -m migrate revert
```

## Best Practices

- Always back up your database before applying migrations.
- Test migrations in a development environment before applying them in production.
- Keep migration files organized and well-documented for future reference.