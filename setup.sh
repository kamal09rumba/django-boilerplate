#!/bin/bash

# Install Development Dependencies
pip install -r requirements-dev.txt


# Initialize hooks4git
hooks4git --init

# Remove created extra hooksforgit file
hooks4gitversion="$(hooks4git --version)"
hooks4gitversion=${hooks4gitversion##* }
rm .hooks4git-"$hooks4gitversion".ini
