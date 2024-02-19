
> IdentiFile is a Rest API for identifying submitted file based on it content type using **'Google Magika AI'** or **standard** file header as **multipart/form-data**.

>thanks to.
> 
> [Google Magika AI](https://github.com/google/magika)
>
> [FastAPI](https://fastapi.tiangolo.com/)
>
> [Python](https://www.python.org/)
>
> [Docker](https://www.docker.com/)


### Prepare Project For Development (MacOS, Ubuntu)

1. setup python env by `python -m venv env`
2. set env by `source ./env/bin/activate`
3. upgrade pip for env `make pip-upgrade`
4. install dependencies: `make pip-install`

### Start Development Server
`$ make dev`

### Build Docker Image
`make build`

### Run Docker Image
`make run`