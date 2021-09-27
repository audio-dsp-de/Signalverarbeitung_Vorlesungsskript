import matplotlib
import numpy
from matplotlib import pyplot

matplotlib.style.use('sv1_style.mplstyle')

rect_window = numpy.concatenate([[0]+[1]*30+[0]])
rect_window = numpy.concatenate([rect_window, [0]*1000])

spectrum = numpy.fft.fft(rect_window)
mid = numpy.floor(len(spectrum)/2)
spectrum = numpy.concatenate([spectrum[int(mid):], spectrum[:int(mid)]])
spectrum_abs = 20*numpy.log10(numpy.abs(spectrum)/numpy.abs(spectrum).max())
freqs_fft = numpy.linspace(-1, 1, len(spectrum_abs))

fig, (ax_sample, ax_spectrum) = pyplot.subplots(1, 2)
ax_sample.plot(rect_window)
ax_sample.set(xlabel='Folgenndex k ->', ylabel='Amplitude x[k]', xlim=[0, 31], title='Rechteck-Fenster im Frequenzbereich')

ax_spectrum.plot(freqs_fft, spectrum_abs)
ax_spectrum.set(xlabel='Frequenz rad/pi ', ylabel='Dämpfung in dB', title='Rechteck-Fenster im Frequenzbereich')

pyplot.show()

