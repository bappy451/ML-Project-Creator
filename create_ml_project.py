import os
import argparse

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")

def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)
    print(f"Created file: {path}")

def create_makefile(project_path):
    makefile_content = """\
.PHONY: help setup create clean

help:
\t@echo "Makefile commands:"
\t@echo "  setup           Install Python dependencies from requirements.txt"
\t@echo "  create NAME DIR Create ML project folder 'NAME' in directory 'DIR' (DIR optional)"
\t@echo "  clean           Remove created project folder"

setup:
\tpython -m pip install -r requirements.txt

create:
\t@if [ -z "$(NAME)" ]; then \\
\t\techo "Error: Please provide project name with NAME variable"; \\
\t\techo "Usage: make create NAME=project_name [DIR=target_directory]"; \\
\t\texit 1; \\
\tfi
\t@DIR=$(DIR); \\
\tif [ -z "$$DIR" ]; then DIR=.; fi; \\
\tpython create_ml_project.py $$NAME $$DIR

clean:
\t@if [ -z "$(NAME)" ]; then \\
\t\techo "Error: Please provide project name with NAME variable"; \\
\t\techo "Usage: make clean NAME=project_name"; \\
\t\texit 1; \\
\tfi
\trm -rf $(NAME)
\t@echo "Removed project folder '$(NAME)'"
"""
    makefile_path = os.path.join(project_path, "Makefile")
    create_file(makefile_path, makefile_content)

def main():
    parser = argparse.ArgumentParser(
        description="Create a structured ML project directory with placeholder files."
    )
    parser.add_argument("project_name", help="Name of the ML project folder to create")
    parser.add_argument(
        "folder_path",
        nargs="?",
        default=".",
        help="Target directory where project folder will be created (default: current directory)"
    )

    args = parser.parse_args()

    project_name = args.project_name
    folder_path = os.path.abspath(args.folder_path)
    project_path = os.path.join(folder_path, project_name)

    # Create folders and files as before
    create_folder(project_path)
    create_folder(os.path.join(project_path, "data", "raw"))
    create_folder(os.path.join(project_path, "data", "processed"))
    create_folder(os.path.join(project_path, "data", "external"))
    create_folder(os.path.join(project_path, "notebooks"))

    src_path = os.path.join(project_path, "src")
    create_folder(src_path)
    create_folder(os.path.join(src_path, "data"))
    create_folder(os.path.join(src_path, "features"))
    create_folder(os.path.join(src_path, "models"))
    create_folder(os.path.join(src_path, "evaluation"))
    create_folder(os.path.join(src_path, "utils"))
    create_folder(os.path.join(src_path, "visualization"))
    create_file(os.path.join(src_path, "__init__.py"))

    create_folder(os.path.join(project_path, "configs"))
    sample_config = """# Example config file
data_path: ./data/processed/
model_params:
  learning_rate: 0.001
  batch_size: 32
"""
    create_file(os.path.join(project_path, "configs", "config.yaml"), sample_config)

    create_folder(os.path.join(project_path, "tests"))
    sample_test = """import unittest

class SampleTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
"""
    create_file(os.path.join(project_path, "tests", "test_sample.py"), sample_test)

    create_folder(os.path.join(project_path, "scripts"))
    sample_train_script = """def main():
    print("Training script placeholder")

if __name__ == '__main__':
    main()
"""
    create_file(os.path.join(project_path, "scripts", "train.py"), sample_train_script)

    create_folder(os.path.join(project_path, "outputs", "models"))
    create_folder(os.path.join(project_path, "outputs", "logs"))
    create_folder(os.path.join(project_path, "outputs", "predictions"))

    requirements_content = """# Add your python dependencies here
numpy
pandas
scikit-learn
"""
    create_file(os.path.join(project_path, "requirements.txt"), requirements_content)

    readme_content = f"""# {project_name}

Project overview.

## Structure

- data/: Dataset folders (raw, processed, external)
- notebooks/: Jupyter notebooks for EDA and experiments
- src/: Source code modules (data processing, features, models, evaluation, utils, visualization)
- configs/: Configuration files for parameters
- tests/: Unit tests
- scripts/: Run training, evaluation, inference scripts
- outputs/: Save models, logs, predictions
- requirements.txt: Python dependencies

## Usage

Explain how to run your project here.
"""
    create_file(os.path.join(project_path, "README.md"), readme_content)

    gitignore_content = """# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.env
env/
venv/
ENV/
*.env

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Data files
data/raw/
data/external/

# Outputs
outputs/
"""
    create_file(os.path.join(project_path, ".gitignore"), gitignore_content)

    # Create Makefile automatically
    create_makefile(project_path)

    print(f"\nProject structure created successfully at: {project_path}")

if __name__ == "__main__":
    main()
