#!/bin/bash
mkdir -p lambdas/lambda_retrieve_data/layer/python/lib/python3.8/site-packages
pip3 install -r lambdas/lambda_retrieve_data/requirements.txt -t lambdas/lambda_retrieve_data/layer/python/lib/python3.8/site-packages/
zip -r lambdas/lambda_retrieve_data/bar_code_reader_setup.zip lambdas/lambda_retrieve_data/layer/*
echo "lambda layer available at files/bar_code_reader_setup.zip"