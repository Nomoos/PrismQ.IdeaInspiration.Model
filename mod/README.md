# Business/Domain Modules (`mod/`)

This directory contains business logic and domain-specific modules for the PrismQ.IdeaInspiration.Model package.

## Purpose

The `mod/` directory is designed to hold higher-level modules that implement:
- Business logic and domain models (beyond the core model)
- Use case implementations
- Domain-specific workflows
- Application-specific extensions

## Separation of Concerns

The repository follows a clear separation:

- **`prismq/`** - Core Python package implementation
  - `prismq/idea/model/` - Core IdeaInspiration model
  - Core data structures and base functionality
  - Package initialization and common functionality

- **`mod/`** - Business/domain modules (this directory)
  - Domain-specific implementations
  - Business logic modules
  - Higher-level application components
  - Use case orchestration

## Structure

Each module in this directory should be self-contained and follow these guidelines:

```
mod/
├── README.md                 # This file
├── ModuleExample/           # Example domain module
│   ├── __init__.py
│   └── ... (module files)
└── YourModule/              # Your domain modules
    ├── __init__.py
    └── ... (module files)
```

## Guidelines

When creating new modules:

1. **Single Responsibility**: Each module should focus on a specific domain or business concern
2. **Dependency Injection**: Depend on `prismq/` infrastructure via interfaces/protocols
3. **Testing**: Add corresponding tests in `tests/mod/YourModule/`
4. **Documentation**: Document the module's purpose, inputs, and outputs
5. **SOLID Principles**: Follow SOLID design principles (see `.github/copilot-instructions.md`)

## Examples

Future domain modules can be added here as the ecosystem grows. For example:
- **Builders** - Factory methods for creating IdeaInspiration from various sources
- **Validators** - Domain-specific validation logic
- **Transformers** - Data transformation utilities

## Related Documentation

- Main README: `/README.md`
- Copilot Instructions: `/.github/copilot-instructions.md`
- Core Model: `/prismq/idea/model/`
