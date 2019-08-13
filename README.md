

# Accessing

The MongoDB runs on an Atlas cluster.


# Deploying / Running

The Python version used is 3.7.

Do not use Python lower than 3.5, as the asyncio / aiohttp libraries are relatively recent.

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
