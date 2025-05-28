# ML-Project-Creator
Industry grade ML/DL project creator script in python

# ML Project Structure Creator

A simple Python script to quickly generate a well-organized machine learning project folder structure with essential subfolders and placeholder files. This helps to kickstart ML projects with best practices and maintainable code organization.

---

## Features

- Creates typical ML project directories such as `data/`, `notebooks/`, `src/` with modular subfolders.
- Adds placeholder files like `README.md`, `.gitignore`, sample config, sample test, and training script.
- Supports custom project name and target folder path.
- Helps enforce clean, modular, and scalable ML project setups.

---

## Usage

Run the script with Python, providing the **project name** and optionally the **target directory path**:

```bash
python create_ml_project.py <project_name> [folder_path]
````

* `<project_name>` (required): Name of your ML project folder.
* `[folder_path]` (optional): Path where the project folder will be created. Defaults to current directory (`.`).

### Examples

Create project `my_ml_project` in current directory:

```bash
python create_ml_project.py my_ml_project
```

Create project `my_ml_project` inside `/home/user/projects`:

```bash
python create_ml_project.py my_ml_project /home/user/projects
```

Create project `my_ml_project` explicitly in current directory:

```bash
python create_ml_project.py my_ml_project .
```

---

## Project Structure Created

```
<project_name>/
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
├── notebooks/
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── evaluation/
│   ├── utils/
│   ├── visualization/
│   └── __init__.py
├── configs/
│   └── config.yaml
├── tests/
│   └── test_sample.py
├── scripts/
│   └── train.py
├── outputs/
│   ├── models/
│   ├── logs/
│   └── predictions/
├── requirements.txt
├── README.md
├── Makefile
└── .gitignore

```
---

## Description of Key Folders and Files

* `data/`: Stores datasets — raw, processed, and external.
* `notebooks/`: Jupyter notebooks for exploration and experimentation.
* `src/`: Source code modules split by functionality.
* `configs/`: Configuration files (e.g., hyperparameters, paths).
* `tests/`: Unit tests for validating your code.
* `scripts/`: Execution scripts such as training and evaluation.
* `outputs/`: Outputs including trained models, logs, and predictions.
* `requirements.txt`: Python package dependencies.
* `.gitignore`: Typical files and folders to exclude from Git.

---

## Extending the Script

You can customize or extend the script by:

* Adding templates for other scripts (e.g., inference, evaluation).
* Including environment setup files like `environment.yml` or Dockerfile.
* Enhancing config templates.
* Adding CI/CD pipeline examples.

---

## Requirements

* Python 3.x

No external dependencies required.

---

## License

This script is open for your personal or commercial use.

---

## Author

Created by Md Min-Ha-Zul Abedin

