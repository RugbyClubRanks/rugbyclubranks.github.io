import glob
import os
import pytest
import random
import re

def test_comp_contents():
    comp_files = glob.glob(os.path.join("comp_files", "*.md"))
    assert len(comp_files) > 0

def test_comp_plot_contents():
    comp_file_plots = glob.glob(os.path.join("comp_files/plots", "*"))
    assert len(comp_file_plots) > 0

def test_projections_contents():
    comp_files = glob.glob(os.path.join("projections", "*.md"))
    assert len(comp_files) > 0

def test_reviews_contents():
    comp_files = glob.glob(os.path.join("reviews", "*.md"))
    assert len(comp_files) > 0

def test_comp_random_accuracy():
    club_accuracy = None
    tbl_values = None
    comp_files = glob.glob(os.path.join("comp_files", "*.md"))

    while tbl_values == None:
        rand_comp_file = random.choice(comp_files)
        with open(rand_comp_file) as fp:
            content = fp.read()
            if "# Completed Match Review" in content:
                accuracy_tbl = content.split("# Completed Match Review")[1].split("\n\n\n")[1]
                tbl_values = list(map(float, re.findall(r"[0-9.]+", accuracy_tbl)))

    tbl_accuracies = tbl_values[::2]
    tbl_errors = tbl_values[1::2]

    assert (min(tbl_accuracies) >= 0) & (max(tbl_accuracies) <= 100) & (min(tbl_errors) >=0)

def test_comp_random_playoff():
    club_accuracy = None
    tbl_values = None
    comp_files = glob.glob(os.path.join("comp_files", "*.md"))

    while tbl_values == None:
        rand_comp_file = random.choice(comp_files)
        with open(rand_comp_file) as fp:
            content = fp.read()
            if "## Projected Playoff Results" in content:
                playoff_tbl = content.split("## Projected Playoff Results")[1].split("\n\n\n\n")[0]
                tbl_values = list(map(float, re.findall(r"[0-9.]+", playoff_tbl)))
    
    ## Should print comp on failure, maybe check all?

                
    assert (min(tbl_values) >= 0) & (max(tbl_values) <= 100)
    

