import librosa
import numpy as np
import scipy
import wave
import os
import sys
import time 
import IPython.display as ipd 
import matplotlib.pyplot as plt
import soundfile as sf 


def get_wav_fromfile_librosa(filepath, sr=22050, hop_length=256,  pad_nums=4, mono=True, dur=None, DEBUG=False):
    wav, sr, nsamples, dur  = load_wav_librosa(filepath ,sr=sr, mono=True, dur = dur, DEBUG=DEBUG ) # max 15 sec to save load time 
    wav_adj  = adjust_wav_librosa(wav, hop_length=hop_length, DEBUG=DEBUG) # fix  hop_size
    wav_norm = norm_wav_librosa(wav, ratio=0.94, DEBUG=DEBUG)  # normalize and 0.94 
    return wav_norm        


def load_wav_librosa(filepath, sr=22050, mono=True, dur=None, DEBUG=False):
    import librosa
    import numpy 
    import time 
    tic = time.time()
    wav, sr = librosa.core.load(filepath,  sr=sr, mono=mono, res_type='polyphase')
    if (dur == None):
        wav_final   = wav
    else:
        wav_final   = wav[0: int(dur*sr) ]
    n_samples = len(wav_final)
    wav_final = wav_final.astype("float32")
    toc = time.time()
    dur = toc-tic
    if DEBUG :
        print( "DEBUG : {:>6.3f} ms load_wav               : sr{} {:>6.2f} sec audio with {} samples  "
        .format(dur*1000, sr,  len(wav)/sr, n_samples  )  )    
    return wav_final, sr, n_samples, len(wav)/sr

def adjust_wav_librosa(wav,  sr=22050, hop_length = 256, DEBUG=False ):
    import librosa 
    import time
    tic = time.time()    
    #stft/istft truncate  n * hop + remains --> h* hop 
    frames_org = len(wav)/hop_length
    n_frames = int(len(wav) / hop_length  ) + 1 
    samples = int( len(wav)/hop_length)*hop_length
    wav_adj = wav[:samples] 
    frames_adj = len(wav_adj)/hop_length
    toc = time.time()
    dur = toc - tic
    if DEBUG :
        print( "DEBUG : {:>6.3f} ms adjust_wav             : sr{} {:>6.2f} sec audio with {} samples {:>8.1f}frames -->  {} samples {:>8.1f} frames ".
              format(dur*1000, sr,  len(wav)/sr, len(wav), frames_org, len(wav_adj), frames_adj  )  )
    return wav_adj 

def enpad_wav_librosa(wav, hop_length = 256, pad_nums=0 , DEBUG=False ):
    import librosa 
    import time
    tic = time.time()    
    wav_expand = librosa.util.pad_center(wav,   len(wav) + int(2*pad_nums * hop_length), mode='constant')
    toc = time.time()
    dur = toc-tic     
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms enpad_wav              : {} -- {} +{}--> {}  {} "
        .format( dur, len(wav), hop_length, pad_nums, len(wav_expand), len(wav_expand)- len(wav)) )    
    return wav_expand


def depad_wav_librosa(wav, sr=22050, hop_length = 256, pad_nums=0, DEBUG=False ):
    import time
    tic = time.time()        
    front_pad =     pad_nums * hop_length 
    back_pad  =     pad_nums * hop_length 
    all_pad   = 2 * pad_nums * hop_length 
    wav_trim  = wav[front_pad: len(wav)- back_pad ] 
    toc = time.time()
    dur = toc-tic        
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms depad_wav              : {} -- {} -{}--> {}  {} "
        .format( dur, len(wav), hop_size, pad_nums, len(wav_trim), len(wav_trim)- len(wav)) )    
    return wav_trim  

def norm_wav_librosa(wav, sr=22050, ratio=0.94 , DEBUG=False):
    import librosa
    import time
    tic = time.time()
    wav_norm = librosa.util.normalize(wav) * ratio   
    toc = time.time()
    dur = toc-tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms norm_wav               : sr{} {:>6.2f} sec audio with {} samples with {}"
        .format(dur * 1000 , sr,  len(wav)/sr, len(wav_norm), ratio )  )   

    return wav_norm    


def save_wav_librosa(filepath, wav, sr=22050, subtype='PCM_16', DEBUG=False):
    import soundfile as sf
    import time
    tic = time.time()
    sf.write(filepath, wav, sr, subtype=subtype)
    toc = time.time()
    dur = toc - tic
    if DEBUG :
        print( "DEBUG : {:>6.3f} ms save_wav               : sr{} {:>6.2f} sec audio with {} samples format {} "
        .format(dur*1000, sr,  len(wav)/sr, len(wav) , subtype )  )



