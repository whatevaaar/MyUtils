#!/bin/bash

echo path?
read path

nitrogen $path
wal -i $path
