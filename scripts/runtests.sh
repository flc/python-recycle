#!/bin/bash

rm -rf coverage_report
time pytest $*
