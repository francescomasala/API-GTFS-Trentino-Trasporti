import csv
import json
import os
import shutil
from datetime import datetime

import wget
import zipfile
import botogram

def csvtojson(csvPath, jsonPath) :
    dataset = []
    with open(csvPath, encoding='utf-8-sig') as csvDataset :
        csvreader = csv.DictReader(csvDataset)
        for rows in csvreader :
            dataset.append(rows)
    with open(jsonPath, 'w', encoding='utf-8-sig') as jsonDataset :
        jsonDataset.write(json.dumps(dataset, indent=4))
    dataset.clear()
    print("Done converting: " + csvPath + " to: " + jsonPath)


def downloader(webPath, filePath) :
    print("Downloading: " + webPath)
    wget.download(webPath, filePath)


def extractor(zipPath, zipExtract) :
    print("Extracting dataset")
    with zipfile.ZipFile(zipPath, 'r') as zipRef :
        zipRef.extractall(zipExtract)
    print("Extracted!")


def init():
    os.mkdir("web/txt_datasets")
    os.mkdir("web/json_datasets")
    os.mkdir("web/json_datasets/Urban")
    os.mkdir("web/json_datasets/Suburban")

def cleanup():
    shutil.rmtree("web/json_datasets")
    shutil.rmtree("web/txt_datasets")


def announce_update():
    chan = botogram.channel("@tt_api", "API-KEY")
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    chan.send("Dataset updated on: " + "`" + dt_string + "`\n" +
              "You can see it on: https://raw.tt.api.francescomasala.me/", syntax="markdown")
