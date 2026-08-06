# MoodTune AI

MoodTune AI is a context-aware music recommendation system that generates personalised playlists using a user's mood, preferred genre, language, listening context, and music preferences.

## Project Objectives

The project aims to:

* Detect the user's mood from text input.
* Predict suitable music genres.
* Support multilingual music preferences.
* Generate recommendations based on listening context.
* Integrate with the Spotify API.
* Learn from likes, dislikes, skips, and saved tracks.
* Provide explanations for generated recommendations.
* Evaluate machine-learning models and recommendation quality.

## Planned Features

* Mood classification
* Genre classification
* Language selection
* Listening-context selection
* Spotify track retrieval
* Personalised recommendation ranking
* Explainable recommendations
* User profiles and preferences
* Like, dislike, save, and skip feedback
* Playlist history
* Recommendation analytics
* Model evaluation dashboard

## Technology Stack

### Backend

* Python
* FastAPI
* Pydantic

### Frontend

* Streamlit

### Data Science

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Jupyter Notebook

### Database

* PostgreSQL or Supabase

### External Services

* Spotify Web API

### Development Tools

* Git
* GitHub
* Pytest
* Ruff
* Docker
* GitHub Actions

## Initial Project Structure

```text
mood-context-music-recommender/
├── backend/
│   └── app/
│       ├── api/
│       ├── core/
│       ├── models/
│       ├── recommender/
│       └── services/
├── frontend/
├── notebooks/
├── data/
│   ├── raw/
│   └── processed/
├── tests/
├── docs/
├── reports/
├── .env.example
├── .gitignore
├── pyproject.toml
├── requirements.txt
└── requirements-dev.txt
```

## Project Phases

1. Project setup and architecture
2. FastAPI backend foundation
3. Streamlit frontend foundation
4. Spotify API integration
5. Dataset exploration and preprocessing
6. Mood-classification model
7. Genre-classification model
8. Recommendation and ranking engine
9. User preferences and feedback
10. Database and authentication
11. Analytics and model evaluation
12. Testing, Docker, CI/CD, and deployment
13. Portfolio documentation

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/SMCodeX7/mood-context-music-recommender.git
cd mood-context-music-recommender
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment on Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install development dependencies

```bash
python -m pip install -r requirements-dev.txt
```

### 5. Create the environment file

Copy `.env.example` to `.env` and add the required private credentials.

Never commit the `.env` file to GitHub.

## Development Workflow

Development is completed through separate branches.

```text
main
├── setup
├── backend
├── frontend
├── spotify
├── mood-model
├── genre-model
├── recommender
├── database
├── testing
└── deployment
```

Each completed checkpoint is tested, committed, pushed, and merged through a pull request.

## Current Status

* [x] GitHub repository created
* [x] Development branch created
* [x] Python virtual environment configured
* [x] Initial project structure created
* [x] Development tools configured
* [ ] FastAPI backend
* [ ] Streamlit frontend
* [ ] Spotify integration
* [ ] Machine-learning models
* [ ] Recommendation engine
* [ ] Database
* [ ] Deployment

## Licence

This project is licensed under the MIT License.