def resample_wav_librosa(wav, org_sr, tgt_sr, res_type = 'polyphase' , DEBUG=False ): #########TODEO
    import librosa 
    import time
    tic = time.time()
    wav_resample = librosa.resample(wav, orig_sr=org_sr, target_sr = tgt_sr, res_type=res_type) 
    toc = time.time()
    dur = toc - tic
    if DEBUG :
        print( "DEBUG : {:>6.3f} ms resample_wav           : sr{} {:>6.2f} sec audio with {} samples --{}--> sr{} {:>6.2f} sec audio with {} samples".
              format(dur*1000, org_sr,  len(wav)/org_sr , len(wav),   res_type, tgt_sr, len(wav_resample)/tgt_sr ,len(wav_resample)) )
    return wav_resample

def get_spec_stft_librosa(audio,sr=22050, n_fft=1024, hop_length=256, win_type='hann', center=False, DEBUG=False  ):
    import librosa 
    import time 
    tic = time.time()
    spectrogram = librosa.stft(audio, n_fft=n_fft, hop_length=hop_length, window=win_type, center=center )
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_spec_stft          : sr{} {:>6.2f} sec audio with {} samples   --> nfft{} hop{} win '{}' --> {}  "
        .format( dur*1000, sr, len(audio)/sr, len(audio), n_fft, hop_length, win_type, spectrogram.shape  ) )    
    return spectrogram


def get_spec_stft_inv_librosa(spectrogram, sr=22050, n_fft=1024, hop_length=256, win_type='hann', center=False, DEBUG=False  ):
    import librosa 
    import time 
    tic = time.time()
    audio= librosa.istft(spectrogram, hop_length=hop_length, window=win_type, center=center )
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_spec_stft_inv      : {}  -->  nfft{} hop{} win '{}'   --> sr {}  {:>6.2f} sec audio with {} samples   "
        .format( dur*1000, spectrogram.shape , n_fft, hop_length, win_type, sr, len(audio)/sr, len(audio),    ) )    
    return audio    

def get_magangle_librosa(spectrogram, DEBUG=False ):
    import numpy as np 
    import librosa 
    import time 
    tic = time.time()    
    magnitude   = np.abs(spectrogram)
    angle       = np.angle(spectrogram)
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_magangle           : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )             
    return magnitude, angle


def get_magangle_inv_librosa(magnitude, angle,  DEBUG=False ):
    import numpy as np 
    import librosa 
    import time 
    tic = time.time()    
    spectrogram = magnitude   * np.exp( 1j* angle) 
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_magangle_inv       : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )             
    return spectrogram


def get_magphase_librosa(spectrogram, DEBUG=False ):
    import numpy as np 
    import librosa 
    import time 
    tic = time.time()    
    magnitude   = np.abs(spectrogram)
    phase       = np.exp(1.j* np.angle(spectrogram) )
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_magphase           : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )                   
    return magnitude, phase

def get_magphase_inv_librosa(magnitude, phase, DEBUG=False ):
    import numpy as np 
    import librosa 
    import time 
    tic = time.time()    

    spectrogram       = magnitude* phase
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_magphase_inv       : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )                   
    return spectrogram


def get_abssign_librosa(spectrogram, DEBUG=False ):
    import numpy as np 
    import librosa 
    import time 
    tic = time.time()    
    magnitude   = np.abs(spectrogram)
    signvalue   = np.sign(spectrogram)
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_magsign            : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )               
    return magnitude, signvalue


def get_abssign_inv_librosa(magnitude, signvalue, DEBUG=False ):
    import numpy as np 
    import librosa 
    import time 
    tic = time.time()    
    spectrogram   = magnitude * signvalue
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_abssign_inv        : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )               
    return spectrogram

def get_zeroclip_librosa(input, a_min=0, a_max=99999, DEBUG=False):
    import numpy as np
    import time
    tic = time.time()    
    clip_val = np.clip(input, a_min=a_min, a_max=a_max)
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_zeroclip               : {} "
        .format( dur*1000,  clip_val.shape  ) )        
    return clip_val

def get_window_librosa(win_length=512, win_type = 'hanning'  ):
    from scipy import signal 
    import numpy as np     
 
    if win_type=='hanning' :
        window = np.hanning
        win = window(win_length)
    elif win_type=='boxcar':
        window = signal.boxcar        
        win = window(win_length)
    else :
        window = np.hanning
        win = window(win_length)        

    return np.asarray(win) 




def get_lin2mel_librosa(mag , mel_basis=None, sr=22050, n_fft=1024, n_mels=80, fmin=0, fmax=None, DEBUG=False ):
    import numpy as np 
    import librosa 
    import time
    tic = time.time()

    mel = np.dot(mel_basis,mag)
    toc = time.time()
    dur = toc-tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_lin2mel          : {}  to {} "
        .format(dur * 1000, mag.shape , mel.shape  )          )   
    return mel

