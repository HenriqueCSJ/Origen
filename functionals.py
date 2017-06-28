dens_functionals = {
    "Local and gradient corrected functionals": {
        "HFS": "Hartree{Fock{Slater Exchange only functional",
        "LDA or LSD": "Local density approximation (defaults to VWN5)",
        "VWN": "Vosko{Wilk{Nusair local density approx. parameter set 'V'",
        "VWN5": "Vosko{Wilk{Nusair local density approx. parameter set 'V'",
        "VWN3": "Vosko{Wilk{Nusair local density approx. parameter set 'III'",
        "PWLDA": "Perdew-Wang parameterization of LDA",
        "BP86 or BP": "Becke '88 exchange and Perdew '86 correlation",
        "BLYP": "Becke '88 exchange and Lee - Yang - Parr correlation",
        "OLYP": "Handy's 'optimal' exchange and Lee-Yang-Parrcorrelation",
        "GLYP": "Gill's '96 exchange and Lee-Yang-Parr correlation",
        "XLYP": "The Xu and Goddard exchange and Lee-Yang-Parr correlation",
        "PW91": "Perdew-Wang '91 GGA functional",
        "mPWPW": "Modified PW exchange and PW correlation",
        "mPWLYP": "Modified PW exchange and LYP correlation",
        "PBE": "Perdew-Burke-Erzerho GGA functional",
        "RPBE": "'Modified' PBE",
        "REVPBE": "'Revised' PBE",
        "PWP": "Perdew-Wang '91 exchange and Perdew '86 correlation"},

    "Hybrid functionals": {
        "B1LYP": "The one - parameter hybrid functional with Becke '88 "
        "exchange and Lee - Yang - Parr correlation(25 % HF exchange)",
        "B3LYP and B3LYP/G": "The popular B3LYP functional (20% HF exchange) "
        "as defined in the TurboMole program system and the Gaussian program "
        "system, respectively",
        "O3LYP": "The Handy hybrid functional",
        "X3LYP": "The Xu and Goddard hybrid functional",
        "B1P": "The one-parameter hybrid version of BP86",
        "B3P": "The three-parameter hybrid version of BP86",
        "B3PW": "The three-parameter hybrid version of PW91",
        "PW1PW": "One-parameter hybrid version of PW91",
        "mPW1PW": "One-parameter hybrid version of mPWPW",
        "mPW1LYP": "One-parameter hybrid version of mPWLYP",
        "PBE0": "One-parameter hybrid version of PBE",
        "PW6B95": "Hybrid functional by Truhlar",
        "BHANDHLYP": "Half-and-half hybrid functional by Becke"},

    "Meta-GGA and hybrid meta-GGA functionals": {
        "TPSS": "The TPSS meta-GGA functional",
        "TPSSh": "The hybrid version of TPSS (10% HF exchange)",
        "TPSS0": "A 25% exchange version of TPSSh that yields improved "
        "energetics compared to TPSSh but is otherwise not well tested",
        "M06L": "The Minnesota M06-L meta-GGA functional",
        "M06": "The M06 hybrid meta-GGA (27% HF exchange)",
        "M062X": "The M06-2X version with 54% HF exchange"},

    "Range-separated hybrid functionals": {
        "wB97": "Head-Gordon's fully variable DF wB97",
        "wB97X": "Head-Gordon's DF wB97X with minimal Fock exchange",
        "wB97X-D3": "Chai's refit incl. D3 correction",
        "CAM-B3LYP": "Handy's fit",
        "LC-BLYP": "Hirao's original application"},

    "Perturbatively corrected double-hybrid functionals": {
        "B2PLYP": "The new mixture of MP2 and DFT from Grimme",
        "RI-B2PLYP": "B2PLYP with RI applied to the MP2 part",
        "B2PLYP-D": "B2PLYP with Grimme's empirical dispersion correction "
        "from 2006 (D2)",
        "B2PLYP-D3": "B2PLYP with Grimme's atom-pairwise dispersion "
        "correction from 2010 and Becke-Johnson damping (D3BJ)",
        "RI-B2PLYP RIJONX": "The same but with RI also applied in the SCF part",
        "mPW2PLYP": "mPW exchange instead of B88 (also with RI and RIJONX as "
        "above for B2PLYP). mPW is supposed to improve on weak interactions",
        "mPW2PLYP-D": "mPW2PLYP with Grimme's empirical dispersion correction "
        "from 2006 (D2)",
        "B2GP-PLYP": "Gershom Martin's 'general purpose' reparameterization",
        "B2K-PLYP": "Gershom Martin's 'kinetic' reparameterization",
        "B2T-PLYP": "Gershom Martin's 'thermochemistry' reparameterization",
        "PWPB95": "Hybrid functional with MP2 mixture from Grimme",
        "RI-PWPB95": "PWPB95 with RI for the MP2 part"},

    "Dispersion corrections": {
        "D3BJ": "Atom-pairwise dispersion correction to the DFT energy with "
        "Becke-Johnson damping (recommended)",
        "D3ZERO": "Atom-pairwise dispersion correction with zero damping",
        "D2": "Empirical dispersion correction from 2006 (not recommended)"}}

# for i in dens_functionals:
#     A = dens_functionals[i]
#     print(dens_dens_functionals[i][A])