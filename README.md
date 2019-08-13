

# Accessing

The MongoDB runs on an Atlas cluster.


# Deploying / Running

## Scraper Setup

Run the following commands

```
cd scraper
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python scrape.py
```

For the articles to be saved to the database, a config.yaml file must be created with the database connection settings. Refer to config_example.yaml for the structure.

## Flask Server Setup

Run the following commands

```
cd server
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python server.py
```
