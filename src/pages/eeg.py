import numpy as np
import matplotlib as mt
import mne
import os

from trydjango.settings import BASE_DIR


def magic(filename):

    temp_raw_name = filename + "_raw.png"
    temp_name = filename + ".png"

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    filename = os.path.join(MEDIA_ROOT, filename)
    raw = mne.io.read_raw_egi(filename)
    mne.channels.make_standard_montage("GSN-HydroCel-256")

    raw.info['bads'] += ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10', 'E11', 'E12', 'E13', 'E14', 'E15',
                         'E16', 'E17', 'E18', 'E19', 'E20', 'E21', 'E22', 'E23', 'E24', 'E25', 'E26', 'E27', 'E28',
                         'E29',
                         'E30',
                         'E31', 'E32', 'E33', 'E34', 'E35', 'E36', 'E37', 'E38', 'E39', 'E40', 'E41', 'E42', 'E43',
                         'E44',
                         'E45',
                         'E46', 'E47', 'E48', 'E49', 'E50', 'E51', 'E52', 'E53', 'E54', 'E55', 'E56', 'E57', 'E58',
                         'E59',
                         'E60',
                         'E61', 'E62', 'E63', 'E64', 'E65', 'E66', 'E67', 'E68', 'E69', 'E70', 'E71', 'E72', 'E73',
                         'E74',
                         'E75',
                         'E76', 'E77', 'E78', 'E79', 'E80', 'E81', 'E82', 'E83', 'E84', 'E85', 'E86', 'E87', 'E88',
                         'E89',
                         'E90',
                         'E91', 'E92', 'E93', 'E94', 'E95', 'E96', 'E97', 'E102', 'E103', 'E104', 'E105',
                         'E106', 'E107', 'E111', 'E112', 'E113', 'E114', 'E115',
                         'E120', 'E121', 'E122', 'E123', 'E130', 'E131', 'E132', 'E133',
                         'E134', 'E135', 'E136', 'E142', 'E143', 'E144', 'E145', 'E146', 'E147',
                         'E148', 'E153', 'E154', 'E155', 'E156', 'E157', 'E158', 'E159', 'E160', 'E161',
                         'E162', 'E163', 'E164', 'E165', 'E166', 'E167', 'E168', 'E169', 'E170', 'E171', 'E172', 'E173',
                         'E174', 'E175',
                         'E176', 'E177', 'E178', 'E179', 'E180', 'E181', 'E182', 'E183', 'E184', 'E185', 'E186', 'E187',
                         'E188', 'E189',
                         'E190', 'E191', 'E192', 'E193', 'E194', 'E195', 'E196', 'E197', 'E198', 'E199', 'E200', 'E201',
                         'E202', 'E203',
                         'E204', 'E205', 'E206', 'E207', 'E208', 'E209', 'E210', 'E211', 'E212', 'E213', 'E214', 'E215',
                         'E216', 'E217',
                         'E218', 'E219', 'E220', 'E221', 'E222', 'E223', 'E224', 'E225', 'E226', 'E227', 'E228', 'E229',
                         'E230', 'E231',
                         'E232', 'E233', 'E234', 'E235', 'E236', 'E237', 'E238', 'E239', 'E240', 'E241', 'E242', 'E243',
                         'E244', 'E245',
                         'E246', 'E247', 'E248', 'E249', 'E250', 'E251', 'E252', 'E253', 'E254', 'E255', 'E256', 'E257']
    fmin, fmax = 2, 100  # look at frequencies between 2 and 100Hz
    n_fft = 2048  # the FFT size (n_fft). Ideally a power of 2

    raw.plot_psd(area_mode='range', tmax=10.0, show=False, average=True).savefig(os.path.join(MEDIA_ROOT, temp_raw_name))

    raw.load_data()

    raw_highpass = raw.copy().filter(l_freq=0.1, h_freq=None)
    raw_highpass.filter(None, 30., fir_design='firwin')

    raw_highpass.plot_psd(area_mode='range', tmin=100, tmax=500.0, show=False, average=True).savefig(os.path.join(MEDIA_ROOT, temp_name))

    return [os.path.join('media', temp_name), os.path.join('media', temp_raw_name)]
