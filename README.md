# project-6
Group 6 project for DSCI445 @ CSU

```markdown
# Drum Classifier Project

This project explores machine learning techniques for classifying drum audio samples. The methodology emphasizes data preprocessing, feature extraction using the CREPE library, and model optimization through decision tree algorithms and cross-validation.

## Setup Instructions

### 1. Create a Conda Environment

To ensure reproducibility, create a virtual environment using conda with the requirements specified in the `requirements.txt` file.


conda env create -f environment.yml
conda activate drum_classifier


### 2. Install Additional Packages

If there are any additional packages not included in the `requirements.txt`, you can install them using pip:

```bash
pip install <package_name>
```

### 3. Run the Notebook

Open the Jupyter Notebook and run the cells to execute the code.

```bash
jupyter notebook group_6_paper.ipynb
```

### 4. Project Structure

- `group_6_paper.ipynb`: Main notebook containing the code and analysis.
- `requirements.txt`: List of dependencies required to run the project.
- `sample_features.csv/`: Dataset of extracted audio features and labels
- 'plt_util.py': Helper function to make plots directly from the paper without unnessary code.
- 'ah_kick_gust.wav': Example wav file used for visualization.

### 5. Feature Extraction

The feature extraction process involves running the CREPE library on each WAV file to extract key features such as core frequency, max amplitude, average activation, and duration. These features are saved into a CSV file for further processing and model training.

### 6. Data Cleaning and Balancing

The dataset is cleaned by filtering out samples longer than 10 seconds and balancing the dataset to ensure equal representation of each class.

### 7. Model Training and Evaluation

The project includes various machine learning models such as Ridge and Lasso Regression, Decision Tree, and Support Vector Classification. Each model is trained and evaluated to determine its accuracy in classifying drum samples.

## Authors

- Carlos: Data Wrangling and Exploration
- Olivia: Ridge and Lasso Regression
- Cody: Decision Tree Model
- Aaron: Support Vector Classification
```
