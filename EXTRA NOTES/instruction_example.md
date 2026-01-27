# Contoso Companions - Pet Adoption Platform

## Project Overview
This is a web application to support pet adoption agencies. Agencies can onboard into the application, manage their locations, available pets, and publicize events. Potential adopters can search for pets in their area, discover agencies, and submit adoption applications.

## Tech Stack
### Backend
- Flask (Python 3.11+)
- SQLAlchemy ORM for database models
- PostgreSQL database
- pytest for testing

### Frontend
- Astro with Svelte components
- Tailwind CSS for styling
- TypeScript

### APIs & Services
- Stripe for payment processing
- SendGrid for email notifications
- AWS S3 for image storage

## Coding Guidelines

### Python
- Follow PEP 8 style guide
- Use type hints for all function signatures
- Prefer list comprehensions for simple loops
- Catch specific exceptions, never use bare `except:`
- Add descriptive docstrings to all functions

**Example:**
```python
# Good
def calculate_adoption_fee(pet_age: int, pet_type: str) -> float:
    """Calculate adoption fee based on pet characteristics."""
    return base_fee * age_multiplier

# Bad
def CalculateAdoptionFee(age, type):
    total = 0
    # calculation logic
    return total
```

### JavaScript/TypeScript
- Use PascalCase for component names
- Use camelCase for variables and functions
- Always write with double quotes and tabs for indentation
- Prefer `const` over `let`
- Add JSDoc comments to all functions

### Database
- Use migrations for all schema changes (never modify models directly in production)
- Add indexes for frequently queried fields
- Name foreign keys as `{table}_id`

## Project Structure
- `server/` - Flask backend code
  - `models/` - SQLAlchemy ORM models
  - `routes/` - API endpoints organized by resource
  - `tests/` - Unit tests for the API
  - `utils/` - Utility functions and database helpers
- `client/` - Astro/Svelte frontend code
  - `src/components/` - Reusable Svelte components
  - `src/layouts/` - Astro layout templates
  - `src/pages/` - Astro pages and routes
  - `src/styles/` - CSS stylesheets
- `scripts/` - Development, deployment and testing scripts
- `docs/` - Project documentation (keep in sync at all times)

## Development Workflow

### Building & Testing
- Run backend: `python server/app.py`
- Run frontend: `npm run dev` (in client directory)
- Run tests: `pytest server/tests/`
- Run linting: `flake8 server/` and `npm run lint`

### Database
- Create migration: `flask db migrate -m "description"`
- Apply migrations: `flask db upgrade`

## Security Practices
- Never commit API keys or secrets
- Always validate and sanitize user input
- Use parameterized queries for all database operations
- Check for hardcoded credentials in code reviews

## Resources
- API documentation: `/docs/api.md`
- Design system: `/docs/design-system.md`
- Deployment guide: `/docs/deployment.md`