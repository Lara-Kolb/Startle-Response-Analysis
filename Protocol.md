# Protocol on Startle Response Experiments

## Table of contents

1. [Introduction](#intro)
2. [Experimental Design](#exp_des)
    1. [Setup](#setup)
    2. [Procedure](#procedure)
3. [Software](#software)
    1. [Recording](#recording)
    2. [Analysis](#analysis)
4. [Troubleshooting](#troubleshooting)



## Introduction <a name="intro"></a>

This is a protocol and guide for the startle response experiments. First, we will go over the setup and procedure of the experiment, before moving on to the software used for recording and analysis. Within this repository, you will also find the example outputs from three separate recording sessions for reference.



## Experimental Design <a name="exp_des"></a>

The idea behind the experiment is to measure and analyze the reaction of a mouse to a startle response, that being a loud, unexpected noise. In the context of ataxia 13, it is of interest whether and in what way different strains and age groups react differently to this startle. The basic version of the experiment, wherein a constant stream of white noise is suddenly overlaid with a loud noise, can be changed and adjusted in several ways, for example by introducing a quieter noise at different times before the startle to warn the mouse, or even a moment of silence where the white noise cuts out. Both have been shown to decrease the startle response.


### Setup <a name="setup"></a>

The setup consists of five parts: 
- A double-layered sound-proof box with a pressure sensor 
- A cage which holds the animal
- A box connecting the recording computer and the pressure sensor
- A computer with the recording software 
- A computer for running the analysis software (and a USB-stick for data transfer)

The sound-proof box consists of two layers, an inner one containing the pressure sensor and cage, secured by a rotating lock, and an outer one which can be fastened using two latches on the left side (be careful not to hit the emergency power switch next to the latches, you don't want to be the first to do it!). <br>
The pressure sensor inside the chamber has pins inside it that hold the cage. Be careful not to press down onto the sensor, especially when putting down the cage, otherwise it could change its calibration. <br>
In order for the sensor and the recording computer to communicate, we need a box between them. The box is below the chamber and has to be turned on before every experiment, with the switch being on the right side on the back of the device. <br>
The connected computer has the "Startle Response" program installed and is used to record and store the data. <br>
Due to the age of the recording computer, it is recommended to use a different computer for the analysis. This can be any other computer or laptop, though the more capable and up to date, the faster the analysis will be. A USB-stick will be needed to transfer the data between the two devices.


### Procedure <a name="procedure"></a>

To place the mouse into the cage for a recording, take the cage out of the chamber, grabbing it by the tray, put it down onto a desk and open the lid. To get the mouse into the cage, carefully but without too much hesitation, grab it around the upper third of its tail, lift it into the cage and close the lid. Be sure to neither grab the tail too far to the base, as this would allow the mouse to use enough muscles to turn around, or too far towards the tip, as that could hurt the animal and also make placing it into the cage more difficult. Now, put the cage with the animal back onto the sensor without pushing down on it. Close both chamber doors and secure the outer one using the two latches. <br>
Now, start a timer for ten minutes. This is the habituation period for the mouse and is crucial to ensure that it is not affected by anything that has happened before. You can obviously continue with other preparations during this period. <br>
Make sure that the box is turned on, indicated by a green light on its front. Do the same for the recording computer and open the Startle Response software, logging in without a username or password. We will go into further detail on configuring the recording software later, but assuming everything is set up, you can now begin the recording. <br>
Once it is done, open the chamber doors and remove the cage (this time being extra careful to get a good grip on the tray). Carefully move the mouse back into its container by placing the box inside and opening it, waiting for it to come out on its own. Before returning the cage to the chamber, be sure to clean the tray of any excrements left behind. <br>
You can now copy the recorded data onto a USB-stick and to the device used for analysis, which you can now begin.



## Software <a name="software"></a>

The software used consists of the recording program, a script for a preliminary cutting and analysis of the data, and another for things like significance tests and trend analysis.


### Recording <a name="recording"></a>

The recoding software, although having a login screen, does not require a password. Once logged in, there are several tabs to configure and conduct your experiments. <br>
These are the Help, Experiment, Analysis, Archive, System Test, Parameters and Exit tabs. <br>
 - Help: link to guides
 - Experiment: configure trials and experiments and start measurements
 - Analysis: select and export data
 - Archive: configure location of saved data
 - System Test: check system functions
 - Parameters: configure export parameters
 - Exit: exit the software

 The most commonly used tabs are Experiment, Analysis and Archive.

#### Experiment Tab
Here you can configure and run experiments. Under `Experiment`, you can find the setup for loading and executing an experiment file containing the trials, both of which can be configured in the `Editor`. To begin an experiment, select the right experiment file, whether or not and in what way you want the trials to be randomized, applying the randomization if applicable. Then, tick `Box 1` and input any relevant information. Note that the field `Animal No.` cannot start with a 0 like some animal numbers do, so it is recommended to use the `Group` or other fields if you wish to save the animal's full number. You may need to adjust the code accordingly depending on how you do so. <br>
The `Editor` allows you to configure the trials and the experiments they make up. The usual method is that an experiment contains one intertrial at the beginning, a short, empty trial needed for the software, and five instances of each trial. A trial, accessible via the `trial editor`, is usually 20 seconds long and begins with the command to begin recording immediately for the duration of the trial, so 20000 ms. The background noise is also started from the beginning and usually goes on for around 10 seconds before trial specific events happen, though this time too can vary.

Under `Experiment`, you can now start the recording. Select the experiment you want to run and whether or not to shuffle the trials, then tick `Box 1`, configure the animal and trial parameters accordingly and run the experiment. If everything is working, you should now see a live visualization of the recording as well as indicators for the noise and recording. If you are running a lot of trials at once, it may be advisable to roughly calculate how much time everything will take (usually 20 seconds per trial) and set a timer accordingly. Besides ensuring that both the sound and recording is running, you do not necessarily need to be present for the duration of the experiment. For example, with 19 different trials with 5 repetitions at 20 seconds each, this would take roughly half an hour, or 40 minutes including the 10 minute habituation period.

#### Analysis Tab
The analysis tab is where you select and export your data. `Data Selection` shows all recorded data in the top field, by default sorted in the order it was recorded in. Either double-clicking on one of the lines or using the `ALL` or `Filter` options copies a recording into the bottom field. When exporting data, only these recordings will be exported. <br>
`Export Analog Data` exports the files in the way specified in `Parameters -> Export Parameters`. By default, this should be the CSV files we need for the analysis. Should you also wish to save Excel files, you can change the export parameters accordingly. Although more pleasant to look at, these are substantially slower to process and are thus not used for analysis.


#### Archive Tab
`Data Directory` defines the directory all recording data is saved to, while the `Reindexing` option allows you to update the `Data Selection` whenever you change directory. The `Data Selection` window also has this option.



### Analysis <a name="analysis"></a>

In order to familiarize yourself with the analysis software, it would be best to go through both notebooks once to know what outputs to expect. <br>
To now use your own data, you first have to set up the input folder. Create a new folder in the same one as the notebooks, for example named after the year of the recording, the operator, etc. Inside this folder, create new folders, one for each animal, and name them accordingly. Within these folders, place all CSV files that contain recordings from the respective animal. The animal folder and CSV file names will be used internally to label slices, but are otherwise not important for anything other than debugging . Lastly, in the "Peakfinder" notebook, change the variable `input_dir` of the second codeblock to the name you gave to the folder containing the animal folders. <br>
There are two different notebooks used for analysis, the first one, "Peakfinder", taking the raw data and turning it into excel files containing the reaction time, the time until the peak, the difference between the former two and the strength of the peak, all averaged across the different experiments. The second notebook, "Analyzer", takes these files and runs several tests on them, examining changes across animals and experiments. Especially the latter can and should be edited by you to fit your specific needs. <br>
However, one thing you may need to adjust in the Peakfinder notebook is the `startle_time` library, wherein you need to insert the experiment names and times at which the startle sound is played. Should there be multiple in one trial, insert them as a list. The variable `startle_offset` defines the size of the examined window, making the program save this many milliseconds of the recording before and after the startle. Depending on what you are examining, you might also need to adjust the code to save things like the strain and age of the animal into the output files. <!-- we could do that and just disable it by default --><br>
Other settings you may want to adjust are `output_dir`, which defines where you want the output files to go, `verbose`, which when set to `False` mutes all output except for error messages, and `excel_output`, which when `False` makes the program output CSV files instead of excel files. CSV files are faster to read by other programs, however they are less readable to humans due to their lack of neat looking columns and rows. However, due to the low amount of data in the output files, this should not make a noticeable difference. <br>
Further details on the code are included in the notebooks markdown sections and comments. 



## Troubleshooting <a name="troubleshooting"></a>


### Oh my god it escaped!
Don't panic. The mouse may be faster and more agile than you, but (hopefully) it is not smarter. Stay calm, and attempt to scoop it up again as done before. It will likely move towards something it perceives as cover - a pile of cables, a dark corner, a bag or jacket, etc. Simply check all of these spots until you find it, and avoid loud noises or rash movements to not scare it further.


### Recording Software Error
Call customer support.


### Analysis Software Error
Usually, any error the notebooks put out is well documented. Check if the files look ok, whether or not the startle times are set correctly, and if in doubt, look up the error code. If the code block handling the creation of the library which will be turned into the output files says that it encountered strange peaks, examine the respective recording, either directly in the raw file or by creating a new code block to plot or print out the segment. If the peak really is too early, late or non-existent, proceed as is fit for your use case. If you are sure that something is wrong with the code or need help understanding a part of it, feel free to reach out to me directly or via another group member. If you happen to have a fix for it and know your way around GitHub, you could even submit a pull request for it.