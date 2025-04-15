# Contributing to IdentiFile

Thank you for considering contributing to IdentiFile! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

By participating in this project, you agree to abide by the [Code of Conduct](CODE_OF_CONDUCT.md).

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report. Following these guidelines helps maintainers understand your report, reproduce the issue, and find related reports.

- Use a clear and descriptive title for the issue
- Describe the exact steps to reproduce the problem
- Provide specific examples to demonstrate the steps
- Describe the behavior you observed after following the steps
- Explain which behavior you expected to see instead and why
- Include screenshots if possible
- Include details about your configuration and environment

### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including completely new features and minor improvements to existing functionality.

- Use a clear and descriptive title for the issue
- Provide a step-by-step description of the suggested enhancement
- Provide specific examples to demonstrate the steps
- Describe the current behavior and explain which behavior you expected to see instead
- Explain why this enhancement would be useful to most users

### Pull Requests

- Fill in the required template
- Do not include issue numbers in the PR title
- Include screenshots and animated GIFs in your pull request whenever possible
- Follow the Python style guide
- Include tests for your changes
- Document new code
- End all files with a newline

## Development Process

### Setting Up Development Environment

1. Fork the repository
2. Clone your fork locally
   ```bash
   git clone https://github.com/your-username/identifile.git
   cd identifile
   ```
3. Create a virtual environment
   ```bash
   python -m venv env
   source ./env/bin/activate  # On Windows: .\env\Scripts\activate
   ```
4. Install dependencies
   ```bash
   make pip-upgrade
   make pip-install
   ```
5. Create a branch for your feature
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Testing

Before submitting a pull request, make sure to run the tests:

```bash
pytest
```

### Code Style

This project follows the [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide for Python code.

## License

By contributing to IdentiFile, you agree that your contributions will be licensed under the project's [GNU General Public License v3.0](LICENSE).
