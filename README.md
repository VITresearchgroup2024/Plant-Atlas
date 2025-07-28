# Plant Virus Atlas

```
plant-virus-atlas/
├── README.md # Intro to the Plant Virus Atlas, features, citations
├── LICENSE # License info 
├── .gitignore # Files/folders to ignore during Git operations
├── data/
│ ├── raw/ # Unprocessed raw datasets
│ └── processed/ # Cleaned/filtered data ready for use
├── metadata/ # Sample sheets, source references, etc.
├── scripts/ # Data processing, modeling, and utilities
│ ├── fetch_ncbi.py # Fetch virus, host, and sequence data
│ ├── clean_data.py # Clean and preprocess data
│ ├── sequence_annotation.py # Annotate functional regions
│ ├── docking_pipeline.py # Structural modeling (docking, MD)
│ └── model_training.py # Train spillover risk prediction model
├── notebooks/ # Jupyter notebooks for exploration and demos
│ ├── exploration/ # EDA, plots, data summaries
│ └── modeling/ # Model prototyping
│ ├── prediction_demo.ipynb # End-to-end prediction example
├── models/ # Trained ML models and MD outputs
│ ├── spillover_model.pkl
│ ├── interaction_model.pkl
│ └── md_simulation_results/
├── db/ # Local database and loading utilities
│ ├── schema.sql # SQL schema for SQLite or Neo4j
│ └── load_data.py # Scripts to populate the database
├── queries/ # Reusable query templates
├── app/ # Streamlit app for visualization
│ ├── streamlit_app.py # Main entry point
│ ├── pages/ # Multi-page support (optional)
│ └── assets/ # Icons, images, or frontend assets
├── docs/ # Project documentation
│ ├── schema.md # Explanation of data schema
│ └── usage.md # How to use scripts/app/models
├── contributing.md # Contribution guidelines
├── tests/ # Unit and integration tests
│ └── test_pipeline.py
```
