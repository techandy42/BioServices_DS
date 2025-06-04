# BioServices_DS

Dataset of BioServices code containing signatures and docstrings.

### Environment Setup ⚙️

> Initial Setup

```bash
# Create and activate virtual environment
conda create -n bioservices-ds python=3.11
conda activate bioservices-ds
# Clone into the external_packages directory
git clone https://github.com/techandy42/bioservices.git external_packages/bioservices
# Create a symbolic link in your project's root directory
ln -s external_packages/bioservices/bioservices bioservices
```

> Reusing the Environment

```bash
# Activate virtual environment
conda activate bioservices-ds
```

### Data & Formatting 📁

> Data Annotations

- Each JSON folder under `data/modules/<module_name>/` contains annotated data for that particular BioServices module.
- Please run `python3 format_dataset.py` to convert all of the modules' JSON data into BioMANIA compatible format as a single JSON file.
- The provided `API_data.json` file contains all of the modules' API in BioMANIA compatible format.

> Running Commands

- `bioservices_run_examples.ipynb` notebook is provided to showcase how each API can be ran.

### Status on Data Annotation ⏰

- The status can be check at `data/status.yaml` for each of the modules.
- The API format validation is completed. However, there some APIs that have issues running, modules that have server failures, or API calls that require further research into valid inputs (some of them very nuansed and require domain knowledge).
