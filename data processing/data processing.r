########################################################################
# Create summary stats from data produced by the 
# One-to-Many Match to Sample task
# Author: Ian.Hussey@ugent.be
########################################################################
# Notes:
# Produces pass/fail summary data, including number of blocks required 
# and total number of completed trials for both training and testing.

# Known issues:
# None.

########################################################################
# Clean the workspace
rm(list=ls())

########################################################################
# Dependencies
library(plyr)
library(dplyr)
library(tidyr)
library(data.table)

########################################################################
# Data acquisition and cleaning
setwd("~/git/MatchToSample3x3/data")
files <- list.files(pattern = "\\.csv$")  # Create a list of the csv files in this folder
df <- tbl_df(rbind.fill(lapply(files, fread, header=TRUE)))  # Read these files into a single dplyr-style data frame. 

########################################################################
# Data cleaning
cleaning_df <- 
  rename(df, # Make some variable names more transparent
         rt = response.rt,
         accuracy = response.corr,
         n_training_and_testing = training_and_testing.thisRepN,
         n_training = training.thisRepN,
         n_testing = testing.thisRepN,
         training_summary_rows_only = post_training_loop.thisRepN,
         testing_summary_rows_only = post_testing_loop.thisRepN) %>%
  mutate(n_training_and_testing = n_training_and_testing +1,
         n_training = n_training +1,
         n_testing = n_testing +1) %>%  # recitfy to start at 1 rather than 0
  select(participant, 
         gender,
         age,
         date,
         rt,
         accuracy,
         trial_description,
         passed_training,
         passed_testing,
         n_training_and_testing,
         n_training,
         n_testing,
         training_summary_rows_only,
         testing_summary_rows_only)

# block summaries
block_summaries_df <-
  filter(cleaning_df, 
         !is.na(training_summary_rows_only) | 
           !is.na(testing_summary_rows_only)) %>%  # summary rows only
  select(participant, 
         gender,
         age,
         date,
         n_training_and_testing,
         n_training,
         n_testing,
         passed_training,
         passed_testing) %>%
  filter(n_training_and_testing == max(n_training_and_testing, na.rm = TRUE) &  # take only the last cycle of training and testing
           (n_training == max(n_training, na.rm = TRUE) |  # and either the last row of training
              n_testing == max(n_testing, na.rm = TRUE)))  # or the last row of testing

# condense the two rows created for each participant into one
condense_summaries_df <-
  group_by(block_summaries_df, participant) %>%
  summarize(n_training_and_testing = max(n_training_and_testing, na.rm = TRUE),
            n_training = max(n_training, na.rm = TRUE),
            n_testing = max(n_testing, na.rm = TRUE), 
            passed_training = as.logical(max(passed_training, na.rm = TRUE)),
            passed_testing = as.logical(max(passed_testing, na.rm = TRUE)))

# extract demographics info from a previous df
demographics_df <- 
  select(block_summaries_df, 
         participant, 
         gender,
         age,
         date) %>%
  distinct(participant)

# count trials per block
# this is used below to calculate the total trials they were exposed to.
training_block_length_df <-
  filter(cleaning_df, 
         n_training_and_testing == 1 & n_training == 1 & !is.na(accuracy)) %>%  # !is.na(accuracy) is neede because the summary trial row is also included otherwise 
  group_by(participant) %>%
  summarize(n_trials_per_training_block = sum(n_training))  # can't get count() or tally() to work here, no idea why.

testing_block_length_df <-
  filter(cleaning_df, 
         n_training_and_testing == 1 & n_testing == 1 & !is.na(accuracy)) %>%  # !is.na(accuracy) is neede because the summary trial row is also included otherwise 
  group_by(participant) %>%
  summarize(n_trials_per_testing_block = sum(n_testing))  # can't get count() or tally() to work here, no idea why.

# join the summaries and the demographics for output
joined_df <- 
  join_all(list(demographics_df, 
                condense_summaries_df, 
                training_block_length_df,
                testing_block_length_df),
           by = "participant",
           type = "full")

# calculate total trials each participant was exposed to
output_df <- 
  group_by(joined_df, participant) %>%
  mutate(total_training_trials = n_training_and_testing * n_training * n_trials_per_training_block,
         total_testing_trials = n_training_and_testing * n_testing * n_trials_per_testing_block)

# Write to file
write.csv(output_df, file = "~/git/MatchToSample3x3/analysis/MTS_summary_data.csv", row.names=FALSE)

