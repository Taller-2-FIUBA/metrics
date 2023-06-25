# metrics

[![codecov](https://codecov.io/gh/Taller-2-FIUBA/metrics/branch/main/graph/badge.svg?token=naVHuDML0R)](https://codecov.io/gh/Taller-2-FIUBA/metrics)

Service to interact with metrics

## Generic MongoDB document

```json
{"metric": "STRING", "value": "INTEGER", "label": "STRING", "date": "DATE"}
```

Labels are used to add another dimension.

## Generic HTTP response

```json
[
    {
        "label": "total",
        "count": 30
    }
]
```

If metric has not label `total` will be used.

## MongoDB documents for metrics by acceptance criteria

### Trainings

- CA 1: Métricas de nuevos entrenamientos
- CA 2: Métricas de entrenamientos por tipo

```json
{"metric": "trainings_created_count", "value": 1, "label": "Cardio", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "trainings_created_count", "value": 1, "label": "Leg", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "trainings_created_count", "value": 1, "label": "Arm", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "trainings_created_count", "value": 1, "label": "Chest", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "trainings_created_count", "value": 1, "label": "Back", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "trainings_created_count", "value": 1, "label": "Abdomen", "date": "2023-06-24T23:26:45-03:00"}
```

CA 4: Métricas de contenidos por usuario

```json
{"metric": "trainings_by_user_count", "value": 1, "label": "my_user", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "trainings_by_user_count", "value": 1, "label": "my_other_user", "date": "2023-06-24T23:26:45-03:00"}
```

### Users

- CA 1: Métricas de nuevos usuarios utilizando mail y contraseña
- CA 2: Métricas de nuevos usuarios utilizando identidad federada

```json
{"metric": "user_created_count", "value": 1, "label": "using_email_password", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "user_created_count", "value": 1, "label": "using_idp", "date": "2023-06-24T23:26:45-03:00"}
```

- CA 3: Métricas de login de usuarios utilizando mail y contraseña
- CA 4: Métricas de login de usuarios utilizando identidad federada

```json
{"metric": "user_login_count", "value": 1, "label": "using_email_password", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "user_login_count", "value": 1, "label": "using_idp", "date": "2023-06-24T23:26:45-03:00"}
```

- CA 5: Métricas de usuarios bloqueados

```json
{"metric": "user_blocked_count", "value": 1, "date": "2023-06-24T23:26:45-03:00"}
```

- CA 6: Métricas de recupero de contraseña

```json
{"metric": "user_password_recovery_count", "value": 1, "date": "2023-06-24T23:26:45-03:00"}
```

- CA 7: Métricas de usuarios por zona geográfica

```json
{"metric": "user_by_region_count", "label": "belgrano", "value": 1, "date": "2023-06-24T23:26:45-03:00"}
{"metric": "user_by_region_count", "label": "palermo", "value": 1, "date": "2023-06-24T23:26:45-03:00"}
{"metric": "user_by_region_count", "label": "lugano", "value": 1, "date": "2023-06-24T23:26:45-03:00"}
```

### TBD Goals

CA 4: Métricas de contenidos por usuario

```json
{"metric": "goals_by_user_count", "value": 1, "label": "my_user", "date": "2023-06-24T23:26:45-03:00"}
{"metric": "goals_by_user_count", "value": 1, "label": "my_other_user", "date": "2023-06-24T23:26:45-03:00"}
```

The label is the user name.

### TBD

- CA 3: Métricas de usuarios

## HTTP API response

### user_blocked_count

GET to `/metrics?name=user_blocked_count`

```json
[
    {
        "label": "total",
        "count": 1
    }
]
```

### user_login_count

GET to `/metrics?name=user_login_count`

```json
[
    {
        "label": "using_email_password",
        "count": 5
    },
    {
        "label": "using_idp",
        "count": 0
    }
]
```

### user_login_count

GET to `/metrics?name=user_login_count`

```json
[
    {
        "label": "using_email_password",
        "count": 5
    },
    {
        "label": "using_idp",
        "count": 0
    }
]
```

## Virtual environment

Set up:

```bash
sudo apt install python3.11 python3.11-venv
python3.11 -m venv .
source venv/bin/activate
pip install pip --upgrade
pip install -r requirements.txt -r dev-requirements.txt
```

## FastAPI

```bash
uvicorn main:app --reload
```

## Tests

```bash
tox
```

## Local K8s

Building docker image:

```bash
docker build . --tag fiufit/metrics:latest
k3d image import fiufit/metrics:latest --cluster=taller2
```
