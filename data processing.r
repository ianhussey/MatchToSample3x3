########################################################################
# Create summary stats from data produced by the MTS 3x3,
# programmed in PsychoPy 1.82
# Ian.Hussey@ugent.be
########################################################################
# Notes:
# Produces pass/fail data and number of blocks required. 
# Analysis of trial level acc/lat data would be possible too.

########################################################################
# Clean the workspace
rm(list=ls())

########################################################################
# Dependencies
library(plyr)
library(dplyr)
library(data.table)

########################################################################
# Data acquisition and cleaning

setwd("~/git/MatchToSample/data")
files <- list.files(pattern = "\\.csv$")  # Create a list of the csv files in this folder

df <- tbl_df(rbind.fill(lapply(files, fread, header=TRUE)))  # Read these files into a single dplyr-style data frame. 

########################################################################
# Data processing

processing_df <- 
  rename(df, # Make some variable names more transparent
         current_training_block = training.thisRepN, 
         current_testing_block = testing.thisRepN, 
         training_summary = post_training.thisRepN,
         testing_summary = post_testing.thisRepN,
         rt = response.rt,
         accuracy = response.corr) %>%
  mutate(current_training_block = current_training_block + 1,  # recitfy to start at 1 rather than 0
         current_testing_block = current_testing_block + 1) %>%  # recitfy to start at 1 rather than 0
  select(participant, 
         gender,
         age,
         date,
         current_training_block,
         current_testing_block,
         training_summary,
         testing_summary,
         passed_training,
         passed_testing,
         rt,
         accuracy,
         current_block,
         block_summary_column)


 <-
  filter(df, !is.na(block_summary_column)) %>%  # summary columns only
  group_by(participant) %>%
  mutate(highest_n_block = max(current_block)) %>%
  filter(current_block == highest_n_block) %>%  # get only the last block that each participant completed
  select(participant, 
         gender,
         age,
         date,
         passed_training,
         highest_n_block)

# Write to file
write.csv(processing_df, file = "~/git/MatchToSample/processed_MTS_data.csv", row.names=FALSE)
