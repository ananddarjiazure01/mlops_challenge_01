## Solution
https://arinco.com.au/author/ben-robertsarinco-com-au/

## Used UV package in this ML project

```
pip install uv
```

## Initialize project
```
uv init
```

## Install Py 3.12
```
uv python install 3.12
```

###
Update python version in .python-version and pyproject.toml file

## Add env
```
uv venv
```
## Activate venv
```
.venv/Scripts/Active
```

## To run
```
cd ./src/model
uv run train.py --training_data ../../production/data --reg_rate 0.01
```


az ml data create --file datasets.yml --workspace-name az-mlops --resource-group ml

```
az ml job create --file job.yml --resource-group ml --workspace-name az-mlops
```

## Set up github action secret.
https://github.com/marketplace/actions/azure-login
