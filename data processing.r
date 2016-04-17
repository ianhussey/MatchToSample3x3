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

df <- 
  rename(df, # Make some variable names more transparent
         current_block = blocks_loop.thisRepN, 
         block_summary_column = postblock_loop.thisRepN,
         rt = response.rt,
         accuracy = response.corr) %>%
  mutate(current_block = current_block + 1) %>%  # recitfy to 1-12 rather than 0-11
  select(participant, 
         gender,
         age,
         date,
         passed_training,
         rt,
         accuracy,
         current_block,
         block_summary_column)
  
########################################################################
# Data processing
processing_df <-
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
