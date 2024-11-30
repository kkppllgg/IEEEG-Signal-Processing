from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

from scipy.signal import butter, filtfilt


def low_pass_filter(signals, sampling_frequency = 250, cutoff_frequency = 4, order=4):

    average_signal = np.mean(signals,axis=0)
    # Normalize the cutoff frequency (cutoff / Nyquist frequency)
    nyquist_frequency = 0.5 * sampling_frequency
    normalized_cutoff = cutoff_frequency / nyquist_frequency

    
    b, a = butter(order, normalized_cutoff, btype='low', analog=False)

   
    filtered_signal = filtfilt(b, a, average_signal)


    
    plot_trial(filtered_signal)

def spectogram_trial_average(trials):
    trial = np.mean(trials,axis = 0)
    trial = trial*np.hamming(trial.size)
    # Normalize the audio data to the range [-1, 1]
    trial = trial / np.max(np.abs(trial), axis=0)

    nperseg = int(datasetA1.Fs* 1) 

   
    f, t, Sxx = signal.spectrogram(trial, fs = datasetA1.Fs,nperseg=nperseg,window=np.hanning(nperseg))

    
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(t, f, np.log(Sxx), shading='gouraud') 
    plt.ylabel('Frequency [Hz]')
    plt.ylim((0,20))
    plt.xlabel('Time [sec]')
    plt.title('Spectrogram of the EEG Signal')
    
def spectogram_trial(trial):
    trial = trial*np.hamming(trial.size)
    # Normalize the audio data to the range [-1, 1]
    trial = trial / np.max(np.abs(trial), axis=0)

    nperseg = int(datasetA1.Fs* 1) 

   
    f, t, Sxx = signal.spectrogram(trial, fs = datasetA1.Fs,nperseg=nperseg,window=np.hanning(nperseg))

    
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(t, f, np.log(Sxx), shading='gouraud') 
    plt.ylabel('Frequency [Hz]')
    plt.ylim((0,20))
    plt.xlabel('Time [sec]')
    plt.title('Spectrogram of the EEG Signal')
    
   


def plot_trial(trial):
    trial_idxs = []
    ct = 0
    for i in trial:
        trial_idxs.append(ct)
        ct = ct + 1

    plt.ylabel("Voltage [μV]")
    plt.xlabel("Time [s]")
    plt.xscale
    plt.plot(np.array(trial_idxs)/datasetA1.Fs,trial)
    plt.show()

class MotorImageryDataset:
    def __init__(self, dataset='workshop/eeg/A01T.npz'):
        if not dataset.endswith('.npz'):
            dataset += '.npz'

        self.data = np.load(dataset)

        self.Fs = 250 # 250Hz from original paper

       

        self.raw = self.data['s'].T
        self.events_type = self.data['etyp'].T
        self.events_position = self.data['epos'].T
        self.events_duration = self.data['edur'].T
        self.artifacts = self.data['artifacts'].T

        # Types of motor imagery
        self.mi_types = {769: 'left', 770: 'right', 771: 'foot', 772: 'tongue', 783: 'unknown'}

    def get_trials_from_channel(self, channel=7):

        # Channel default is C3 

        startrial_code = 768
        starttrial_events = self.events_type == startrial_code
        idxs = [i for i, x in enumerate(starttrial_events[0]) if x]

        trials = []
        classes = []
        for index in idxs:
            try:
               
                type_e = self.events_type[0, index+1]
                if(self.mi_types[type_e] == 'right' ):
                    class_e = self.mi_types[type_e]
                    classes.append(class_e)

                    start = self.events_position[0, index]
                    stop = start + self.events_duration[0, index]
                    trial = self.raw[channel, start:stop]
                    trials.append(trial)

            except:
                continue

        return trials, classes

datasetA1 = MotorImageryDataset()
trials, classes = datasetA1.get_trials_from_channel()
# trials contains the N valid trials, and clases its related class.

print(classes)

#plot_trial(trials[0])
#spectogram_trial(trials[20])
low_pass_filter(trials)
#spectogram_trial_average(trials)
print("calculating for channel")


plt.show()