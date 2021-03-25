# Job Search

This applications allows candidates to find jobs through different Job Source platforms.

## Getting Started

To run the project locally, clone the project and follow these instructions.

### Server setup

Navigate to the frontend repository.

```bash
cd job-source/client
```
Make sure you have npm installed. Install project dependancies

```bash
npm install
```
This should spinup the website at <http://localhost:3000/>

### Client setup

Open another terminal and navigate to:

```bash
cd job-source/backend
```

Make sure you've pip installed and install virtualenv package.
```bash
pip install virtualenv
```

Create a virtual environment in this repository

```bash
virtualenv venv
```
Install all depandancies

```bash
pip install -r requirements.txt
```
Run the main file

```bash
python src/main.py
```
This will spinup the server at <http://localhost:5000/>



## Project Overview 

1. Database Architecture
    1. It uses four database tables: Job Opportunity, Job Board, Job root and Job Source
    2. Job Opportunity and Job Board are where the sample data are stored.
    3. Job root table stores "registered domains" of all the given urls(Job Opportunities), which forms a bridge between Job Opportunity table and Job Board table.
    4. Each entity in Job Root, has info about the domain name and the Job Source name(if any)
    4. Job source tables stores the names of all Job sources which will later be used to resolve Job opportunities in O(1) time complexity.
2. API Framework and UI
    1. The architecture is then effectively used to query data through indexing, thereby drastically cutting down time for network calls
    2. User Interface provides access to all the Job Source Boards with details about each Job source
    3. Each of these boards take us to a different page that display all the job opportunities posted in that job Board

### References

1. Please find the Job Source Resolver logic in: `/backend/src/seedops/populate_db.py`

2. Resolved Job Opportunites CSV file can be found in: `/backend/src/utils/job_source_resolution_data.csv`

3. Visual representation showing the job source and the total count of job opportunities associated with that job source can be found here: `/backend/src/utils/job_source_map.png`

4. Third party library used in this project are:
    1. tldextract: To extract domain names for a given url as it accurately separates the gTLD or ccTLD (generic or country code top-level domain) from the registered domain and subdomains of a URL
    2. Flask, SQLAlchemy, Marshmallow: Framework to build database and create API endpoints
    3. Antd: React UI library to build high quality components


