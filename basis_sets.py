# To reduce the size of the deys in the dictionaries, long strings were
# replaced by smaller and more suitable variables

pople = "Pople-style basis sets"
def2 = "The def2 basis sets of the Karlsruhe group"
def1 = "Older ('def') Ahlrichs basis sets"
dif_def2 = "Diffuse def2 basis sets"
rel_def2 = "Relativistically recontracted Karlsruhe basis sets"
sarc = "SARC (Segmented all-electron relativistically contracted) basis sets"
sarc2 = "SARC2 basis sets for the lanthanides"
jensen = "Jensen basis sets"
sapporo = "Sapporo basis bets"
cc = "Correlation-consistent basis sets"
rel_cc = "DKH versions of correlation-consistent basis sets"
ecp_cc = "ECP-based versions of correlation-consistent basis sets"
f12 = "F12 and F12-CABS basis sets"
ANO = "Atomic Natural Orbital basis sets"
misc_bs = "Miscellaneous and specialized basis sets"

# Dictionary with the basis sets provided with ORCA 4.0.0

basis_sets = {
    pople: {
        "3-21G": "Pople 3-21G (H-Cs)",
        "STO-3G": "Minimal basis set(H-I)",
        "3-21GSP": "Buenker 3-21GSP (H-Ar)",
        "4-22GSP": "Buenker 4-22GSP (H-Ar)",
        "6-31G": "Pople 6-31G and its modifications (H-Zn)",
        "m6-31G": "Modified 6-31G for 3d transition metals (Sc-Cu)",
        "6-311G": "Pople 6-311G and its modifications (H-Br)"},

    def2: {
        "def2-SVP": "Valence double-zeta basis set with 'new' polarization functions",
        "def2-SV(P)": "The above with slightly reduced polarization",
        "def2-TZVP": "Valence triple-zeta basis set with 'new' polarization "
                     "functions. Note that this is quite similar to the older ('def') TZVPP "
                     "for the main group elements and TZVP for hydrogen.",
        "def2-TZVP(-f)": "TZVP with f polarization removed from main group elements",
        "def2-TZVPP": "TZVPP basis set with 'new' polarization functions",
        "def2-QZVPP": "Accurate polarized quadruple-zeta basis"},

    def1: {
        "SV": "Valence double-zeta basis set",
        "SV(P)": "Valence double-zeta with polarization only on heavy elements",
        "SVP": "Polarized valence double-zeta basis set",
        "TZV": "Valence triple-zeta basis set",
        "TZV(P)": "Valence triple-zeta with polarization on heavy elements",
        "TZVP": "Polarized valence triple-zeta basis set",
        "TZVPP": "Doubly polarized triple-zeta basis set",
        "QZVP": "Polarized valence quadruple-zeta basis set",
        "QZVPP": "Doubly polarized quadruple-zeta basis set"},

    dif_def2: {
        "ma-def2-SVP": "Minimally augmented def2-SVP basis set",
        "ma-def2-SV(P)": "Minimally augmented def2-SV(P) basis set",
        "ma-def2-TZVP": "Minimally augmented def2-TZVP basis set",
        "ma-def2-TZVP(-f)": "Minimally augmented def2-TZVP(-f ) basis set",
        "ma-def2-TZVPP": "Minimally augmented def2-TZVPP basis set",
        "ma-def2-QZVPP": "Minimally augmented def2-QZVPP basis set",
        "def2-SVPD": "Diffuse def2-SVP basis set for property calculations",
        "def2-TZVPD": "Diffuse def2-TZVP basis set for property calculations",
        "def2-TZVPPD": "Diffuse def2-TZVPP basis set for property calculations",
        "def2-QZVPD": "Diffuse def2-QZVP basis set for property calculations",
        "def2-QZVPPD": "Diffuse def2-QZVPP basis set for property calculations"},

    rel_def2: {
        "DKH-def2-SVP": "Retain the original def2 exponents but have only one "
                        "contracted function per angular momentum",
        "DKH-def2-SV(P)": "Retain the original def2 exponents but have only one "
                          "contracted function per angular momentum",
        "DKH-def2-TZVP": "Retain the original def2 exponents but have only one "
                         "contracted function per angular momentum",
        "DKH-def2-TZVP(-f)": "Retain the original def2 exponents but have only one "
                             "contracted function per angular momentum",
        "DKH-def2-TZVPP": "Retain the original def2 exponents but have only one "
                          "contracted function per angular momentum",
        "DKH-def2-QZVPP": "Retain the original def2 exponents but have only one "
                          "contracted function per angular momentum",
        "ZORA-def2-SVP": "Retain the original def2 exponents but have only one "
                         "contracted function per angular momentum",
        "ZORA-def2-SV(P)": "Retain the original def2 exponents but have only one "
                           "contracted function per angular momentum",
        "ZORA-def2-TZVP": "Retain the original def2 exponents but have only one "
                          "contracted function per angular momentum",
        "ZORA-def2-TZVP(-f)": "Retain the original def2 exponents but have only one "
                              "contracted function per angular momentum",
        "ZORA-def2-TZVPP": "Retain the original def2 exponents but have only one "
                           "contracted function per angular momentum",
        "ZORA-def2-QZVPP": "Retain the original def2 exponents but have only one "
                           "contracted function per angular momentum",
        "ma-DKH-def2-SVP": "Retain the original def2 exponents but have only one "
                           "contracted function per angular momentum",
        "ma-DKH-def2-SV(P)": "Retain the original def2 exponents but have only one "
                             "contracted function per angular momentum",
        "ma-DKH-def2-TZVP": "Retain the original def2 exponents but have only one "
                            "contracted function per angular momentum",
        "ma-DKH-def2-TZVP(-f)": "Retain the original def2 exponents but have only one "
                                "contracted function per angular momentum",
        "ma-DKH-def2-TZVPP": "Retain the original def2 exponents but have only one "
                             "contracted function per angular momentum",
        "ma-DKH-def2-QZVPP": "Retain the original def2 exponents but have only one "
                             "contracted function per angular momentum",
        "ma-ZORA-def2-SVP": "Retain the original def2 exponents but have only one "
                            "contracted function per angular momentum",
        "ma-ZORA-def2-SV(P)": "Retain the original def2 exponents but have only one "
                              "contracted function per angular momentum",
        "ma-ZORA-def2-TZVP": "Retain the original def2 exponents but have only one "
                             "contracted function per angular momentum",
        "ma-ZORA-def2-TZVP(-f)": "Retain the original def2 exponents but have only one "
                                 "contracted function per angular momentum",
        "ma-ZORA-def2-TZVPP": "Retain the original def2 exponents but have only one "
                              "contracted function per angular momentum",
        "ma-ZORA-def2-QZVPP": "Retain the original def2 exponents but have only one "
                              "contracted function per angular momentum"},

    sarc: {
        "SARC-DKH-SVP": "5d transition metals only",
        "SARC-DKH-TZVP": "Available for elements beyond Xe",
        "SARC-DKH-TZVPP": "Available for elements beyond Xe",
        "SARC-ZORA-SVP": "5d transition metals only",
        "ARC-ZORA-TZVP": "Available for elements beyond Xe",
        "SARC-ZORA-TZVPP": "Available for elements beyond Xe"},

    sarc2: {
        "SARC2-DKH-QZV": "SARC2 basis set of valence quadruple-zeta quality",
        "SARC2-DKH-QZVP": "Extended with NEVPT2-optimized (3g2h) polarization",
        "SARC2-ZORA-QZV": "SARC2 basis set of valence quadruple-zeta quality",
        "SARC2-ZORA-QZVP": "Extended with NEVPT2-optimized (3g2h) polarization"},

    jensen: {
        "PC-0": "'Polarization-consistent' generally contracted basis sets (H-Kr) "
                "of up to quintuple-zeta quality, optimized for SCF calculations",
        "PC-1": "'Polarization-consistent' generally contracted basis sets (H-Kr) "
                "of up to quintuple-zeta quality, optimized for SCF calculations",
        "PC-2": "'Polarization-consistent' generally contracted basis sets (H-Kr) "
                "of up to quintuple-zeta quality, optimized for SCF calculations",
        "PC-3": "'Polarization-consistent' generally contracted basis sets (H-Kr) "
                "of up to quintuple-zeta quality, optimized for SCF calculations",
        "PC-4": "'Polarization-consistent' generally contracted basis sets (H-Kr) "
                "of up to quintuple-zeta quality, optimized for SCF calculations",
        "aug-PC-0": "As above, augmented by diffuse functions",
        "aug-PC-1": "As above, augmented by diffuse functions",
        "aug-PC-2": "As above, augmented by diffuse functions",
        "aug-PC-3": "As above, augmented by diffuse functions",
        "aug-PC-4": "As above, augmented by diffuse functions",
        "PCseg-0": "Segmented PC basis sets (H-Kr), DFT-optimized",
        "PCseg-1": "Segmented PC basis sets (H-Kr), DFT-optimized",
        "PCseg-2": "Segmented PC basis sets (H-Kr), DFT-optimized",
        "PCseg-3": "Segmented PC basis sets (H-Kr), DFT-optimized",
        "PCseg-4": "Segmented PC basis sets (H-Kr), DFT-optimized",
        "aug-PCseg-0": "As above, augmented by diffuse functions",
        "aug-PCseg-1": "As above, augmented by diffuse functions",
        "aug-PCseg-2": "As above, augmented by diffuse functions",
        "aug-PCseg-3": "As above, augmented by diffuse functions",
        "aug-PCseg-4": "As above, augmented by diffuse functions",
        "PCSseg-0": "Segmented contracted basis sets (H{Kr) optimized "
                    "for nuclear magnetic shielding",
        "PCSseg-1": "Segmented contracted basis sets (H{Kr) optimized "
                    "for nuclear magnetic shielding",
        "PCSseg-2": "Segmented contracted basis sets (H{Kr) optimized "
                    "for nuclear magnetic shielding",
        "PCSseg-3": "Segmented contracted basis sets (H{Kr) optimized "
                    "for nuclear magnetic shielding",
        "PCSseg-4": "Segmented contracted basis sets (H{Kr) optimized "
                    "for nuclear magnetic shielding",
        "aug-PCSseg-0": "As above, augmented by diffuse functions",
        "aug-PCSseg-1": "As above, augmented by diffuse functions",
        "aug-PCSseg-2": "As above, augmented by diffuse functions",
        "aug-PCSseg-3": "As above, augmented by diffuse functions",
        "aug-PCSseg-4": "As above, augmented by diffuse functions",
        "PCJ-0": "Segmented contracted basis sets (H{Ar) optimized for "
                 "spin-spin coupling constants",
        "PCJ-1": "Segmented contracted basis sets (H-Ar) optimized for "
                 "spin-spin coupling constants",
        "PCJ-2": "Segmented contracted basis sets (H-Ar) optimized for "
                 "spin-spin coupling constants",
        "PCJ-3": "Segmented contracted basis sets (H-Ar) optimized for "
                 "spin-spin coupling constants",
        "PCJ-4": "Segmented contracted basis sets (H-Ar) optimized for "
                 "spin-spin coupling constants",
        "aug-PCJ-0": "As above, augmented by diffuse functions",
        "aug-PCJ-1": "As above, augmented by diffuse functions",
        "aug-PCJ-2": "As above, augmented by diffuse functions",
        "aug-PCJ-3": "As above, augmented by diffuse functions",
        "aug-PCJ-4": "As above, augmented by diffuse functions"},

    sapporo: {
        "Sapporo-DZP-2012": "All-electron generally contracted "
                            "non-relativistic basis sets (H-Xe)",
        "Sapporo-TZP-2012": "All-electron generally contracted "
                            "non-relativistic basis sets (H-Xe)",
        "Sapporo-QZP-2012": "All-electron generally contracted "
                            "non-relativistic basis sets (H-Xe)",
        "Sapporo-DKH3-DZP-2012": "All-electron basis sets optimized for the DKH3 "
                                 "Hamiltonian and finite nucleus (K{Rn)",
        "Sapporo-DKH3-TZP-2012": "All-electron basis sets optimized for the DKH3 "
                                 "Hamiltonian and finite nucleus (K{Rn)",
        "Sapporo-DKH3-QZP-2012": "All-electron basis sets optimized for the DKH3 "
                                 "Hamiltonian and finite nucleus (K{Rn)"},

    cc: {
        "cc-pVDZ": "Dunning correlation-consistent polarized double-zeta",
        "cc-pVTZ": "Dunning correlation-consistent polarized triple-zeta",
        "cc-pVQZ": "Dunning correlation-consistent polarized quadruple-zeta",
        "cc-pV5Z": "Dunning correlation-consistent polarized quintuple-zeta",
        "cc-pV6Z": "Dunning correlation-consistent polarized sextuple-zeta",
        "aug-cc-pVDZ": "Augmented with diffuse functions",
        "aug-cc-pVTZ": "Augmented with diffuse functions",
        "aug-cc-pVQZ": "Augmented with diffuse functions",
        "aug-cc-pV5Z": "Augmented with diffuse functions",
        "aug-cc-pV6Z": "Augmented with diffuse functions",
        "cc-pCVDZ": "Core-polarized basis sets",
        "cc-pCVTZ": "Core-polarized basis sets",
        "cc-pCVQZ": "Core-polarized basis sets",
        "cc-pCV5Z": "Core-polarized basis sets",
        "cc-pCV6Z": "Core-polarized basis sets",
        "aug-cc-pCVDZ": "As above, augmented with diffuse functions",
        "aug-cc-pCVTZ": "As above, augmented with diffuse functions",
        "aug-cc-pCVQZ": "As above, augmented with diffuse functions",
        "aug-cc-pCV5Z": "As above, augmented with diffuse functions",
        "aug-cc-pCV6Z": "As above, augmented with diffuse functions",
        "cc-pwCVDZ": "Core-polarized with weighted core functions",
        "cc-pwCVTZ": "Core-polarized with weighted core functions",
        "cc-pwCVQZ": "Core-polarized with weighted core functions",
        "cc-pwCV5Z": "Core-polarized with weighted core functions",
        "aug-cc-pwCVDZ": "As above, augmented with diffuse functions",
        "aug-cc-pwCVTZ": "As above, augmented with diffuse functions",
        "aug-cc-pwCVQZ": "As above, augmented with diffuse functions",
        "aug-cc-pwCV5Z": "As above, augmented with diffuse functions",
        "cc-pVD(+d)Z": "With tight d functions",
        "cc-pVT(+d)Z": "With tight d functions",
        "cc-pVQ(+d)Z": "With tight d functions",
        "cc-pV5(+d)Z": "With tight d functions"},

    rel_cc: {
        "cc-pVDZ-DK": "Correlation-consistent all-electron basis sets "
                      "for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian",
        "cc-pVTZ-DK": "Correlation-consistent all-electron basis sets "
                      "for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian",
        "cc-pVQZ-DK": "Correlation-consistent all-electron basis sets "
                      "for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian",
        "cc-pV5Z-DK": "Correlation-consistent all-electron basis sets "
                      "for use with the 2nd-order Douglas-Kroll-Hess Hamiltonian",
        "aug-cc-pVDZ-DK": "As above, augmented with diffuse functions",
        "aug-cc-pVTZ-DK": "As above, augmented with diffuse functions",
        "aug-cc-pVQZ-DK": "As above, augmented with diffuse functions",
        "aug-cc-pV5Z-DK": "As above, augmented with diffuse functions",
        "cc-pwCVDZ-DK": "DK versions of weighted core correlation-consistent basis sets",
        "cc-pwCVTZ-DK": "DK versions of weighted core correlation-consistent basis sets",
        "cc-pwCVQZ-DK": "DK versions of weighted core correlation-consistent basis sets",
        "cc-pwCV5Z-DK": "DK versions of weighted core correlation-consistent basis sets",
        "aug-cc-pwCVDZ-DK": "Weighted-core DK basis sets with diffuse functions",
        "aug-cc-pwCVTZ-DK": "Weighted-core DK basis sets with diffuse functions",
        "aug-cc-pwCVQZ-DK": "Weighted-core DK basis sets with diffuse functions",
        "aug-cc-pwCV5Z-DK": "Weighted-core DK basis sets with diffuse functions"},

    ecp_cc: {
        "cc-pVDZ-PP": "Correlation-consistent all-electron basis sets "
                      "combined with SK-MCDHF-RSC effective core potentials",
        "cc-pVTZ-PP": "Correlation-consistent all-electron basis sets "
                      "combined with SK-MCDHF-RSC effective core potentials",
        "cc-pVQZ-PP": "Correlation-consistent all-electron basis sets "
                      "combined with SK-MCDHF-RSC effective core potentials",
        "cc-pV5Z-PP": "Correlation-consistent all-electron basis sets "
                      "combined with SK-MCDHF-RSC effective core potentials",
        "aug-cc-pVDZ-PP": "As above, augmented with diffuse functions",
        "aug-cc-pVTZ-PP": "As above, augmented with diffuse functions",
        "aug-cc-pVQZ-PP": "As above, augmented with diffuse functions",
        "aug-cc-pV5Z-PP": "As above, augmented with diffuse functions",
        "cc-pwCVDZ-PP": "With weighted core functions",
        "cc-pwCVTZ-PP": "With weighted core functions",
        "cc-pwCVQZ-PP": "With weighted core functions",
        "cc-pwCV5Z-PP": "With weighted core functions",
        "aug-cc-pwCVDZ-PP": "As above, augmented with diffuse functions",
        "aug-cc-pwCVTZ-PP": "As above, augmented with diffuse functions",
        "aug-cc-pwCVQZ-PP": "As above, augmented with diffuse functions",
        "aug-cc-pwCV5Z-PP": "As above, augmented with diffuse functions"},

    f12: {
        "cc-pVDZ-F12": "Special orbital basis sets for F12 calculations "
                       "(larger than the regular D, T, Q-zeta basis sets!)",
        "cc-pVTZ-F12": "Special orbital basis sets for F12 calculations "
                       "(larger than the regular D, T, Q-zeta basis sets!)",
        "cc-pVQZ-F12": "Special orbital basis sets for F12 calculations "
                       "(larger than the regular D, T, Q-zeta basis sets!)",
        "cc-pCVDZ-F12": "With core polarization functions",
        "cc-pCVTZ-F12": "With core polarization functions",
        "cc-pCVQZ-F12": "With core polarization functions",
        "cc-pVDZ-PP-F12": "ECP-based versions",
        "cc-pVTZ-PP-F12": "ECP-based versions",
        "cc-pVQZ-PP-F12": "ECP-based versions",
        "cc-pVDZ-F12-CABS": "Near-complete auxiliary basis sets for F12 calculations",
        "cc-pVTZ-F12-CABS": "Near-complete auxiliary basis sets for F12 calculations",
        "cc-pVQZ-F12-CABS": "Near-complete auxiliary basis sets for F12 calculations",
        "cc-pVDZ-F12-OptRI": "With RI",
        "cc-pVTZ-F12-OptRI": "With RI",
        "cc-pVQZ-F12-OptRI": "With RI",
        "cc-pCVDZ-F12-OptRI": "With RI",
        "cc-pCVTZ-F12-OptRI": "With RI",
        "cc-pCVQZ-F12-OptRI": "With RI",
        "cc-pVDZ-PP-F12-OptRI": "With RI",
        "cc-pVTZ-PP-F12-OptRI": "With RI",
        "cc-pVQZ-PP-F12-OptRI": "With RI",
        "aug-cc-pVDZ-PP-F12-OptRI": "With RI",
        "aug-cc-pVTZ-PP-F12-OptRI": "With RI",
        "aug-cc-pVQZ-PP-F12-OptRI": "With RI",
        "aug-cc-pV5Z-PP-F12-OptRI": "With RI",
        "aug-cc-pwCVDZ-PP-F12-OptRI": "With RI",
        "aug-cc-pwCVTZ-PP-F12-OptRI": "With RI",
        "aug-cc-pwCVQZ-PP-F12-OptRI": "With RI",
        "aug-cc-pwCV5Z-PP-F12-OptRI": "With RI"},

    ANO: {
        "ano-pVDZ": "Very accurate basis sets that are "
                    "signifcantly better than the cc-pVnZ counterparts "
                    "for the same number of basis",
        "ano-pVTZ": "Very accurate basis sets that are "
                    "signifcantly better than the cc-pVnZ counterparts "
                    "for the same number of basis",
        "ano-pVQZ": "Very accurate basis sets that are "
                    "signifcantly better than the cc-pVnZ counterparts "
                    "for the same number of basis",
        "ano-pV5Z": "Very accurate basis sets that are "
                    "signifcantly better than the cc-pVnZ counterparts "
                    "for the same number of basis",
        "saug-ano-pVDZ": "Augmentation with a single set of sp functions. Greatly "
                         "enhances the accuracy of the SCF energies but not for "
                         "correlation energies",
        "saug-ano-pVTZ": "Augmentation with a single set of sp functions. Greatly "
                         "enhances the accuracy of the SCF energies but not for "
                         "correlation energies",
        "saug-ano-pVQZ": "Augmentation with a single set of sp functions. Greatly "
                         "enhances the accuracy of the SCF energies but not for "
                         "correlation energies",
        "aug-ano-pVDZ": "Full augmentation with spd, spdf, spdfg set of "
                        "polarization functions. Almost as expensive as the "
                        "next higher basis set. In fact, aug-ano-pVnZ = "
                        "ano-pV(n + 1)Z with the highest angular momentum "
                        "polarization function deleted",
        "aug-ano-pVTZ": "Full augmentation with spd, spdf, spdfg set of "
                        "polarization functions. Almost as expensive as the "
                        "next higher basis set. In fact, aug-ano-pVnZ = "
                        "ano-pV(n + 1)Z with the highest angular momentum "
                        "polarization function deleted",
        "aug-ano-pVQZ": "Full augmentation with spd, spdf, spdfg set of "
                        "polarization functions. Almost as expensive as the "
                        "next higher basis set. In fact, aug-ano-pVnZ = "
                        "ano-pV(n + 1)Z with the highest angular momentum "
                        "polarization function deleted",
        "ANO-RCC-FULL": "The complete ANO-RCC basis sets (H-Cm)",
        "ANO-RCC-DZP": "Contraction of ANO-RCC-FULL",
        "ANO-RCC-TZP": "Contraction of ANO-RCC-FULL",
        "ANO-RCC-QZP": "Contraction of ANO-RCC-FULL"},

    misc_bs: {
        "D95": "Dunning's double-zeta basis set (H-Cl)",
        "D95p": "Polarized version of D95",
        "MINI": "Huzinaga's minimal basis set",
        "MINIS": "Scaled version of the MINI",
        "MIDI": "Huzinaga's valence double-zeta basis set",
        "MINIX": "Combination of small basis sets by Grimme",
        "Wachters+f": "First-row transition metal basis set (Sc-Cu)",
        "Partridge-1": "Uncontracted basis sets by Partridge",
        "Partridge-2": "Uncontracted basis sets by Partridge",
        "Partridge-3": "Uncontracted basis sets by Partridge",
        "Partridge-4": "Uncontracted basis sets by Partridge",
        "LANL2DZ": "Los Alamos valence double-zeta with Hay-Wadt ECPs",
        "LANL2TZ": "Triple-Zeta version",
        "LANL2TZ(f)": "Triple-zeta plus polarization",
        "LANL08": "Uncontracted basis set",
        "LANL08(f)": "Uncontracted basis set + polarization",
        "EPR-II": "Barone's basis set (H, B-F) for EPR calculations (double-zeta)",
        "EPR-III": "Barone's basis set for EPR calculations (triple-zeta)",
        "IGLO-II": "Kutzelnigg's basis set (H, B-F, Al-Cl) for NMR and EPR "
                   "calculations",
        "IGLO-III": "Larger version of IGLO-II",
        "aug-cc-pVTZ-J": "Sauer's basis set for accurate hyperfine coupling constants"}}

for i in basis_sets:
    print(*[i])
    for j in basis_sets[i]:
        print("\t\t" + j, ":", basis_sets[i][j])

# Auxiliary basis sets starts here (ORCA 4.0.0)

