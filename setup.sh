#!/usr/bin/env bash

conda env install -f environment.yml
conda activate owsf
earthengine authenticate
