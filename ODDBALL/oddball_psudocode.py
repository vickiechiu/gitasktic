"""Oddball Experiment
created by Paul Z. Cheng

Experimental flow:
    (1). Imports and Setups
    (2). Functions
    (3). Excution

** Word on debuging:
    This script is design for minimal variable adjustment in function
    and Excution. All input variable is defined either in configuration file or
    Import and Setup.
"""

## Script Partition ##
instruction = True
demo_gui = True
beh = True
debug = False
fullscr = False

##############################
### (1).Imports and Setups ###
##############################

## Global imports ##

## Local import ##

## Experimental conditons generation ##
blocks = list_gene(config)

## Run Demographic interface ##
# get demographic data for log ouput
if demo_gui:


## Behavior initate  ##
if beh:
    ## Time Configuration ##

    ## Log Configuration

    ## Create window ##

    ## stimulus initation
    # Setup each present stimulus before experiment began
    # Fixation cross is just the character "+".

    # Initate parallel port for eeg


###################
## (2).Functions ##
###################

## Helper functions
# Keypress need to add in exit key()

# A function for present prompts
def block_prompt():
    """presnts out
    """
# Block construction
# takes in list gene



# Need a function for breaks
def run_block(blocks, bn, config):
    for tr in range(len(blocks[bn])):
        ## Inter Stimulus Interval (ISI) ##

        ## stimulus On ##

        ## Response duration ##
        # need to setup so keypress is on when stimulus is on

        # Log Response after receive respond


def exp(blocks, config, glob_t, instruct):
    ## Instructions ##

    # Show examples

    # Final instructions before experiment start

    ## Initate Experimental ##
    for bn in range(len(blocks)):
        block_prompt()
        # Beginning of each block
        run_block()

    # Experiment End prompt
    prompt(finished_inst)

###########################
## (3).Excute Experiment ##
###########################
if __name__ == "__main__":
    # Run Experiment
    if beh:
        exp(args*)
