
stages = [
    # ["non rem", "nrem", "non rapid eye movement"],
    ["stage 1 sleep", "stage one sleep", "light sleep"],
    ["stage 2 sleep", "stage two sleep"],
    ["stage 3 sleep", "stage three sleep"],
    ["stage 4 sleep", "stage four sleep"],
    ["rem", "rapid eye movement", "paradoxical sleep"]
]

# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8198610/#:~:text=Statistical%20features%20like%20mean%2C%20median,analysis%20of%20the%20EEG%20signals.
eeg_features = [
    "spindle",

    "time-domain",
    "skewness",
    "kurtosis"
    "zero crossing rate", 'ZCR',
    "number of waves",
    "wave duration",
    "peak amplitude",
    "instantaneous frequency",
    "hjorth",
    "mobility",
    "activity",
    "complexity",
    "k-complex",
    "energy",

    "frequency-domain",
    "delta",
    "theta",
    "alpha",
    "beta",
    "gamma",
    "sigma",
    "reflection coefficient",
    "partial correlation coefficient"
    "wavelet coefficient",
    "phase coupling",
    
    "hurst exponent",
    "renyi scaling exponent",
    "renyi geneneralized dimension multifractal",
    "capacity dimension",
    "information dimension",
    "correlation dimension",
    "Katz fractal",
    "Petrosian fractal",
    "Higuchi fractal",
    "fractal spectrum",
    "lyapunov exponent",
    "lempel-ziv complexity",
    "central tendency measure",
    "auto-mutual information",
    "temporal irreversibility",
    "recurrence rate",
    "determinism",
    "laminarity",
    "average diagonal line length",
    "maximum length of diagonal",
    "Maximum length of vertical lines",
    "trapping time",
    "Divergence",

    "Entropy",
    "Shannon entropy",
    "renyi entropy",
    "Tsallis entropy",
    "Kraskov entropy",
    "Spectral entropy",
    "Quadratic Renyi",
    "response entropy",
    "state entropy",
    "wavelet",
    "tsallis wavelet entropy",
    "renyi wavelet entropy",
    "hilbert-huang",
    "log energy",
    "multiresolution",
    "Kolmogorov",
    "nonlinear forecasting",
    "maximum-likelihood entropy",
    "coarse-grained",
    "correntropy", "CoE",
    "approximate entropy",
    "sample entropy",
    "quadratic sample",
    "multiscale entropy",
    "Composite multiscale entropy",
    "Permutation entropy",
    "renyi's permutation",
    "permutation renyi",
    "multivariate PE",
    "tsallis permutation",
    "dispersion entropy",
    "amplitude-aware PE",
    "bubble entropy",
    "differential entropy",
    "fuzzy entropy",
    "transfer entropy",

    "undirected spatiotemporal",
    "coherence",
    "partial coherence",
    "phase coherence",
    "phase-locking value",
    "coherency",
    "imaginary compenent of Coh",
    "phase-lag index",
    "wieghted phase lag index",
    "debiased weighted PLI",
    "pairwise phsae consistency",
    "generalized synchronization",
    "synchronization likelihood",
    "mutual information",
    "cross-RQA",
    "correlation length",

    "directed spatiotemporal",
    "granger causality",
    "spectral granger",
    "phase slope index",

    "complex networks",
    "number of vertices",
    "number of edges",
    "degree distribution",
    "degree correlation",
    "clustering coefficient",
    "transitivity",
    "motif",
    "characteristric path length",
    "small worldness",
    "assortativity",
    "local efficiency",
    "global efficiency",
    "modularity",
    "centrality degree",
    "closeness centrality",
    "eigenvalue centrality",
    "betweenness centraility",
    "diameter",
    "eccentricity",
    "hubs",
    "rich club",
    "leaf fraction",
    "hierarchy"
]

# https://bycycle-tools.github.io/bycycle/glossary.html
bycycle_features = {
    "Period": "period",
    "Peak": "time_peak",
    "Trough": "time_trough",
    "Rise": "time_rise",
    "Decay": "time_decay",
    "Rise-decay symmetry": "time_rdsym",
    "Peak-trough symmetry": "time_ptsym",
    "Sinusoidality": "",
    "Voltage Peak": "volt_peak",
    "Voltage Trough": "volt_trough",
    "Voltage Rise": "volt_rise",
    "Voltage Decay": "volt_decay",
    "Voltage Amplitude": "volt_amp",
    "Band Amplitude": "band_amp",

    "Amplitude Fraction": "amp_frac",
    "Amplitude Consistency": "amp_consistency",
    "Period Consistency": "period_consistency",
    "Monotonicity": "monotonicity",
    "Burst Fraction": "burst_fraction",

    "Sample Peak": "sample_peak",
    "Sample Last Trough": "smaple_last_trough",
    "Sample Next Trough": "sample_next_trough",
    "Sample Rise": "sample_zerox_rise",
    "Sample Decay": "sample_zerox_decay"
}