def get_mel2lin_librosa(mel , mel_basis_T=None, sr=22050, n_fft=1024, n_mels=80, fmin=0, fmax=None, DEBUG=False):
    import numpy as np 
    import librosa
    import time
    tic = time.time() 
    mag = np.dot(mel_basis_T,mel)
    toc = time.time()
    dur = toc-tic
    if DEBUG :      
        print("DEBUG : {:>6.3f} ms get_mel2lin          : {}  to {} "
        .format(dur * 1000, mel.shape , mag.shape  )          )   
    return mag

def get_mel_basis_half_librosa(sr=22050, n_fft=1024, n_mels=80, fmin=0, fmax=None, DEBUG=False ):
    import librosa
    import time
    tic = time.time()
    mel_basis = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels, fmin=fmin, fmax=fmax)
    toc = time.time()
    dur = toc-tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_mel_basis        : {}   "
        .format(dur * 1000, mel_basis.shape )          )   
    return mel_basis

def get_mel_basis_full_librosa(sr=22050, n_fft=1024, n_mels=80, fmin=0, fmax=None, norm=1, DEBUG=False):
    import time 
    import librosa
    import numpy as np 
    tic = time.time()
    #two_side float
    if fmax is None:
        fmax = int(float(sr) /2)   #  
    if norm is not None and norm != 1 and norm != np.inf:
        raise ParameterError('Unsupported norm: {}'.format(repr(norm)))              
    n_mels   = int(n_mels)
    weights  = np.zeros( (n_mels, int(n_fft+1)) , dtype=float)  
    fftfreqs = librosa.fft_frequencies(sr=sr, n_fft=n_fft*2)  # bug fixed 2021. 11.1   librosa.fft_frequencies(sr=sr, n_fft=n_fft*2)*2 was bug
    mel_f    = librosa.mel_frequencies(n_mels + 2, fmin=fmin, fmax=fmax)
    fdiff = np.diff(mel_f) 
    ramps = np.subtract.outer(mel_f, fftfreqs)   
    for i in range(n_mels):
        lower = -ramps[i] / fdiff[i]
        upper = ramps[i+2] / fdiff[i+1]        
        weights[i] = np.maximum(0, np.minimum(lower, upper))
    if norm == 1:
        # Slaney-style mel is scaled to be approx constant energy per channel
        enorm = 2.0 / (mel_f[2:n_mels+2] - mel_f[:n_mels])
        weights *= enorm[:, np.newaxis]

    weights = np.delete(weights,int(n_fft),1) 
    toc = time.time()
    dur = toc-tic
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_mel_basis        : {}   "
        .format(dur * 1000, weights.shape )          )   

    return weights

def get_drc_librosa(spectrogram, C=1, clip_val=1e-5, DEBUG=False):
    import numpy as np
    import time
    tic = time.time()
    spectrogram_drc = np.log(np.clip(spectrogram, a_min=clip_val, a_max=None)* C )
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_drc                : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )    

    return spectrogram_drc

def get_drc_inv_librosa(spectrogram, C=1, DEBUG=False):
    import numpy as np
    import time
    tic = time.time()
    spectrogram_drd = np.exp(spectrogram) / C 
    toc = time.time()
    dur = toc - tic 
    if DEBUG : 
        print("DEBUG : {:>6.3f} ms get_drc_inv            : {} bin x {} frames   "
        .format( dur*1000,  spectrogram.shape[0], spectrogram.shape[1]  ) )    

    return spectrogram_drd


def get_spec_strft_librosa(wav, sr=22050, n_fft=1024,  win_length=None, hop_length=256, win_type='kaiser' , center=False, DEBUG=False):
    # scipy strft with scipy packed rfft
    import time 
    from scipy.fftpack import rfft as rfft  # good quality rfft, irfft
    import numpy as np 
    import librosa
    
    if win_length == None :
        win_length = n_fft        

    tic = time.time()
    if len(wav)%hop_length ==0 :     
        wav = librosa.util.fix_length( wav, len(wav) + hop_length) # match with librosa(center=False) #################### final ###################
    
    
    window = get_window(win_length=win_length, win_type = win_type) #get_window(win_length=win_length+1, win_type = win_type)[:-1] 
    spectrogram = np.array([ rfft(window*wav[i:i+win_length]  )
                     for i in range(0, len(wav)-win_length, hop_length)])
    spectrogram=spectrogram.T
    toc = time.time()
    dur = toc-tic
    if DEBUG :      
        print("DEBUG : {:>6.3f} ms get_spec_strft         : sr{} {:>6.2f} sec audio with {} samples -->   nfft{} hop{} win '{}' --> {}  "
        .format( dur*1000, sr, len(wav)/sr, len(wav), n_fft, hop_length, win_type, spectrogram.shape  ) )

    return spectrogram


