# IdentiFile

IdentiFile is a REST API for identifying file types based on their content using **Google Magika AI** or standard file header detection. Files are submitted as **multipart/form-data**.

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

## Features

- **Standard Identification**: Identifies files based on their content type headers
- **AI-Powered Identification**: Uses Google's Magika AI for more accurate file type detection
- **Simple REST API**: Easy to integrate with any application
- **Docker Support**: Run as a containerized service

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/version` | GET | Get API version information |
| `/identify` | POST | Identify file using standard header detection |
| `/ai_identify` | POST | Identify file using Google Magika AI |

## Quick Start

### Using Docker

```bash
# Build the Docker image
make docker-build

# Run the Docker container
make docker-start
```

The API will be available at `http://localhost:8079`

### Local Development

#### Prerequisites

- Python 3.9+
- Make

#### Setup

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/identifile.git
   cd identifile
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv env
   source ./env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

3. Install dependencies
   ```bash
   make pip-upgrade
   make pip-install
   ```

4. Start the development server
   ```bash
   make dev
   ```

The API will be available at `http://localhost:8080`

## Usage Examples

### Identify a file using standard detection

```bash
curl -X POST -F "file=@/path/to/your/file.jpg" http://localhost:8080/identify
```

### Identify a file using AI detection

```bash
curl -X POST -F "file=@/path/to/your/file.jpg" http://localhost:8080/ai_identify
```

## Response Format

```json
{
  "method": "ai_identify",
  "mime": "image/jpeg",
  "score": 0.99,
  "description": "JPEG image",
  "label": "jpeg",
  "group": "image",
  "size": 12345,
  "filename": "example.jpg"
}
```

## Built With

- [Google Magika AI](https://github.com/google/magika) - AI-powered file type detection
- [FastAPI](https://fastapi.tiangolo.com/) - Fast web framework for building APIs
- [Python](https://www.python.org/) - Programming language
- [Docker](https://www.docker.com/) - Containerization platform

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.