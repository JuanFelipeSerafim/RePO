#!/bin/bash

cat ./data/packet_based/monday.zip_parta* > ./data/packet_based/monday.zip
cat ./data/packet_based/tuesday.zip_parta* > ./data/packet_based/tuesday.zip
cat ./data/packet_based/wednesday.zip_parta* > ./data/packet_based/wednesday.zip

unzip ./data/packet_based/monday.zip -d ./data/extracted_packet_based
unzip ./data/packet_based/tuesday.zip -d ./data/extracted_packet_based
unzip ./data/packet_based/wednesday.zip -d ./data/extracted_packet_based
unzip ./data/packet_based/thursday.zip -d ./data/extracted_packet_based
unzip ./data/packet_based/friday.zip -d ./data/extracted_packet_based