def get_spec_strft_inv_librosa(D, sr=22050, n_fft=1024,  win_length=None, hop_length=256, win_type='kaiser' , center=False, DEBUG=False ):    
    import time 
    import numpy as np 
    from scipy.fftpack import irfft as irfft    
    
    if win_length == None :
        win_length = n_fft    
    D = D.T

    tic = time.time()    
    window = get_window(win_length=win_length, win_type = win_type)#[:-1]
    time_slices = D.shape[0] #   match with librosa(center=False) #################### final ################### 

    len_samples = int(time_slices*hop_length + win_length)
    wav_tmp = np.zeros(len_samples)
    wsum = np.zeros(len_samples)
    for n,i in enumerate(range(0, len(wav_tmp)-win_length, hop_length)): # for n,i in enumerate(range(0, len(wav_tmp)-win_length, hop_length)):
        wav_tmp[i:i+win_length] += window* irfft(D[n]  ).real 
        wsum[i:i+win_length] += window ** 2.
    pos = wsum != 0
    wav_tmp[pos] /= wsum[pos]   
    toc = time.time()
    dur = toc - tic     
    wav_tmp = wav_tmp.astype("float32")
    wav_tmp=wav_tmp[:len_samples-hop_length]  # match with librosa(center=False) #################### final ###################
    if DEBUG :      
        print("DEBUG : {:>6.3f} ms get_spec_strft_inv     : {}  --> nfft{} hop{} win '{}'  -->  sr {} {:>6.2f} sec audio with {} samples   "
        .format( dur*1000,  D.T.shape , n_fft, hop_length, win_type, sr, len(wav_tmp)/sr, len(wav_tmp),) )          
    return wav_tmp

def get_spec_stdct_librosa(wav, sr=22050, n_fft=1024,  win_length=None, hop_length=256, win_type='kaiser' , center=False, DEBUG=False):
    # scipy strft with scipy packed rfft    
    import time 
    #from scipy.fftpack import rfft as rfft  # good quality rfft, irfft
    from scipy.fftpack import dct as dct
    import numpy as np 
    import librosa
    
    if win_length == None :
        win_length = n_fft        

    tic = time.time()
    if len(wav)%hop_length ==0 :     
        wav = librosa.util.fix_length( wav, len(wav) + hop_length) # match with librosa(center=False) #################### final ###################
    
    
    window = get_window(win_length=win_length, win_type = win_type) #get_window(win_length=win_length+1, win_type = win_type)[:-1] 
    spectrogram = np.array([ dct(window*wav[i:i+win_length],  type=2, norm='ortho'   ) #  type=2, norm='ortho'
                     for i in range(0, len(wav)-win_length, hop_length)])
    spectrogram=spectrogram.T
    toc = time.time()
    dur = toc-tic
    if DEBUG :      
        print("DEBUG : {:>6.3f} ms get_spec_stdct         : sr{} {:>6.2f} sec audio with {} samples -->   nfft{} hop{} win '{}' --> {}  "
        .format( dur*1000, sr, len(wav)/sr, len(wav), n_fft, hop_length, win_type, spectrogram.shape  ) )

    return spectrogram


def get_spec_stdct_inv_librosa(D, sr=22050, n_fft=1024,  win_length=None, hop_length=256, win_type='kaiser' , center=False, DEBUG=False ):    
    import time 
    import numpy as np 
    #from scipy.fftpack import irfft as irfft   
    from scipy.fftpack import idct as idct 
    
    if win_length == None :
        win_length = n_fft    
    D = D.T

    tic = time.time()    
    window = get_window(win_length=win_length, win_type = win_type)#[:-1]
    time_slices = D.shape[0] #   match with librosa(center=False) #################### final ################### 

    len_samples = int(time_slices*hop_length + win_length)
    wav_tmp = np.zeros(len_samples)
    wsum = np.zeros(len_samples)
    for n,i in enumerate(range(0, len(wav_tmp)-win_length, hop_length)): # for n,i in enumerate(range(0, len(wav_tmp)-win_length, hop_length)):
        wav_tmp[i:i+win_length] += window* idct(D[n],  type=2, norm='ortho'   ) 
        wsum[i:i+win_length] += window ** 2.
    pos = wsum != 0
    wav_tmp[pos] /= wsum[pos]   
    toc = time.time()
    dur = toc - tic     
    wav_tmp = wav_tmp.astype("float32")
    wav_tmp=wav_tmp[:len_samples-hop_length]  # match with librosa(center=False) #################### final ###################
    if DEBUG :      
        print("DEBUG : {:>6.3f} ms get_spec_stdct_inv     : {}  -->  nfft{} hop{} win '{}' -->  sr {} {:>6.2f} sec audio with {} samples   "
        .format( dur*1000,  D.T.shape , n_fft, hop_length, win_type, sr, len(wav_tmp)/sr, len(wav_tmp),) )          
    return wav_tmp
