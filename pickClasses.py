#!/usr/bin/python3
import argparse
import sys
import json

parserSingleton = argparse.ArgumentParser()

parserSingleton.add_argument("-c","--classes",
    nargs="+",
    help="List of classes to attempt to register for"
)
parserSingleton.add_argument("-m","--min-classes",
    type=int,
    help="minimum number of classes to register for",
    dest="min",
)
parserSingleton.add_argument("-M","--max-classes",
    type=int,
    help="maximum number of classes to register for",
    dest="max",
)
parserSingleton.add_argument("-o","--json-location",
    nargs=1,
    default="./classes.json",
    dest="databasePath"
)

args = parserSingleton.parse_args()

global database
with open(args.databasePath) as file:
    database = json.open(file)["data"]

print(database[0])

